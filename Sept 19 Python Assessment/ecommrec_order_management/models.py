class Product:
    def __init__(self, id, name, category, price, stock):
        self.id = int(id)
        self.name = name
        self.category = category
        self.price = float(price)
        self.stock = int(stock)

    def update_stock(self, qty):
        if self.stock >= qty:
            self.stock -= qty
            return True
        return False

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Category: {self.category}, Price: ₹{self.price:,.2f}, Stock: {self.stock}"

class Order:
    def __init__(self, order_id, customer, items):
        self.order_id = order_id
        self.customer = customer
        self.items = items

    def get_total(self, products_map):
        total = 0
        for item in self.items:
            product = products_map.get(item['product_id'])
            if product:
                total += product.price * item['qty']
        return total