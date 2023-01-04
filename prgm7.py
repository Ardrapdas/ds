import matplotlib.pyplot as plt
import numpy as np
x = np.array([2001,2002,2003,2004,2005,2006,2007])
y = np.array([24000,22500,19700,17500,14500,10000,5800])
plt.plot(x,y)
plt.xlabel('Year')
plt.ylabel('Car Value')
plt.title('Value Depreciation',loc='left')
plt.plot(x,y,linestyle='.',color='red',linewidth='2',marker='*',markerfacecolor='green',
markersize='20')
plt.show()
