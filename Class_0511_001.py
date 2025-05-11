import matplotlib.pyplot as plt
import pandas as pd
plt.rc('font',family='Microsoft Jhenghei')
datas = pd.read_csv('../tmpYv/ExercriseOnClass/outbound.csv')

# x = ['A','B','C','D','E']
# h = [30,10,40,50,20]
#
# plt.bar(x,h)
#
# plt.show()

# print(datas.head())
# print(datas.columns[1:-1])
# print(datas)

x = datas.columns[2:-1]
h = [int(h) for h in datas.iloc[1][2:-1]]
# h = datas.iloc[1][2:-1]
# print(type(h))
# print(datas.iloc[1][2:-1])


plt.bar(x,h)
plt.show()