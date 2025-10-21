import pandas as pd

sampleData = {
    "Name": ["Alice", None, "Charlie", "David", "Eva", "Frank", "Grace", "Hannah", "Ian", "Jack"],
    "Age": [25, 30, 35, 40, 45, None, 55, 60, 65, 70],
    "Salary": [50000, 60000, 70000, 80000, 90000, 100000, 110000, 120000, 130000, 140000],
    "Performance": [85.0, 90.0, 75.0, 88.0, 92.0, None, 95.0, 80.0, 78.0, 85.0],
    "City": ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego", "Dallas", None]
}

sampleDF = pd.DataFrame(sampleData)

print("DataFrame after Dropping Rows with Missing Values:")
print(sampleDF.dropna())

print("DataFrame after Dropping Columns with Missing Values:")
print(sampleDF.dropna(axis=1))

print("DataFrame after Filling Missing Values:")
print(sampleDF.fillna(0))

print("DataFrame after Forward Fill:")
print(sampleDF.ffill())

print("DataFrame after Backward Fill:")
print(sampleDF.bfill())

print("DataFrame after Filling Missing Values with Column Mean:")
print(sampleDF.fillna(sampleDF.mean(numeric_only=True)))
