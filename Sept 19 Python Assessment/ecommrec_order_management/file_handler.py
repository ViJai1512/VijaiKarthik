import csv
import json
from models import Product, Order

def load_products(filename="products.csv"):
    products = {}
    try:
        with open("products.csv", 'r', newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                product = Product(**row)
                products[product.id] = product
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
    return products

def save_products(products, filename="products.csv"):
    with open("products.csv", 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['id', 'name', 'category', 'price', 'stock'])
        for product in products.values():
            writer.writerow([product.id, product.name, product.category, product.price, product.stock])

def load_orders(filename="orders.json"):
    try:
        with open("orders.json", 'r') as f:
            orders_data = json.load(f)
        return [Order(**data) for data in orders_data]
    except (FileNotFoundError, json.JSONDecodeError):
        print(f"Error reading or parsing {filename}.")
        return []

def save_orders(orders, filename="orders.json"):
    orders_data = [
        {"order_id": o.order_id, "customer": o.customer, "items": o.items}
        for o in orders
    ]
    with open("orders.json", 'w') as f:
        json.dump(orders_data, f, indent=2)