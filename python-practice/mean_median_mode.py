import numpy as np
from statistics import mean, median, mode


scores = [65, 72, 78, 85, 90, 92, 88, 76, 82, 95]

print("Data:", scores)


#Mean: Average
avg = np.mean(scores)
print(f"\n Mean (Average): {avg}")
# = (65+72+78+....+95)/10 = 82.3

#Median: Middle value when sorted
median = np.median(scores)
print(f"\n Median : {median}")
# Sort: [65, 72, 76, 78, 82, 85, 88, 90, 92, 95]
# Middle = (82 + 85) / 2 = 83.5

# MODE: Most frequent value
print(f"Mode (most frequent) : No repeat in this data")

scores_with_mode = [65, 72, 78, 85, 90, 90, 88, 76, 82, 90]
print(f"Mode example: {mode(scores_with_mode)}") #90 appears 3 times


print("\n" + "="*50)
print("when to use each")
print("="*50)
print("Mean: Normal data(no outliers)")
print("Median: Data with outliers(more robust)")
print("Mode: Categorial data (most commom category)")