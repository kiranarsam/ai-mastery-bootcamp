import numpy as np

A = np.array([[2,2,3],[4,5,6],[7,8,9]])

determinant = np.linalg.det(A)
inv1 = np.linalg.inv(A)

print("Determinant: ", determinant)
print("Inverse of A:\n", inv1)

# A.inv(A) = Identity Matrix
print("Identity Matrix:\n", A @ inv1)
