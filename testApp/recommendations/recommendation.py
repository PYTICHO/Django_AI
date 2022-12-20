import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn import preprocessing
from sklearn.cluster import DBSCAN


class Recommendation:

    def __init__(self):
        #                                                    Обучение ИИ
        num_clusters = 6
        train_count = 10000
        plotted_point_count = 500


        dfStr = pd.read_csv('testApp/recommendations/checks_str.txt', sep='\t')  # Читаем чеки
        # Читаем доп.инфу по каждому чеку
        dfTitles = pd.read_csv('testApp/recommendations/checks_titles.txt', sep='\t')
        # Читаем ID каждого товара
        names = pd.read_csv('testApp/recommendations/id.txt', sep='\t', names=['idtov', 'name'])
        # Объединение чеков с именами товаров
        data = pd.merge(dfStr, names, on='idtov')
        # Объединение чеков с доп.инф по ним
        data = pd.merge(dfTitles, data, on='iddoc')


        group_by_iddoc = data.groupby(['iddoc'])
        ch = group_by_iddoc.sum(numeric_only=True)
        ch['count_uniq_good'] = group_by_iddoc.size()

        checks = ch.drop(columns=["return", "kassa", "price"])  # Удаляем поля
        # Используем только чеки с  >=  3 товарами
        checks = checks[checks['count_uniq_good'] > 2]
        checks = checks[checks['summa'] > 0]  # Используем только чеки с суммой  >  0


        # cheks - чеки у которых больше 3-ех позиций и сумма больше 0
        # нормализация данных
        checks = pd.DataFrame(preprocessing.normalize(
            checks, axis=0), index=checks.index.values)  # Приводим все в числа от 0 до 1

        checks.columns = ["kolvo", "summa", "count_uniq_good"]

        # Обрезаем нашу таблицу до 10000 чеков
        trainDF = pd.DataFrame(checks[:train_count])
        # trainDF - таблица, которую мы используем для тренировки ИИ

        train = trainDF.values  # Достаем только значения


        #                            K-Means кластеризация


        model = KMeans(n_clusters=num_clusters)
        model.fit(train)



        #                             DB-Scan кластеризация 
        dbscan = DBSCAN(eps=0.0005, min_samples=100) #Радиус и миним. кол-во точек в радиусе
        dbscan.fit(trainDF)
        all_predictions = dbscan.labels_



        #                           Записываем для каждого чека его кластер


        dfrm = pd.Series({'predicted': all_predictions})
        trainDF['predicted'] = dfrm['predicted']

        self.model = model
        self.trainDF = trainDF
        self.data = data
        self.names = names





    # Получаем pandas таблицу с чеком (kolvo, summa, count_uniq_good)
    def get_recommendations(self, check, id_tovars):
        model = self.model
        trainDF = self.trainDF
        data = self.data
        names = self.names


        a = []
        for index, t in check.iterrows():
            closest = model.predict(np.array([t.values])) #получаем номер кластера тестового чека

            stop = False
            # Если в a не будет схожих товаров, то берем  кластер +- 1 
            for i in range(1,5):
                if not stop:
                    for j in [-1, 1]:
                        similar_checks = pd.DataFrame(trainDF[trainDF['predicted']==closest[0]]) #Все чеки с таким же кластером
                        check_content = id_tovars #Все товары тестового чека

                        #получить все товары из чеков с таким же кластером
                        train_tov = pd.DataFrame(data[data['iddoc'].isin(similar_checks.index.values)])

                        for check_index, tovar in check_content.iterrows():
                            #отбираем все товары (из чеков с таким же кластером) у которых есть товары, как в тестовом чеке
                            a.append(train_tov[train_tov['idtov'] == tovar['idtov']])

                        try:
                            if a[0].empty:
                                closest += (i*j)
                                a = []
                            else:
                                stop = True
                                break
                        except:
                            closest += (i*j)
                            a = []
                        
                else:
                    break


            if len(a) == 0:
                return None

            a = pd.concat(a) #Создаем таблицу
    
            #Группируем из отдельных товаров в один чек (чек  -  кол-во товаров)
            a = pd.DataFrame(a.groupby(['iddoc']).size().reset_index(name='count')) 
            a = a.sort_values(by=['count', 'iddoc'], ascending=False) # Сортируем
            # a - Таблица:  Чек  -  кол-во товаров в чеке 

            b = []
            for ind, k in a.iterrows():    #(76 эл.)
                t = pd.DataFrame(data[data["iddoc"]==a.loc[ind]['iddoc']])  #Как train_tov, но там мы берем только некоторые товары, а здесь все
                b.extend(t.values) 

            b = pd.DataFrame(b, columns = data.columns)
            summ = b.groupby(['idtov']).sum(numeric_only=True)    #Общая суммированная информация о каждом товаре
            summ['count_good'] = b.groupby(['idtov']).size()  #Добавление поля кол-ва товаров 
            summ = summ.sort_values(by = ['count_good'], ascending=False)  #Сортируем по кол-ву товаров

        summ = pd.merge(summ, names, on='idtov')



        for index, tov in check_content.iterrows():
            summ = summ[summ.idtov != tov.idtov]   #удаляем тестовые товары из summ
        summ = summ.sort_values(by = ['count_good'], ascending=False)

        recommended = summ[:25].to_dict('records')

        return recommended










