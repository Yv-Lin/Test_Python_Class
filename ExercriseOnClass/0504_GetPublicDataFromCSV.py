import  pandas as pd

dataCSV = pd.read_csv('Ind_re.csv')
condition = dataCSV['地址'].str.contains('臺北市')
# result= dataCSV[condition]
# result = result.drop(['餐廳名稱','地址'])
print(result)
print(dataCSV.columns)
# print(datas['餐廳名稱'])

# dataCSV.to_excel('Restaurant_TPE.xlsx')
