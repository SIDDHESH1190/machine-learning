import pandas as pd
from openpyxl.workbook import Workbook

# # smallDataDF = pd.read_csv('python_scripts\\resources\\small_data.csv', encoding='utf-8')
# # smallDataDF.to_excel('python_scripts\\resources\\excel_data.xlsx', index=False)


# sampleData = {
#     "Name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Hannah", "Ian", "Jack"],
#     "Age": [25, 30, 35, 40, 45, 50, 55, 60, 65, 70],
#     "Salary": [50000, 60000, 70000, 80000, 90000, 100000, 110000, 120000, 130000, 140000],
#     "Performance": [85.0, 90.0, 75.0, 88.0, 92.0, 70.0, 95.0, 80.0, 78.0, 85.0],
#     "City": ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose"]
# }

# sampleDF = pd.DataFrame(sampleData)

# # print("Dataframe Info:")
# # print(sampleDF)

# # print("\nDataframe Description:")
# # print(sampleDF.describe())

# # print(sampleDF.describe().quantile([0.25, 0.5, 0.75]))

# # print(sampleDF[["Salary","Performance"]].corr())


# # # ✅ CORRECT: Using & with parentheses
# # filteredDF = sampleDF[(sampleDF["Age"] > 30) & (sampleDF["Salary"] > 80000)]
# # print("Using & operator:")
# # print(filteredDF)
# # print("\n")

# # # ✅ CORRECT: Using query method
# # filteredDF_query = sampleDF.query("Age > 30 and Salary > 80000")
# # print("Using query method:")
# # print(filteredDF_query)

# ### Demonstrating DataFrame operations
# # newDF = sampleDF.assign(Bonus = sampleDF["Salary"] * 1.1)
# # print("DataFrame after adding Bonus column:")
# # print(newDF)

# # print("Old DataFrame remains unchanged:")
# # print(sampleDF)

# # sampleDF.loc[0:3, ["Name", "Salary"]] = [
# #     ["UpdatedName1", 99999],
# #     ["UpdatedName2", 88888], 
# #     ["UpdatedName3", 77777],
# #     ["UpdatedName4", 66666]
# # ]
# # print("DataFrame after modifying specific rows and columns:")
# # print(sampleDF)

# # Create a sample DataFrame
# df = pd.DataFrame({
#     'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
#     'Age': [25, 30, 35, 28, 32],
#     'City': ['New York', 'Los Angeles', 'Chicago', 'Miami', 'Seattle'],
#     'Salary': [50000, 60000, 70000, 55000, 65000],
#     'Department': ['HR', 'IT', 'Finance', 'HR', 'IT']
# })

# columns_to_select = ['Name', 'City','Salary']

# dynamic_subset = df[columns_to_select][df["Salary"] > 55000]
# print("Dynamic column selection:")
# print(dynamic_subset)

# department_summary = df[['Department', 'Salary']].groupby('Department').agg({
#     'Salary': ['mean', 'min', 'max', 'count']
# })
# print("Department salary summary:")
# print(department_summary)


# df = pd.DataFrame({
#     'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
#     'Age': [25, 30, 35, 28, 32],
#     'City': ['New York', 'Los Angeles', 'Chicago', 'Miami', 'Seattle'],
#     'Salary': [50000, 60000, 70000, 55000, 65000],
#     'Department': ['HR', 'IT', 'Finance', 'HR', 'IT']
# }, index=['A', 'B', 'C', 'D', 'E'])  # Custom index labels

# print("Original DataFrame:")
# print(df)
# print("\n" + "="*50 + "\n")

# # Select single row by label
# print("Single row (label 'A'):")
# print(df.loc[(df['Department'] == 'IT') & (df['Age'] > 30),['Name','City']])
# print(df[(df['Department'] == 'IT') & (df['Age'] > 30)][['Name','City']])


import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Alice', 'Bob', 'Diana'],
    'Age': [25, 30, 35, 25, 30, 40],
    'City': ['NYC', 'London', 'Paris', 'NYC', 'London', 'Tokyo'],
    'Salary': [50000, 60000, 70000, 50000, 65000, 80000]
}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

print("Unique")
print(df["City"].unique())