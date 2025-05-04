import  pandas as pd
import matplotlib.pyplot as plt

petsCSV = pd.read_csv('COA_OpenData.csv')
plt.rc ('font',family='Microsoft Jhenghei')
cats = petsCSV[petsCSV['animal_kind'].str.contains('貓')]
cats_total = cats['animal_id'].count()

dogs = petsCSV[petsCSV['animal_kind'].str.contains('狗')]
dogs_total = dogs['animal_id'].count()

othersX = petsCSV[petsCSV['animal_kind'].str.contains('狗|貓') == False]
others = petsCSV[petsCSV['animal_kind'].str.contains('其他')]
others_total = others['animal_id'].count()

# print(others_total)
plt.pie([dogs_total, cats_total, others_total],
        labels=['狗','貓','其他'],
        autopct='%.1f%%',
        explode=[0, 0, .6]

        )
plt.legend()
plt.show()