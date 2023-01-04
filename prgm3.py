import numpy as np
X=np.array([[3,5,8],[5,8,9],[7,3,2]])
print("Matrix X:",X)
exponent = 3
power = np.power(X,exponent)
print("Power of each matrix element is:",power)
identity =np.identity(3)
print("identity matrix is:",identity)
I =np.power(X,exponent)
print("Element wise power is:",I)
Y=np.array([[1,2,3],[4,5,6],[7,8,9]])
print("Matrix Y is:",Y)
A=np.dot(2,Y)
B=np.dot(X,X)
C=np.add(A,B)
print("X^2+2Y is:",C)

