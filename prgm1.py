import numpy as np
a=np.array([[2,4],[4,6]])
b=np.array([[5,2],[3,6]])
print("matrix addition is :")
c=a+b
print(c)
print("matrix subtraction is :")
d=a-b
print(d)
print("element wise multiplication")
e=np.multiply(a,b)
print(e)
print("division is :")
f=np.divide(a,b)
print(f)
print("matrix multiplication:")
g=np.matmul(a,b)
print(g)
print("transpose of multiplied matrix")
h=np.transpose(g)
print("diagonal elements")
i=np.diagonal(g)
print(i)
print("sum of diagonal elements")
print(sum(i))