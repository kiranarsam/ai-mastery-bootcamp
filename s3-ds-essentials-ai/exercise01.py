import numpy as np

# arrays
arr = np.array([1,2,3,4])
print(arr)

# 3 x 3 matrix of an array
zeros = np.zeros((3,3))
print(zeros)
#print(len(zeros))

# 2 x 4 matrix of an array
ones = np.ones((2,4))
print(ones)

# range based with skip counting
range_array = np.arange(1, 10, 2)
print(range_array)

# lin space with interval
linspace_array = np.linspace(0, 1, 5)
print(linspace_array)
# output: [ 0. 0.25 0.5 0.75 1. ]

arr = np.array([1,2,3,4,5,6])

reshaped = arr.reshape((3,2))
print(reshaped)

arr = np.array([1,2,3])
expanded  = arr[:, np.newaxis]
print(expanded)
