import numpy as np

onesArray = np.ones((3,3), dtype=int)
print("Original Array:")
print(onesArray)

zerosArray = np.zeros((3,3), dtype=int)
print("Zeros Array:")
print(zerosArray)

fullArray = np.full((3,3), 12, dtype=float)
print("Full Array with 12s:")
print(fullArray)

identityArray = np.eye(3, dtype=float)
print("Identity Matrix:")
print(identityArray)

tableOf3 = np.arange(3, 3*10+1, 3)
print("Table of 3:")
print(tableOf3)
print("Shape of Table of 3:", tableOf3.shape)

randomArray = np.random.rand(3,4)
print("Random Array:")
print(randomArray)
print("Shape of Random Array:", randomArray.shape)