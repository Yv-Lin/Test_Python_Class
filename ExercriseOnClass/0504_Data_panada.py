import pandas as pd

data = pd.Series([10,20,30,40,50])
data2 = pd.DataFrame(
                [
                    [1,2,3],
                    [4,5,6]
                ]
            )
# data3 = pd.DataFrame(
#       data: {
#                 'name':['Zac','Andy','Tim','Julian'],
#                 'age':[30,40,32,35]
#               }
# )

data4 = pd.DataFrame(
      [
        {'name':  'Zac','age':30,'gender':'M','weight':58},
        {'name':  'Andy','age':40,'gender':'M','weight':57},
        {'name':  'Tim','age':32,'gender':'M','weight':65},
        {'name':  'Julian','age':36,'gender':'F','weight':49},
        {'name':  'Lily','age':35,'gender':'F','weight':48}
      ]
)
# print(data4['weight'].max())
# print(data4['age'].min())
# print(data4['weight'].mean())

# 篩選資料
condition_1 = data4['age'] >= 30
condition = data4['gender'].str.contains('F')
print(data4[condition])