# import pandas as pd
# from threading import Thread
# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.cluster import KMeans
# from sklearn import preprocessing
# from scipy.cluster.hierarchy import linkage, dendrogram
# from ..models import *
# import sqlite3, os, sys

j = 5
class Good():
    jj = j

    def __init__(self, gg):
        print(gg)

    def get_jj(self):
        print(jj)


a = Good("Hi")









# def first_five():
#     path = __file__.split("\\")
#     path = "/".join(path[:-1])
#     path = path + "/"

#     dfStr = pd.read_csv(path + 'checks_str.txt', sep='\t')   #Читаем чеки
#     names = pd.read_csv(path + 'id.txt', sep='\t', names=['idtov','name'])  #Читаем ID каждого товара
#     data = pd.merge(dfStr, names, on='idtov')

#     print("dfStr: ",dfStr, sep="\n")


#     # test_dict = []
#     # for check in Checks.objects.all()[:50]:
#     #     for tovar in check.tovars.all():
#     #         test_dict.append({"iddoc": check.iddoc, "idtov": tovar.idtov})
#     # test_df = pd.DataFrame(test_dict)

#     # pytdfStr = pd.merge(pytdfStr, test_df, on = "iddoc")

#     pytdfStr = pd.DataFrame(list(Checks.objects.all().values())).drop(columns=["id", "createtime"])

#     print("pytdfStr: ",pytdfStr, sep="\n")

#     test_dict = []
#     for check in Checks.objects.all()[:10]:
#         for tovar in check.tovars.all():
#             test_dict.append({"iddoc": check.iddoc, "idtov": tovar.idtov})
#     test_df = pd.DataFrame(test_dict)

#     pytdfStr_good = pd.merge(pytdfStr, test_df, on = "iddoc")
#     print("pytdfStr_good",pytdfStr_good, sep="\n")



























    







# data = pd.merge(dfStr, names, on='idtov') #Объединение чеков с именами товаров 

# data = pd.merge(dfTitles, data, on='iddoc') # Объединение чеков с доп.инф по ним

# data = data.drop(columns=['docdate', 'return', 'store', 'kassa', 'seller', 'collector', 'idtov', 'price'])
# print(data.head())
# r = data.to_dict('records')

# for i in r:
#     i['name'] = i['name'].replace("  ", '')









# with sqlite3.connect(r"C:\Users\kasae\Desktop\PYTHON\PYTHON_NEW\Django\Rest-Api\drf\db.sqlite3") as db:
#     cursor = db.cursor()
#     cursor.executemany("INSERT INTO testApp_tovar(idtov, name) VALUES(:idtov, :name)", dict)

# print("Mission completed!")








# with sqlite3.connect(r"C:\Users\kasae\Desktop\PYTHON\PYTHON_NEW\Django\Rest-Api\drf\db.sqlite3") as db:
#     cursor = db.cursor()

#     cursor.execute("SELECT * from testApp_checks")
#     checkss = cursor.fetchall()

#     cursor.execute("SELECT * from testApp_tovar")
#     tovarss = cursor.fetchall()




# good_data = []

# def get_piece_of_data(checks, tovars):
#     global good_data

#     dictt = {}
#     for tovar in tovars:
#         dictt[tovar[2]] = {"id": tovar[0], "name": tovar[1]}

#     data = []
#     shet = 0
#     for check in checks:
#         tovars_in_check = dfStr[dfStr["iddoc"] == check[1]]
#         for idtov in tovars_in_check["idtov"].values:

#             try:
#                 data.append(
#                     {"checks_id":check[0], "tovar_id":dictt[idtov]["id"]}
#                 )
#                 # print({"checks_id":check[0], "tovar_id":dictt[idtov]["id"]})
#             except:
#                 print("Ошибка!")
#                 print("Checks_id - ", check[0])
#                 print("tovar_id - ", idtov)
#                 continue

#             shet += 1
#             if shet % 50 == 0:
#                 procents = format((len(data) / 54210) * 100, ".4f")
#                 print(procents + "% Выполнено!")
#     print("Готов один из потоков!")    
#     good_data.extend(data)        
            
            
            


# 542108
# t1 = Thread(target=get_piece_of_data, args=(checkss[:54210], tovarss))
# t2 = Thread(target=get_piece_of_data, args=(checkss[54210:108420], tovarss))
# t3 = Thread(target=get_piece_of_data, args=(checkss[108420:162630], tovarss))
# t4 = Thread(target=get_piece_of_data, args=(checkss[162630:216840], tovarss))
# t5 = Thread(target=get_piece_of_data, args=(checkss[216840:271050], tovarss))
# t6 = Thread(target=get_piece_of_data, args=(checkss[271050:325260], tovarss))
# t7 = Thread(target=get_piece_of_data, args=(checkss[325260:379470], tovarss))
# t8 = Thread(target=get_piece_of_data, args=(checkss[379470:433680], tovarss))
# t9 = Thread(target=get_piece_of_data, args=(checkss[433680:487890], tovarss))
# t10 = Thread(target=get_piece_of_data, args=(checkss[487890:], tovarss))

# threads = [t1,t2,t3,t4,t5,t6,t7,t8,t9,t10]


# # Start all threads
# for x in threads:
#     x.start()

# # Wait for all of them to finish
# for x in threads:
#     x.join()

# testth1 = Thread(target=get_piece_of_data, args=(checkss[:5], tovarss))
# testth2 = Thread(target=get_piece_of_data, args=(checkss[5:10], tovarss))

# threadstest = [testth1, testth2]

# # Start all threads
# for x in threadstest:
#     x.start()

# # Wait for all of them to finish
# for x in threadstest:
#     x.join()

# print(good_data)







# if good_data:
#     with sqlite3.connect(r"C:\Users\kasae\Desktop\PYTHON\PYTHON_NEW\Django\Rest-Api\drf\db.sqlite3") as db:
#         cursor = db.cursor()
#         cursor.execute("")
#         cursor.executemany("INSERT OR IGNORE INTO testApp_checks_tovars(checks_id, tovar_id) VALUES(:checks_id, :tovar_id)", good_data)

#     print("Mission completed!")







# a = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
# lists = [a,a]
# if a:
#     print(1)
