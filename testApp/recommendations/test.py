import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.cluster import KMeans
# from sklearn import preprocessing
# from scipy.cluster.hierarchy import linkage, dendrogram


# import sqlite3
# dfStr = pd.read_csv('checks_str.txt', sep='\t')   #Читаем чеки
# dfTitles = pd.read_csv('checks_titles.txt', sep='\t')   #Читаем доп.инфу по каждому чеку
# names = pd.read_csv('id.txt', sep='\t', names=['idtov','name'])  #Читаем ID каждого товара
# data = pd.merge(dfStr, names, on='idtov') #Объединение чеков с именами товаров 

# data = pd.merge(dfTitles, data, on='iddoc') # Объединение чеков с доп.инф по ним

# data = data.drop(columns=['docdate', 'return', 'store', 'kassa', 'seller', 'collector', 'idtov', 'price'])
# r = data.to_dict('records')

# for i in r:
#     i['name'] = i['name'].replace("  ", '')



# with sqlite3.connect(r"C:\Users\kasae\Desktop\PYTHON\PYTHON_NEW\Django\Rest-Api\drf\db.sqlite3") as db:
#     cursor = db.cursor()

#     cursor.executemany("INSERT INTO testApp_tovars(iddoc, kolvo, summa, name) VALUES(:iddoc, :count, :summa, :name)", r)

# print("Mission completed!")

