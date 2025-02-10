import pandas as pd
data = {
    'item': ['Tablet', 'Monitor', 'Tablet', 'PC', 'Monitor'], 
    'units_sold': [15, 8, None, 10, 6], 
    'total_sales': [200, None, 50, 120, 80]  
}
df = pd.DataFrame(data)
print("Original DataFrame:\n")
print(df)
NumericColumns = df.select_dtypes(include=['int64', 'float64']).columns  
df[NumericColumns] = df[NumericColumns].fillna(df[NumericColumns].mean())  
print("\nDataFrame after filling missing values with column-wise means:\n")
print(df)
