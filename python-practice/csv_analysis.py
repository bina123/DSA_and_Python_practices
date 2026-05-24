import pandas as pd

data = {
    'Date': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05'],
    'Product': ['A', 'B', 'A', 'C', 'B'],
    'Sales': [100, 150, 120, 200, 180],
    'Units': [10, 15, 12, 20, 18]
}

df = pd.DataFrame(data)

df.to_csv('python-practice/sales_data.csv',index=False)

df = pd.read_csv('python-practice/sales_data.csv')
print("Sales Data")
print(df)

# Analysis
print("\n Total Sales",df["Sales"].sum())
print("Average Unit Sold",df["Units"].mean())
print("\n Sales by product")
print(df.groupby('Product')['Sales'].sum().sort_values(ascending=False))

# Add calculated column
df["Price_Per_Unit"] = df["Sales"]/df["Units"]
print("\n With price per Unit")
print(df)

# Save processed data
df.to_csv("python-practice/sales_analyzed.csv",index=False)
print("\n Processed data saved")