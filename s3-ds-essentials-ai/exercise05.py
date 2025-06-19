import numpy as np

# Array and scalar broadcasting
arr = np.array([1,2,3])
print("arr: = ", arr)

print("arr + 10: ", arr + 10)

matrix = np.array([[1,2,3], [4,5,6]])
print("matrix: \n", matrix)
vector = np.array([1,0,1])
print("vector: \n", vector)

print("matrix + vector: \n", matrix + vector)

arr = np.array([[1,2,3], [4,5,6]])
print("arr: \n", arr)

print("Sum: ", np.sum(arr))
print("Mean: ", np.mean(arr))
print("Max: ", np.max(arr))
print("Min: ", np.min(arr))
print("Standard Deviation: ", np.std(arr))
print("Sum along rows: ", np.sum(arr, axis=1))
print("Sum along columns: ", np.sum(arr, axis=0))


# boolean *indexing and filtering
arr = np.array([1,2,3,4,5,6])

# New array with evens numbers
evens = arr[arr % 2 == 0]
print("Evens: ", evens)

# modified array, > 3 becomes 0
arr[arr > 3] = 0
print("Modified- Array: ", arr)

# this will help, generating random with same numbers
np.random.seed(42)

# random number generation and seeds
# random array with 3x3 matrix
random_array = np.random.rand(3,3)
print("Random Array: \n", random_array)

random_integers = np.random.randint(0, 10, size=(2,3))
print("Random Integers: \n", random_integers)
