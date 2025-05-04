import matplotlib.pyplot as plt

plt.rc('font',family='Microsoft Jhenghei')

datas = [35,67,86]
labels = ['國中','高中', '大學']
plt.pie(
    datas,
    labels=labels,
    radius=1,
    labeldistance=1.1,
    textprops={'size':12, 'weight':'bold'},
    autopct='%.1f'
)
plt.legend()
plt.show()

# data2List=[30,70,50]
# total = sum(data2List)
# # sumData2=[str(100*d/total)+'%' for d in data2List]
# sumData2=[str(round(100*d/total))+'%' for d in data2List]
# print(sumData2)
