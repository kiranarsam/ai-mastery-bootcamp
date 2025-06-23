import numpy as np

A = np.array([[2,3], [1,4]])

# Linear Algerbra
# determinants  = det(A) = (ad-bc) for 2 * 2 matrix
determinant = np.linalg.det(A)
print("Determinant: ", determinant)

# Inverse Matrix = (1/det(A))*[[d -b], [-c a]]
inverse = np.linalg.inv(A)
print("Inverse of A: \n", inverse)


# Eigenvalues and EIgenvectors
eigenValues, eigenVectors = np.linalg.eig(A)
print("EigenValue:\n", eigenValues)
print("EigenVectors:\n", eigenVectors)

B = np.array([[4,2], [1,1]])
eigenValues, eigenVectors = np.linalg.eig(B)
print("EigenValue:\n", eigenValues)
print("EigenVectors:\n", eigenVectors)

# SVD
U, S, Vt = np.linalg.svd(A)
print("U:\n", U)
print("Singular Values:\n", S)
print("V Transpose:\n", Vt)
