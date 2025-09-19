from collections import defaultdict
from models import Order
from file_handler import load_products, save_products, load_orders, save_orders
from reports import generate_sales_report, generate_inventory_report

def view_products(products):
    print("\n--- 🛍️ Available Products ---")
    for product in products.values():
        print(product)
    if products:
        most_expensive = max(products.values(), key=lambda p: p.price)
        print(f"\nMost Expensive Product: {most_expensive.name} (₹{most_expensive.price:,.2f})")

def view_orders(orders, products):
    print("\n--- 📜 All Orders ---")
    if not orders:
        print("No orders have been placed yet.")
        return
        
    product_demand = defaultdict(int)
    for order in orders:
        total = order.get_total(products)
        print(f"Order ID: {order.order_id}, Customer: {order.customer}, Total Bill: ₹{total:,.2f}")
        for item in order.items:
            product_demand[item['product_id']] += item['qty']
    
    if product_demand:
        most_ordered_id = max(product_demand, key=product_demand.get)
        most_ordered_product = products.get(most_ordered_id)
        if most_ordered_product:
            print(f"\nMost Ordered Product: {most_ordered_product.name} (Total Qty: {product_demand[most_ordered_id]})")

def place_new_order(orders, products):
    print("\n--- 🛒 Place a New Order ---")
    customer_name = input("Enter your name: ")
    new_items = []
    
    while True:
        try:
            product_id = int(input("Enter Product ID to add (or 0 to finish): "))
            if product_id == 0:
                break
            product = products.get(product_id)
            if not product:
                print("Invalid Product ID. Please try again.")
                continue
            
            qty = int(input(f"Enter quantity for {product.name}: "))
            if qty <= 0:
                print("Quantity must be positive.")
                continue
            if product.stock < qty:
                print(f"Not enough stock for {product.name}. Available: {product.stock}")
                continue

            new_items.append({"product_id": product_id, "qty": qty})
            print(f"Added {qty} of {product.name} to your order.")
            
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    if new_items:
        for item in new_items:
            products[item['product_id']].update_stock(item['qty'])

        new_order_id = max([o.order_id for o in orders]) + 1 if orders else 101
        new_order = Order(new_order_id, customer_name, new_items)
        orders.append(new_order)
        save_orders(orders)
        save_products(products)
        print("\nOrder placed successfully! Your Order ID is:", new_order_id)
    else:
        print("\nOrder cancelled. No items were added.")

def main():
    products = load_products()
    orders = load_orders()
    
    while True:
        print("\n=====  E-Commerce Order Management System =====")
        print("1. View Products")
        print("2. Place a New Order")
        print("3. View All Orders")
        print("4. Generate Reports")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            view_products(products)
        elif choice == '2':
            place_new_order(orders, products)
        elif choice == '3':
            view_orders(orders, products)
        elif choice == '4':
            generate_sales_report(orders, products)
            generate_inventory_report(products)
        elif choice == '5':
            print("Exiting the system. Thank you!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()