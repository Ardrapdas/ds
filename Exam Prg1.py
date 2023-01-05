import numpy as np
import matplotlib.pyplot as plt
X = np.array(['Mon','Tue','Wed','Thurs','Fri'])
Y = np.array([300,450,150,400,650])
plt.subplot(1,2,1)
plt.xlabel("Day")
plt.ylabel("Drinks")
plt.plot(X,Y,linestyle='dotted',color ='c',marker='d',mfc="green",mec='red')
plt.title("Daily Sales Data",loc ="center")
X = np.array(['Mon','Tue','Wed','Thur','Fri'])
Y = np.array([400,500,350,300,500])
plt.subplot(1,2,2)
plt.xlabel("Day")
plt.ylabel("Food")
plt.plot(X,Y,linestyle='dashed',color='y',marker='h',mfc='m',mec='k')
plt.title("Daily Sales Data",loc='center')
plt.show()