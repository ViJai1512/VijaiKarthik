from collections import defaultdict

def generate_sales_report(orders, products):
    print("\n--- 📊 Sales Report ---")
    if not orders:
        print("No order data to generate a report.")
        return

    total_revenue = sum(order.get_total(products) for order in orders)
    print(f"Total Revenue: ₹{total_revenue:,.2f}")

    revenue_by_category = defaultdict(float)
    customer_spending = defaultdict(float)

    for order in orders:
        order_total = order.get_total(products)
        customer_spending[order.customer] += order_total
        for item in order.items:
            product = products.get(item['product_id'])
            if product:
                revenue_by_category[product.category] += product.price * item['qty']

    print("\nRevenue by Category:")
    for category, revenue in revenue_by_category.items():
        print(f"  - {category}: ₹{revenue:,.2f}")

    if customer_spending:
        top_customer = max(customer_spending, key=customer_spending.get)
        print(f"\nTop Spending Customer: {top_customer} (₹{customer_spending[top_customer]:,.2f})")
    print("-" * 25)

def generate_inventory_report(products):
    print("\n--- 📦 Inventory Report ---")
    if not products:
        print("No product data available.")
        return

    print("Low Stock Alert (less than 5 items):")
    low_stock_products = [p for p in products.values() if p.stock < 5]
    if low_stock_products:
        for product in low_stock_products:
            print(f"  - {product.name} (Stock: {product.stock})")
    else:
        print("  - None")

    category_prices = defaultdict(list)
    for product in products.values():
        category_prices[product.category].append(product.price)

    print("\nAverage Price by Category:")
    for category, prices in category_prices.items():
        avg_price = sum(prices) / len(prices)
        print(f"  - {category}: ₹{avg_price:,.2f}")
    print("-" * 25)