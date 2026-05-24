import pandas as pd
import numpy as np

np.random.seed(42)

data = {
    'Name': ['Alice','Bob','Charlie','David','Eve','Frank'],
    'Department': ['Sales','IT','Sales','IT','HR','HR'],
    'Age': [25,30,35,28,32,45],
    'Salary': [50000,60000,55000,65000,58000,70000],
    'Experience': [2,5,7,3,6,15]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

# 1. Average salary by department
print("\n Average Salary by department")
print(df.groupby('Department')['Salary'].mean())

# 2. Employees with age > 30
print("\n Employee older than: 30")
print(df[df['Age'] > 30])

# 3. Add bonus column (10% of salary)
df['Bonus'] = df['Salary'] * 0.10
print("\n With Bonus Salary")
print(df)

# 4. Sort by salary descending
print("\n Sort by salary descending")
print(df.sort_values('Salary',ascending=False))

# 5. Statistics
print("\n Statistics")
print(df[['Age','Salary','Experience']].describe())