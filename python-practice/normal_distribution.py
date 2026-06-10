import numpy as np
import matplotlib.pyplot as plt

# Generate normal distribution data
np.random.seed(42)
heights = np.random.normal(loc=170,scale=10, size=1000)
# loc = mean (170 cm)
# scale = std dev (10 cm)

print(f"Mean height: {np.mean(heights):.1f}")
print(f"Std dev: {np.std(heights):.1f}")

print("\n"+"="*50)
print("z-scores:")
print("="*50)

height= 180
z_score = (height-np.mean(heights)) / np.std(heights)
print(f"Height: {height} cm")
print(f"z-score: {z_score:.2f}")
print(f"Meaning: {z_score:.2f} starndard deviation above mean")

print("\n"+"="*50)
print("68-95-99.7 RULE:")
print("="*50)

mean = np.mean(heights)
std = np.std(heights)
print(f"68% of data: {mean-std:.1f} to {mean+std:.1f}")
print(f"95% of data: {mean-2*std:.1f} to {mean+2*std:.1f}")
print(f"99.7% of data: {mean-3*std:.1f} to {mean+3*std:.1f}")

# VISUALIZE (we'll use matplotlib)
plt.figure(figsize=(10,6))
plt.hist(heights, bins=30, density=True,alpha=0.7,color='blue',edgecolor='black')
plt.xlabel('Height (cm)')
plt.ylabel('Probability')
plt.title('Normal Distribution of Heights')
plt.axvline(np.mean(heights),color='red',linestyle='--',linewidth=2,label="Mean")
plt.axvline(np.mean(heights) + np.std(heights),color="green",linestyle='--',label="+- Std dev")
plt.axvline(np.mean(heights) - np.std(heights),color="green",linestyle="--")

plt.legend()
plt.show()