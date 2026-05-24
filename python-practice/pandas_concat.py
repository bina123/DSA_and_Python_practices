import pandas as pd

df1 = pd.DataFrame({
    'ID' : [1,2,3],
    'Name': ['Alice','Bob','Charlie']
})

df2 = pd.DataFrame({
    'ID': [4,5,6],
    'Name' : ['David','Eve','Frank']
})

vertical = pd.concat([df1,df2],ignore_index=True)
print(vertical)

df3 = pd.DataFrame({
    'Age': [25,30,35],
    'City': ['NYC','LA','Chicago']
})

horizontal = pd.concat([df1,df3],axis=1)
print("\n Horozonatl Data ")
print(horizontal)

Sales = pd.DataFrame({
    'Date': ['2024-01','2024-01','2024-02','2024-02'],
    'Product': ['A','B','A','B'],
    'Region': ['North','North','South','South'],
    'Sales': [100,150,200,250]
})

print("\n Orginal data:")
print(Sales)

# Pivot: Products as columns, Dates as rows
pivot = Sales.pivot_table(
    values='Sales',
    index='Date',
    columns='Product',
    aggfunc='sum'
)

print("\nPIVOT TABLE:")
print(pivot)


