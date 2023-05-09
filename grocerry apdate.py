# Define the items and prices in the grocery shop
grocery_shop = {
    "apple": {"price": 40, "quantity": 50},
    "banana": {"price": 30, "quantity": 40},
    "cherry": {"price": 70, "quantity": 80}
}

# Initialize the user's shopping cart
shopping_cart = {
    "apple": 0,
    "banana": 0,
    "cherry": 0
}

# Define the admin password
admin_password = "000"

# Prompt the user for their role (admin or customer)
user_role = input("Enter your role (admin or customer): ")

if user_role == "admin":
    # Prompt the admin for their password
    password = input("Enter your password: ")
    if password == admin_password:
        # If the password is correct, allow the admin to change the quantity and price of an item
        item = input("Enter the name of the item you want to change: ")
        if item in grocery_shop:
            action = input("Enter the action you want to perform (change quantity or change price): ")
            if action == "change quantity":
                quantity = int(input("Enter the new quantity: "))
                grocery_shop[item]["quantity"] = quantity
            elif action == "change price":
                price = int(input("Enter the new price: "))
                grocery_shop[item]["price"] = price
            else:
                print("Invalid action.")
        else:
            print("Invalid item.")
    else:
        print("Invalid password.")
elif user_role == "customer":
    # Loop until the customer is done shopping
    done_shopping = False
    while not done_shopping:
        # Display the available items and their prices
        print("Available items:")
        for item, details in grocery_shop.items():
            print(f"{item}: {details['price']}")
        # Prompt the user to select an item and a quantity
        item = input("Enter the name of the item you want to buy (press 'q' to check out): ")
        if item == "q":
            # If the customer is done shopping, exit the loop
            done_shopping = True
        elif item in grocery_shop:
            # If the item is available, prompt for the quantity
            quantity = int(input("Enter the quantity you want to buy: "))
            # Check if the desired quantity is available in the inventory
            if quantity <= grocery_shop[item]["quantity"]:
                # Add the item and quantity to the shopping cart
                shopping_cart[item] += quantity
                # Subtract the quantity from the inventory
                grocery_shop[item]["quantity"] -= quantity
            else:
                # If the desired quantity is not available, print an error message
                print(f"Sorry, only {grocery_shop[item]['quantity']} {item}s are available.")
        else:
            # If the item is not available, print an error message
            print("Sorry, that item is not available.")

    # Calculate the total cost of the items in the shopping cart
    total_cost = 0
    for item, quantity in shopping_cart.items():
        total_cost += quantity * grocery_shop[item]["price"]

    # Display the final shopping cart and total cost
    print("Your shopping cart:")
    for item, quantity in shopping_cart.items():
        print(f"{item}: {quantity}")
    print(f"Total cost: {total_cost}")
else:
    print("Invalid role.")