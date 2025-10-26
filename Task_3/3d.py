import pandas as pd
import numpy as np
# Create sample sales data
data = pd.DataFrame({
    'Product': ['Laptop', 'Headphones', 'Mouse', 'Keyboard'] * 5,
    'Units_Sold': np.random.randint(5, 50, 20),
    'Price_per_Unit': np.random.randint(1000, 5000, 20)
})
# Calculate total sales for each row
data['Total_Sales'] = data['Units_Sold'] * data['Price_per_Unit']
# Find top-selling product
top_product = data.groupby('Product')['Total_Sales'].sum().idxmax()
# Calculate total sales
total_sales = data['Total_Sales'].sum()
# Show results
print("Top Selling Product:", top_product)
print("Total Sales: ₹", total_sales)
print("\nSample Data:\n", data)
