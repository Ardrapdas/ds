import numpy as np
A = np.array([[2,1,-2],[3,0,1],[1,1,-1]])
print("Matrix A is:",A)
b = np.array([[-3],[5],[-2]])
print("Matrix b is:",b)
a = np.linalg.inv(A)
X = np.matmul(a,b)
print("The value of X is:",X)