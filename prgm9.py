import matplotlib.pyplot as plt
x=['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
y=[173,153,195,147,120,144,148,109,174,130,172,131]
plt.scatter(x,y,color='r')
plt.xlabel('months of year',fontsize=18)
plt.ylabel('sales of segments')
plt.title(' sales data')
x=['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
y=[189,189,105,112,173,109,151,197,174,145,177,161]
plt.scatter(x,y,color='c')
x=['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
y=[185,185,126,134,196,153,112,133,200,145,167,110]
plt.scatter(x,y,color='k')
plt.show()