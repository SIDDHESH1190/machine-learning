import numpy as np

num_arr = np.array([1, 2, 3, 4, 5])
print("Original Array:")
print(num_arr)
print("num_arr shape:")
print(num_arr.shape)

num_arr = np.array([[1, 2, 3.0], [4, 5, 6]])
print("2D Array:")
print(num_arr)
print("num_arr shape:")
print(num_arr.shape)
print("num_arr size:")
print(num_arr.size)
print("num_arr ndim:")
print(num_arr.ndim)

print("Array datatype : ")
print(num_arr.dtype)

num_arr = num_arr.astype(np.int32)
print("Array after conversion : ")
print(num_arr)
print("Array datatype after conversion : ")
print(num_arr.dtype)

new_arr = np.array([1,2,3,4,5,6,7,8,9,10])
new_arr= new_arr.astype(str)
print(new_arr.dtype)
