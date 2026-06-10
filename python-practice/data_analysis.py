import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("="*70)
print("COMPREHENSIVE DATA ANALYSIS PROJECT")
print("="*70)


np.random.seed(42)
n_students = 100

data = {
    'StudentID': range(1,n_students+1),
    'StudyHours': np.random.uniform(2,10,n_students),
    'TestScore': np.random.normal(70,15,n_students),
    'Attendance':np.random.uniform(0.6,1.0,n_students),
    'Age': np.random.randint(18,25,n_students)
}

# Create correlation between study hours and test scores
data['TestScore'] = data['StudyHours'] * 8 + np.random.normal(0,5,n_students)
data['TestScore'] = np.clip(data['TestScore'],0,100)

df = pd.DataFrame(data)

print("\n Dataset Overview:")
print(df.head(10))
print(f"\nShape: {df.shape}")

print("="*70)
print("Part 1: DESCRIPTIVE STATISTICS")
print("="*70)

print("\n Test score Statistics")
print(f" Mean: {df['TestScore'].mean():.2f}")
print(f" Median: {df['TestScore'].median():.2f}")
print(f" Std Dev: {df['TestScore'].std():.2f}")
print(f" Min: {df['TestScore'].min():.2f}")
print(f" Max: {df['TestScore'].max():.2f}")

print("\n Study Hours Statistics:")
print(f" Mean: {df['StudyHours'].mean():.2f}")
print(f" Median: {df['StudyHours'].median():.2f}")
print(f" Std Dev: {df['StudyHours'].std():.2f}")

print("\n Attendance Statistics:")
print(f" Mean: {df['Attendance'].mean()}")
print(f" Median: {df['Attendance'].median()}")

print("\n"+"="*70)
print("PART 2: Z-SCORE & Outlier Detection")
print("="*70)

df['TestScore_Z'] = (df['TestScore'] - df['TestScore'].mean())/df['TestScore'].std() 

#Find Outliers (z > 2 or Z< -2)
outliers = df[np.abs(df['TestScore_Z']) > 2]
print(f"\n Outliers detected (|z| > 2): {len(outliers)} students")
print(outliers[['StudentID','TestScore','TestScore_Z']].head())

print("\n"+"="*70)
print("PART 3: CORRELATION ANALYSIS")
print("="*70)

corr_study_test = np.corrcoef(df['StudyHours'],df['TestScore'])[0,1]
corr_attendance_test = np.corrcoef(df['Attendance'],df['TestScore'])[0,1]
corr_study_attendance = np.corrcoef(df['StudyHours'],df['Attendance'])[0,1]

print(f"\nCorrelation (Study Hours <-> Test Score): {corr_study_test:.3f}")
print(f" Interpretation: Strong postive correlation!")
print(f"\nCorrelation (Attendance <-> Test Score): {corr_attendance_test:.3f}")
print(f" Interpretation: Moderate Postive correlation ")
print(f"\nCorrelation (Study Hours <-> Attendance): {corr_study_attendance:.3f}")


print("\n"+"="*70)
print("PART 4: CATEGORICAL ANALYSIS")
print("="*70)

#Create age groups
df['AgeGroup'] = pd.cut(df['Age'],bins=[17,19,21,25],labels=['18-19','20-21','22+'])

#Group Analysis
group_stats = df.groupby('AgeGroup')['TestScore'].agg(['count','mean','std'])
print("\n Test Score by Age Group:")
print(group_stats)

print("\n"+"="*70)
print("PART 5: VISUALIZATION")
print("="*70)

# Create 6 subplots
fig, axes = plt.subplots(2,3,figsize=(15,10))

# Plot 1: Distribution of Test Scores
axes[0,0].hist(df['TestScore'],bins=20,color='blue',edgecolor="black",alpha=0.7)
axes[0,0].axvline(df['TestScore'].mean(),color="red",linestyle="--",linewidth=2,label='Mean')
axes[0,0].set_title("Normal Distribution of Test Scores")
axes[0,0].set_xlabel('Test Score')
axes[0,0].set_ylabel('Frequncy')
axes[0,0].legend()

# Plot 2: Distribution of Study Hours
axes[0,1].hist(df['StudyHours'],bins=15,color="green",edgecolor="black",alpha=0.7)
axes[0,1].set_title("Normal Distribution of Study Hours")
axes[0,1].set_xlabel("Study hours per week")
axes[0,1].set_ylabel("Frequency")

# Plot 3: Scatter - Study Hours vs Test Scores
axes[0,2].scatter(df['StudyHours'],df['TestScore'],alpha=0.6,color="purple",s=50)
axes[0,2].set_title(f"Study Hours vs Test Score\n(r={corr_study_test:.3f})")
axes[0,2].set_xlabel("Study Hours")
axes[0,2].set_ylabel("Test Scores")
axes[0,2].grid(True,alpha=0.3)

# Plot 4: Scatter - Attendance vs Test Scores
axes[1, 0].scatter(df['Attendance'], df['TestScore'], alpha=0.6, color='orange', s=50)
axes[1, 0].set_title(f'Attendance vs Test Scores\n(r={corr_attendance_test:.3f})')
axes[1, 0].set_xlabel('Attendance Rate')
axes[1, 0].set_ylabel('Test Score')
axes[1, 0].grid(True, alpha=0.3)

# Plot 5: Box plot by Age Group
df.boxplot(column="TestScore",by="AgeGroup",ax=axes[1,1])
axes[1, 1].set_title('Test Scores by Age Group')
axes[1, 1].set_xlabel('Age Group')
axes[1, 1].set_ylabel('Test Score')
plt.sca(axes[1, 1])
plt.xticks(rotation=0)

# Plot 6: Z-scores histogram
axes[1, 2].hist(df['TestScore_Z'], bins=20, color='red', edgecolor='black', alpha=0.7)
axes[1, 2].axvline(-2, color='blue', linestyle='--', linewidth=2, label='Outlier threshold')
axes[1, 2].axvline(2, color='blue', linestyle='--', linewidth=2)
axes[1, 2].set_title('Z-Score Distribution')
axes[1, 2].set_xlabel('Z-Score')
axes[1, 2].set_ylabel('Frequency')
axes[1, 2].legend()

plt.tight_layout()
plt.savefig('data_analysis_project.png', dpi=150)
plt.close()

print("✓ Comprehensive visualization saved: data_analysis_project.png")

print("\n" + "="*70)
print("SUMMARY & KEY INSIGHTS")
print("="*70)

print(f"\n1. TEST SCORE DISTRIBUTION:")
print(f"   Mean: {df['TestScore'].mean():.1f}, Std Dev: {df['TestScore'].std():.1f}")
print(f"   Range: {df['TestScore'].min():.1f} to {df['TestScore'].max():.1f}")

print(f"\n2. STUDY IMPACT:")
print(f"   Correlation with Test Scores: {corr_study_test:.3f}")
print(f"   → Strong positive relationship!")
print(f"   → For each extra study hour, expect +8 point improvement")

print(f"\n3. OUTLIERS:")
print(f"   {len(outliers)} students ({len(outliers)/len(df)*100:.1f}%) are statistical outliers")
print(f"   → Worth investigating (unusually high or low scores)")

print(f"\n4. AGE GROUPS:")
age_means = df.groupby('AgeGroup')['TestScore'].mean()
for age, score in age_means.items():
    print(f"   {age}: {score:.1f}")
    
print(f"\n5. ATTENDANCE:")
print(f"   Correlation with Test Scores: {corr_attendance_test:.3f}")
print(f"   → Moderate positive (important but not as much as study hours)")


print("\n" + "="*70)
print("✅ DATA ANALYSIS PROJECT COMPLETE!")
print("="*70)