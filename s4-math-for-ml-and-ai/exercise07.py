import numpy as np

A = np.array([[4,-2], [1,1]])

eigvals, eigvecs = np.linalg.eig(A)

print("EigenValues:\n", eigvals)
print("EigenVectors:\n", eigvecs)
