import numpy as np
import matplotlib.pyplot as plt

study_hours = np.array([2,3,4,5,6,7,8,9,10])
test_scores = np.array([50, 55, 65, 70, 75, 80, 85, 90, 95])

# Calculate correlation coefficient
correlation = np.corrcoef(study_hours,test_scores)[0,1]
print(f"Correlation (hours vs scores): {correlation:.3f}")
print(f"Interpretation: Strong positive correlstion (0.99)")
print(" -> More studying = Higher score\n")

# Example 2: Screen time vs Sleep (NEGATIVE correlation)
screen_time = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
sleep_hours = np.array([9, 8.5, 8, 7.5, 7, 6.5, 6, 5.5, 5])

correlation = np.corrcoef(screen_time,sleep_hours)[0,1]
print(f"Correlation (screen time vs sleep): {correlation:.3f}")
print("Interpretation: Strong Negative correlation (-0.99)")
print(" -> More screen time = Less sleep\n")

# Example 3: Shoe size vs IQ (NO correlation)
shoe_size = np.array([6, 7, 8, 9, 10, 11, 12, 13])
iq = np.array([100, 98, 105, 102, 99, 103, 101, 104])

correlation = np.corrcoef(shoe_size,iq)[0,1]
print(f"Correlation (shoe size vs IQ): {correlation:.3f}")
print("Interpretation: No correlation(0.15)")
print(" -> Shoe size tells us nothing about IQ\n")

print("="*50)
print("CORRELATION VALUES:")
print("="*50)
print("+1.0: Perfect positive (both increase together)")
print(" 0.0: No correlation (independent)")
print("-1.0: Perfect negative (one increases, other descreses)")
print("\n Correlation != Causation")
print("Example: Ice creame sales ↑ when drowning deaths ↑")
print(" Cause: Both increases in summer, not related!")

fig, axes = plt.subplots(1,3,figsize=(15,4))

axes[0].scatter(study_hours,test_scores, color="green")
axes[0].set_title("Positive correlation (r=0.99)")
axes[0].set_xlabel("Study hours")
axes[0].set_ylabel("Test Scores")

axes[1].scatter(screen_time,sleep_hours,color="red")
axes[1].set_title("Negative correlation (r=-0.99)")
axes[1].set_xlabel('Screen time (hrs)')
axes[1].set_ylabel('Sleep (hrs)')

axes[2].scatter(shoe_size,iq, color="blue")
axes[2].set_title("No correlation (r=0.15)")
axes[2].set_xlabel("Shoe size")
axes[2].set_ylabel("IQ")

plt.tight_layout()
plt.show()
