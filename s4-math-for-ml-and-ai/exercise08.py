import numpy as np

A = np.array([[3,1,1],[-1,3,1],[1,1,3]])

U, S, Vt = np.linalg.svd(A)

print("U:\n", U)
print("Singualr Values:\n", S)
print("V Transpose:\n", Vt)

# Reconstruct Matrix from U, S, and Vt
Sigma = np.zeros((3,3))
np.fill_diagonal(Sigma, S)
# @ means dot (matrix multiplication)
reconstructed = U @ Sigma @ Vt

print("Reconstructed Matrix \n:", reconstructed)
