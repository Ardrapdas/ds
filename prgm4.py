import numpy as np
arr = np.array([[2,3,6,7],
                [3,5,8,9],
                [4,8,6,7],
                [8,5,4,7]])
print("array is:",arr)
print("all elements excluding the first row\n",arr[1:4])
print("all elements excluding the last column\n",arr[:,0:3])
print("rows- 2,3 columns- 1,2 : \n",arr[1:3,0:2])
print("elements of 2 nd and 3 rd column : \n",arr[:,1:3])
print("2 nd and 3 rd element of 1 st row :\n",arr[0:,1:3])

