import pandas as pd
import numpy as np

# Load Data from CSV
sales = pd.read_csv("sales.csv")
inventory = pd.read_csv("inventory.csv")

# Data Cleaning
sales['quantity'] = sales['quantity'].fillna(0)

# Convert sale_date to datetime
sales['sale_date'] = pd.to_datetime(sales['sale_date'], errors='coerce')

# Drop rows with invalid dates
sales = sales.dropna(subset=['sale_date'])

# Monthly Sales Calculation
sales['month'] = sales['sale_date'].dt.to_period('M')

monthly_sales = sales.groupby(['product_id', 'month'])['quantity'].sum().reset_index()
monthly_sales.rename(columns={'quantity': 'total_units_sold'}, inplace=True)

print("✅ Monthly Sales Summary:")
print(monthly_sales)
# Inventory Turnover using NumPy
inventory['avg_stock'] = np.mean([inventory['opening_stock'], inventory['closing_stock']], axis=0)

# Merge sales with inventory
df = pd.merge(monthly_sales, inventory, on=['product_id','month'], how='left')

df['inventory_turnover'] = df['total_units_sold'] / df['avg_stock']

print("\n✅ Inventory Turnover Report:")
print(df[['product_id', 'month', 'total_units_sold', 'avg_stock', 'inventory_turnover']])

# Top Selling Products
top_sellers = monthly_sales.sort_values(by='total_units_sold', ascending=False).head(5)
print("\n🏆 Top Selling Products:")
print(top_sellers)

# Underperforming Products
underperforming = monthly_sales[monthly_sales['total_units_sold'] < np.mean(monthly_sales['total_units_sold'])]
print("\n⚠️ Underperforming Products:")
print(underperforming)

# Save Output Files
monthly_sales.to_csv("processed_monthly_sales.csv", index=False)
df.to_csv("inventory_turnover_report.csv", index=False)
