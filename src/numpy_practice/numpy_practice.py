import numpy as np

oneDArr = np.array([1, 2, 3, 4, 5])
twoDArr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
threeDArr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

print("1D Array:")
print(oneDArr)
print("Shape of 1D Array:", oneDArr.shape)
print("2D Array:")
print(twoDArr)
print("Shape of 2D Array:", twoDArr.shape)

print("3D Array:")
print(threeDArr)
print("Shape of 3D Array:", threeDArr.shape)