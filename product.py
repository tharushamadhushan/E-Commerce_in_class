class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_details(self):
        return f"Product Name: {self.name}, Price: ${self.price:.2f}, Quantity: {self.quantity}"

    def update_price(self, new_price):
        self.price = new_price
        print(f"Price of {self.name} has been updated to ${self.price:.2f}")

    def update_quantity(self, new_quantity):
        self.quantity = new_quantity
        print(f"Quantity of {self.name} has been updated to {self.quantity}")

