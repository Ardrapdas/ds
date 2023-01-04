import numpy as np
A = np.array([[3,7,0,],[2,5,4],[8,3,9]])
print("Matrix A is:",A)
U,D,VT = np.linalg.svd(A)
print("U is:",U)
print("D is:",D)
print("VT is:",VT)
A_remake = (U @ np.diag(D) @ VT)
print("Original matrix is:",A_remake)