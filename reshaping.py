import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

arr = arr.reshape(3,4)
print(arr)
arr = arr.reshape(4,3)
print(arr)
arr = arr.reshape(2,6)
print(arr)
arr = arr.reshape(12,)
print(arr)