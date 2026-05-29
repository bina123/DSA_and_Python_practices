import numpy as np
import pandas as pd

df = pd.read_csv('python-practice/titanic.csv')

print("\n Top 5")
print(df.head())

print("\n Column info")
print(df.info())

print("\n Basic statistics")
print(df.describe())

print("\n Missing Values")
print(df.isnull().sum())

print("\n Column names")
print(df.columns.to_list())

print("Orginal Shape: ",df.shape)
print("Missing Values")
print(df.isnull().sum())

#Step Drop rows with missing embarked (only 2)
df = df.dropna(subset=["embarked"])
print(f"\n After dropping emarked: {df.shape}")

# STEP 2: Drop 'deck' column (too many missing - 77%)
df = df.drop('deck',axis=1)
print(f"\n After dropping deck: {df.shape}")

# STEP 3: Fill missing 'age' with median age
median_age = df['age'].median()
df['age'] = df['age'].fillna(median_age)
print(f"\n Filled age with median : {median_age}")

# STEP 4: Check remaining missing values
print("\n Remaining missing values")
print(df.isnull().sum())

print(f"\nFinal cleaned shape: {df.shape}")

print("="*50)
print("SURVIVAL ANALYSIS")
print("="*50)

# Q1: Overall survival rate
survival_rate = df['survived'].mean()
print(f"\n1. Overall survival rate : {survival_rate:.2%}")

# Q2: Survival by gender
print("\n2. Survival by Gender:")
gender_survival = df.groupby('sex')['survived'].agg(['sum','count','mean'])
gender_survival.columns = ['Survived','Total','Rate']
print(gender_survival)

# Q3: Survival by class
print("\n3. Survival by ticket class:")
class_survival = df.groupby('pclass')['survived'].agg(['sum','count','mean'])
class_survival.columns = ['Survived','Total','Rate']
print(class_survival)

# Q4: Survival by age group
df['age_group'] = pd.cut(df['age'],bins=[0,12,18,35,60,100],
                         labels=['Child','Teen','Adult','Middle-aged','Elderly'])
print("\n4. Survival by Age Group:")
age_survival = df.groupby('age_group')['survived'].agg(['sum','count','mean'])
age_survival.columns = ['Survived','Total','Rate']
print(age_survival)

# Q5: Average fare by survival
print("\n5. Average Fare by Survival:")
fare_by_survival = df.groupby('survived')['fare'].mean()
print(fare_by_survival)

# Q6: Family size analysis+
df['family_size'] = df['sibsp'] + df['parch'] + 1
print("\n6. Survival by Family Size:")
family_survival = df.groupby('family_size')['survived'].agg(['sum','count','mean'])
family_survival.columns = ['Survived','Total','Rate']
print(family_survival)

# Q7: Pivot - Gender & Class Combined
print("\n7. Survival by Gender & Class (Pivot):")
pivot = df.pivot_table(values='survived', index="sex",columns='pclass',aggfunc='mean')
print(pivot)

# Add this to the end of your analysis

summary = {
    'Total Passengers': int(len(df)),
    'Survived': int(df['survived'].sum()),
    'Died': int((df['survived'] == 0).sum()),
    'Survival Rate': f"{df['survived'].mean():.2%}",
    'Female Survival': f"{df[df['sex']=='female']['survived'].mean():.2%}",
    'Male Survival': f"{df[df['sex']=='male']['survived'].mean():.2%}",
    'Average Age': float(df['age'].mean()),
    'Average Fare': float(df['fare'].mean())
}

import json
with open('python-practice/titanic_summary.json', 'w') as f:
    json.dump(summary, f, indent=2)

df.to_csv('python-practice/titanic_cleaned.csv')