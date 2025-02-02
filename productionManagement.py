from product import Product

# Get initial input from the user
product_name = input("Enter product name: ")
product_price = float(input("Enter product price: "))
product_quantity = int(input("Enter product quantity: "))

# Create a Product object
product = Product(product_name, product_price, product_quantity)

# Menu for user interaction
while True:
    print("\nOptions:")
    print("1. Get Product Details")
    print("2. Update Product Price")
    print("3. Update Product Quantity")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        print("\n" + product.get_details())
    elif choice == "2":
        new_price = float(input("Enter the new price: "))
        product.update_price(new_price)
    elif choice == "3":
        new_quantity = int(input("Enter the new quantity: "))
        product.update_quantity(new_quantity)
    elif choice == "4":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
