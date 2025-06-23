import numpy as np

# Create matrix and vector
M = np.array([[1,2,3], [4,5,6], [7,8,9]])
V = np.array([1,0,-1])
print("M:\n", M)
print("V:\n", V)

# Matrix & Vector multiplication
result = np.dot(M, V)
print("Matrix . Vector Multiplication:\n", result)
