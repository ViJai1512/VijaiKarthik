import json
# Open and load JSON file
with open("products.json", "r") as file:
    products = json.load(file)
# Print all product names
print("Available Products:")
for p in products:
    print(f"- {p['name']} ({p['category']})")
    
# Calculate total inventory value (price x stock)
print("\nInventory:")
total_value = sum(p["price"] * p["stock"] for p in products)
print(f"\nTotal Inventory Value: {total_value}")

# Find out-of-stock products (if any)
out_of_stock = [p["name"] for p in products if p["stock"] == 0]
if out_of_stock:
    print("Out of stock",", ".join(out_of_stock))
else:
    print("All products are in stock.")