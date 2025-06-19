import numpy as np

a = np.array([1,2,3])
b = np.array([4,5,6])

print(a + b)
print(a * b)
print(a / b)

# mathematical array
arr = np.array([4, 16, 25])
print("Sum of an array: ", np.sum(arr))
print("Square root: ", np.sqrt(arr))
print("Mean value: ", np.mean(arr))
print("Maximum value: ", np.max(arr))

# array indexing, slicing and reshaping
arr = np.array([10, 20, 30, 40, 50, 60])
print(arr[2])
print(arr[-1])

print(arr[1:4])
print(arr[:3])
print(arr[3:])

# reshaping 2 x 3
reshaped = arr.reshape(2,3)
print(reshaped)
