from httpx import delete
import numpy as np

num_arr = np.array([12, 8, 20, 40, 5, 32])
print("Original Array:")
print(num_arr)

# print("Array after multiplication by 10:")
# print(num_arr * 10)

# print("Array after adding 5:")
# print(num_arr + 5)
# print("Array after subtracting 3:")
# print(num_arr - 3)
# print("Array after dividing by 2:")
# print(num_arr / 2)
# print("Array after integer division by 3:")
# print(num_arr // 3)
# print("Array after squaring each element:")
# print(num_arr ** 2)

# print("Array after taking square root of each element:")
# print(np.sqrt(num_arr))

# print("Mean of the array:")
# print(np.mean(num_arr))
# print("Sum of the array:")
# print(np.sum(num_arr))
# print("Maximum value in the array:")
# print(np.max(num_arr))
# print("Minimum value in the array:")
# print(np.min(num_arr))
# print("Standard Deviation of the array:")
# print(np.std(num_arr))
# print("Variance of the array:")
# print(np.var(num_arr))
# print("Index of Maximum value in the array:")
# print(np.argmax(num_arr))
# print("Index of Minimum value in the array:")
# print(np.argmin(num_arr))

# print(num_arr[5:0:-1])
# ## fancy indexing
# indices = [0, 2, 4]
# print(num_arr[indices])

# # boolean indexing
# print(num_arr[num_arr > 15])

# # conditional replacement
# modified_arr = np.where(num_arr > 15, 15, num_arr)
# print("Array after conditional replacement (values > 15 set to 15):")
# print(modified_arr)

# num_arr = num_arr.reshape(2,3)
# print("Array after reshaping to 5x1:")
# print(num_arr)

# num_arr =num_arr.reshape(3,2)
# num_arr = np.insert(num_arr, 1, 99, 0)
# print("Array after inserting 99 at the end:")
# print(num_arr)

num_arr = np.append(num_arr, 200)
print("Array after appending 200 at the end:")
print(num_arr)

num_arr = np.delete(num_arr, num_arr.size-1)
print("Array after deleting last element:")
print(num_arr)


amountArr = [100, 200, 300, 400, 500]
amountArr = np.array(amountArr) * 0.9
print("Array after 10% discount:")
print(amountArr)

matrix1 = np.array([[1, 2, 3], [4, 5, 6]])
matrix2 = np.array([[7, 8, 9], [10, 11, 12]])

print(f"{matrix1} * {matrix2} = {matrix1 * matrix2}")