from order import Order
from product import Product
from customer import Customer

# Get customer details from the user
customer_name = input("Enter customer name: ")
customer_address = input("Enter customer address: ")
customer_phone = input("Enter customer phone number: ")

customer = Customer(customer_name, customer_address, customer_phone)

# Create an order for the customer
order = Order(customer)

# Option to add multiple products
while True:
    product_name = input("Enter product name: ")
    product_price = float(input("Enter product price: "))
    product_quantity = int(input("Enter product quantity: "))
    
    product = Product(product_name, product_price, product_quantity)
    order.add_product(product)
    
    add_more = input("Do you want to add another product? (yes/no): ").lower()
    if add_more != "yes":
        break

# Calculate and display the total
total = order.calculate_total()
print(f"Order Total: Rs{total}")

# Generate and display the summary
print(order.generate_summary())