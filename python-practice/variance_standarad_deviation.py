import numpy as np

scores = [65, 72, 78, 85, 90, 92, 88, 76, 82, 95]

mean_score = np.mean(scores)
print(f"Mean : {mean_score}")

differences = [(x-mean_score) for x in scores]
print(f"\nDifferences from mean: {[f'{d:.1f}' for d in differences]}")

squared_diffs = [(x-mean_score) ** 2 for x in scores]
print(f"Squared differences : {[f'{d:.1f}' for d in squared_diffs]}")

variance = np.var(scores)
print(f"\n Variance {variance:.2f}")
# = Sum of squared differences / count


# STANDARD DEVIATION: Square root of variance
std_dev = np.std(scores)
print(f"Standard devoation: {std_dev:.2f}")
# sqrt(variance)

print("\n" + "="*50)
print("Interpretation")
print("="*50)

print(f"Mean: {mean_score}")
print(f"Std dev: ±{std_dev:.2f}")
print(f"\nMost scores are within ±1 std dev:")
print(f"{mean_score - std_dev:.1f} to {mean_score + std_dev:.1f}")


#verify
within_1_std = [s for s in scores if abs(s-mean_score) <= std_dev]
print(f" Actual: {len(within_1_std)}/10 scores = {len(within_1_std)*10}%")

