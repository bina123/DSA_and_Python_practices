import numpy as np
import pandas as pd

np.random.seed(42)

dates = pd.date_range('2024-01-01',periods=100)
products = ['Laptop','Phone','Tablet','Monitor','Keyboard']
regions = ['North','South','East','West']

data = {
    'Date': np.random.choice(dates,200),
    'Product': np.random.choice(products,200),
    'Region': np.random.choice(regions,200),
    'Units': np.random.randint(1,20,200),
    'Price': np.random.randint(50,2000,200)
}

df = pd.DataFrame(data)
df['Revenue'] = df["Units"] * df["Price"]

print("SAMPLE DATA:")
print(df.head(10))
print(f"\nTotal Rows: {len(df)}")

# Q1: What's the total revenue?
total_revenue = df['Revenue'].sum()
print(f"\n1. Total Revenue: ${total_revenue:,}")

# Q2: Which product generated the most revenue?
product_revenue = df.groupby('Product')['Revenue'].sum().sort_values(ascending=False)
print("\n2. Revenue by Product:")
print(product_revenue)

# Q3: Which region has the highest sales?
region_revenue = df.groupby('Region')['Revenue'].sum().sort_values(ascending=False)
print("\n3. Revenue by region: ")
print(region_revenue)

# Q4: Average units sold per product
average_units = df.groupby('Product')['Units'].mean().sort_values(ascending=False)
print("\n4. Average Units by Product:")
print(average_units)

# Q5: Create pivot table - Products vs Regions
pivot = df.pivot_table(
    values='Revenue',
    index='Product',
    columns='Region',
    aggfunc='sum',
    fill_value=0
)

print("\n5. Pivot: Products vs Regions (Revenue):")
print(pivot)

# Step 3: Advanced - Merge with product info
product_info = pd.DataFrame({
    'Product' : ['Laptop','Phone','Tablet','Monitor','Keyboard'],
    'Category': ['Computer','Mobile','Mobile','Computer','Accessory'],
    'Cost': [800,400,300,200,30]
})

# Merge sales with product info
df_merged = pd.merge(df,product_info,on="Product",how='left')
df_merged['Profit'] = df_merged['Revenue'] - (df_merged['Units'] * df_merged['Cost'])

print("\n Sample data with profit")
print(df_merged[['Product','Units','Revenue','Cost','Profit']].head())

# Q6: Which product is most profitable?
profit_by_products = df_merged.groupby('Product')['Profit'].sum().sort_values(ascending=False)
print("\n7. Profit by Product:")
print(profit_by_products)

# Q8: What's the most expensive single transaction?
most_expensive = df['Revenue'].max()
most_expensive_row = df[df["Revenue"] == most_expensive]

print(f"\n8. Expensive transasction: ${most_expensive}")
print(most_expensive_row[["Product","Units","Price","Revenue"]].head(1))

# Q8: What's the most expensive single transaction?
#Alternative
max_idx = df['Revenue'].idxmax()
most_expensive_row = df.loc[max_idx]

print("\n8. Most Expensive Transaction:")
print(f"   Product: {most_expensive_row['Product']}")
print(f"   Units: {most_expensive_row['Units']}")
print(f"   Price: ${most_expensive_row['Price']}")
print(f"   Revenue: ${most_expensive_row['Revenue']:,}")

# Q9: Average revenue per transaction by region
avg_revenue = df.groupby('Region')["Revenue"].mean().sort_values(ascending=False)
for region, avg in avg_revenue.items():
    print(f"   {region}: ${avg:,.2f}")

# Q10: How many unique products were sold in each region?
unique_products = df.groupby('Region')['Product'].nunique()
print("\n Unique Products")
for region, count in unique_products.items():
    print(f"   {region}: {count} products")
    
# BONUS: Which product-region combination has the highest total revenue?
highest_total_revenue = df.groupby(['Product','Region'])['Revenue'].sum().sort_values(ascending=False)
print("\nBONUS: Top 5 Product-Region Combinations:")
print(highest_total_revenue.head())

# Step 4: Save results
df.to_csv('python-practice/sales_data.csv',index=False)
pivot.to_csv('python-practice/sales_pivot.csv')
print("\n✅ Files saved: sales_data.csv, sales_pivot.csv")


