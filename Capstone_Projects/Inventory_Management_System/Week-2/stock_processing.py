import pandas as pd
import numpy as np

# 1. Load Stock Movement Data
df = pd.read_csv("stock_movements.csv")

# 2. Clean and Transform Data
df['quantity'] = df['quantity'].astype(int)
df['quantity'] = np.where(df['movement_type'] == 'OUT', -df['quantity'], df['quantity'])

# 3. Calculate Current Stock
stock_summary = df.groupby(['product_id', 'product_name'])['quantity'].sum().reset_index()
stock_summary.rename(columns={'quantity': 'current_stock'}, inplace=True)

# 4. Load Product Master
products = pd.read_csv("products.csv")
stock_status = pd.merge(products, stock_summary, on=['product_id', 'product_name'], how='left')
stock_status['current_stock'] = stock_status['current_stock'].fillna(0).astype(int)

# 5. Flag Low Stock Items
stock_status['low_stock_flag'] = np.where(stock_status['current_stock'] < stock_status['reorder_level'], "YES", "NO")

# 6. Save Report
stock_status.to_csv("stock_report.csv", index=False)
print(stock_status)
print(stock_status[stock_status['low_stock_flag'] == "YES"])
