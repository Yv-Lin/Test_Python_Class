import  pandas as pd
import matplotlib.pyplot as plt

outTravelersCSV = pd.read_csv('出國旅客按目的地統計.csv')
plt.rc ('font',family='Microsoft Jhenghei')


labels = outTravelersCSV.columns[2:-1]


# data = outTravelersCSV.iloc[1][2:-1]
data = outTravelersCSV.iloc[3][2:-1]
print(data)

plt.pie(
    data,
    labels=labels,
    radius=1,
    labeldistance=1.1,
    autopct='%.2f%%'
)
plt.legend()
plt.show()










