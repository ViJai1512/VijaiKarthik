import pandas as pd
import numpy as np

# 1. Load Sales & Product Data

sales_df = pd.read_csv("sales.csv")
products_df = pd.read_csv("products.csv")

print("✅ Sales Data Loaded")
print(sales_df.head())
print("\n✅ Products Data Loaded")
print(products_df.head())


# 2. Clean Data

# Handle missing values
sales_df['quantity'] = sales_df['quantity'].fillna(0).astype(int)
sales_df['price'] = sales_df['price'].fillna(sales_df['price'].mean())

# Convert date column
sales_df['sale_date'] = pd.to_datetime(sales_df['sale_date'], errors='coerce')

# Drop rows with invalid dates
sales_df = sales_df.dropna(subset=['sale_date'])

print("\n✅ Cleaned Sales Data:")
print(sales_df.info())

# 3. Add Calculated Fields

# Revenue = quantity * price
sales_df['revenue'] = sales_df['quantity'] * sales_df['price']

# Add discount column if not present
if 'discount' not in sales_df.columns:
    sales_df['discount'] = 0  

# Discount percentage
sales_df['discount_percentage'] = (sales_df['discount'] / 
                                   (sales_df['price'] * sales_df['quantity']).replace(0, np.nan)) * 100
sales_df['discount_percentage'] = sales_df['discount_percentage'].fillna(0)

sales_df['cost'] = sales_df['price'] * 0.7
sales_df['profit'] = sales_df['revenue'] - (sales_df['cost'] * sales_df['quantity'])

print("\n✅ With Calculated Fields:")
print(sales_df[['sale_id', 'revenue', 'discount_percentage', 'profit']].head())


# 4. Summarize Revenue by Product & Store

# Merge with products for product names
merged_df = pd.merge(sales_df, products_df, on="product_id", how="left")

# Revenue by product
revenue_by_product = merged_df.groupby("product_name")['revenue'].sum()
print("\n✅ Revenue by Product:")
print(revenue_by_product)

# Revenue by store
revenue_by_store = merged_df.groupby("store_id")['revenue'].sum()
print("\n✅ Revenue by Store:")
print(revenue_by_store)

# 5. Save Outputs

sales_df.to_csv("sales_cleaned.csv", index=False)
summary = merged_df.groupby("store_id")[['revenue', 'profit']].sum()
summary.to_csv("store_summary.csv")

print("\n Week 2 Processing Complete!")
print("sales_cleaned.csv and store_summary.csv have been saved.")
