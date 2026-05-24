import numpy as np

# 1. Create a 5x5 matrix of random integers between 1 and 100
matrix = np.random.randint(1,101,size=(5,5))

print("Matrix: ")
print(matrix)

# 2. Find mean of each row
row_means = matrix.mean(axis=1)
print("Row means: ", row_means)

# 3. Find max of each column
cols_max = matrix.max(axis=0)
print("Column maxs: ",cols_max)

# 4. Find elements greater than 50
print("\n Elements > 50")
print(matrix[matrix > 50])

# 5. Replace all values < 30 with 0
matrix_modified = matrix.copy()
matrix_modified[matrix_modified < 30] = 0
print("\n Matrix with value <30 replace by 0")
print(matrix_modified)

# 6. Calculate correlation between two arrays
arr1 = np.random.rand(100)
arr2 = np.random.rand(100)
correlation = np.corrcoef(arr1,arr2)[0,1]
print(f"\nCorrelation: {correlation:.3f}")
