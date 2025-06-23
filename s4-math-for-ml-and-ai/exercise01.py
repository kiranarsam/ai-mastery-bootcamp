# Vector
# 1 D array

# Matrix: 3 x 3 matrix as an example
import numpy as np

A = np.array([[1,2], [3,4]])
B = np.array([[5,6], [7,8]])

print("Addition: \n", A + B)
print("Subtraction: \n", B - A)

# 2 times A (scalar value)
C = 2 * A
print("Scalar Multiplication: \n", C)

# Matrix Multiplication
# | 1*5 + 2*7    1*6 + 2*8 |  ==> | 19  22 |
# | 3*5 + 4*7    3*6 + 4*8 |      | 43  50 |
result = np.dot(A, B)
print("Matrix Multiplication: \n", result)

# Identity Matrix ( i times A is A)
# I * A = A
I = np.eye(5)
print("Identity MAtrix: \n", I)

# Zero Matrix
Z = np.zeros((2,3))
print("Zero Matrix: \n", Z)

# Diagonal Matrix (Except diagonal, others are zero)
D = np.diag([1,2,3])
print("Diagonal Matrix: \n", D)
