import numpy as np

print("="*60)
print("Numpy advanced - Broadcasting")
print("="*60)

a = np.array([[1,2,3],[4,5,6]])

print("Array a 2 * 3:")
print(a)

b = np.array([10,20,30])
print("\n Array b 1*3:")
print(b)

# Add b to each row of a (broadcasting!)
result = a+b
print("\n a+b (broadcasting):")
print(result)
# NumPy automatically "broadcasts" b to match a's shape!

print("="*60)
print("Numpy advanced - Indexing & Slicing")
print("="*60)

arr = np.array([10,20,30,40,50,60,70,80,90])
print(f"Arr: {arr}")

print(f"\n Element > 50: {arr[arr > 50]}")
print(f"\n Element == 30: {arr[arr == 50]}")

# 2D indexing
matrix = np.array([[1,2,3],
                [4,5,6],
                [7,8,9]])
print(f"\nmatrix:\n{matrix}")

print(f"Element at [0,0], {matrix[0][0]}")
print(f"Row 1: {matrix[1,:]}")
print(f"Column 1: {matrix[:,1]}")

print("\n"+"="*60)
print("NUMPY advanced - Reshaping")
print("="*60)

arr = np.arange(12)
print(f"Original 1D: {arr}")

reshaped = arr.reshape(3,4)
print(f"\nReshaped to 3*4:\n{reshaped}")

reshaped  = arr.reshape(2,2,3)
print(f"\n Reshpaed to 2*2*3: \n{reshaped}")

print("\n"+"="*60)
print("Numpy Advanced - Aggregation")
print("="*60)

data = np.array([[1,2,3,4],
                 [5,6,7,8],
                 [9,10,11,12]])
print(f"\n Data:\n {data}")

print(f"\n Sum all: {np.sum(data)}")
print(f"\n Sum per row: {np.sum(data,axis=1)}")
print(f"\n Sum per column: {np.sum(data, axis=0)}")

print(f"\n Mean: {np.mean(data)}")
print(f"\n Mean per row: {np.mean(data,axis=1)}")

print(f"\n Max: {np.max(data)}")
print(f"\n Min: {np.min(data)}")

print("\n"+"="*60)
print("Numpy Advanced - Concatenate & stack")
print("="*60)

a = np.array([1,2,3])
b = np.array([4,5,6])

print(f"a: {a}")
print(f"b: {b}")

concat = np.concatenate([a,b])
print(f"\n Concatenate : {concat}")

stacked = np.stack([a,b])
print(f"\n Stack:\n{stacked}")

print("\n"+"="*60)
print("Numpy advanced - Element wise operations")
print("="*60)

a = np.array([1,2,3,4,5])
print(f"a: {a}")

print(f"\n a * 2: {a * 2}")
print(f"\n a ** 2: {a ** 2}")
print(f"np.sqrt(q): {np.sqrt(a)}")
print(f"np.exp(a): {np.exp(a)}")
print(f"np.log(a): {np.log(a)}")

# Element-wise between arrays
b = np.array([10,20,30,40,50])
print(f"\nb: {b}")
print(f"a+b:{a+b}")
print(f"a*b:{a*b}")
print(f"b/a:{b/a}")

print("\n"+"="*60)
print("Numpy - Random numbers (Important for ML!)")
print("="*60)


# Random uniform [0, 1)
print("Randon uniform [0,1):",np.random.random(5))

#Random integers
print("Random intergers 0-10:",np.random.randint(0,10,size=5))

#Random normal(Gaussian)
print("Random normal (μ=0, σ=1)",np.random.randn(3))

# With seed (reproducible)
np.random.seed(42)
print("\n With seed=42",np.random.randn(3))
np.random.seed(42)
print("\n Same seed: ",np.random.randn(3))