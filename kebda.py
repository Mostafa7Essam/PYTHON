# Define the correct password
password = "202156"

# Define the initial menu with prices
menu = {
    "kebda feno": 10,
    "kebda balady": 10,
    "kebda fransawy": 15,
    "sgo2 feno": 15,
    "sgo2 balady": 15,
    "sgo2 fransawy": 20,
}

# Ask the user if they are a customer or owner
mode = input('''Are you a customer or an owner?
              Customer: Enter '1'
              Owner: Enter '2'
              Quit: Enter 'q' ''')

# Loop until the user wants to quit
while mode != "q":
    # If the user is an owner, prompt for password and allow them to update the menu
    if mode == "2":
        # Prompt for password
        verification = input("Please enter password: ")
        # If password is correct, allow owner to update menu
        if verification == password:
            # Prompt for action: add new item or update existing item
            action = input("Would you like to add a new item or update an existing item? Enter 'add' or 'update': ")
            # If adding a new item, prompt for name and price and add to menu
            if action == "add":
                new_product = input("Enter the name of the new item: ")
                price = float(input("Enter the price of the new item: "))
                # Add the new item to the menu
                menu[new_product] = price
                print(f"{new_product} added to menu with price {price}.")
            # If updating an existing item, prompt for name and check if it exists in menu
            elif action == "update":
                new_product = input("Enter the name of the item you want to change the price of: ")
                if new_product in menu:
                    # Prompt for new price and update menu
                    price = float(input("Enter the new price of the item: "))
                    menu[new_product] = price
                    print(f"Price of {new_product} updated successfully!")
                else:
                    # If item not found in menu, print error message
                    print(f"{new_product} not found in menu.")
            else:
                # If user enters invalid action, print error message
                print("Invalid input. Please enter 'add' or 'update'.")
        # If password is incorrect, print error message
        else:
            print("Wrong password. Please try again.")
    # If the user is a customer, display the menu and ask for the customer's order
    elif mode == "1":
        # Initialize the order list and total price
        order_list = []
        total_price = 0
        # Display the menu
        print("Menu:")
        for item, price in menu.items():
            print(f"{item}: {price}")
        # Prompt for the customer's order
        order = input("What would you like to order? Enter the item name (press 'q' to exit): ")
        # Loop until the customer is done ordering
        while order != "q":
            # Check if the order is valid
            if order in menu:
                # Prompt for the quantity of the item and add it to the order list
                quantity = int(input("How many would you like to order? "))
                for i in range(quantity):
                    order_list.append(order)
                    total_price += menu[order]
                print(f"{quantity} {order} added to your order. Your total is {total_price}.")
            else:
                # If the order is not valid, print error message
                print("Invalid order. Please enter a valid item name.")
            # Prompt for the next order or to exit
            order = input("Enter another item or press 'q' to exit: ")
        # Print the final order confirmation
        if len(order_list) > 0:
            print("Your order is:")
            for item in order_list:
                print(f"- {item}: {menu[item]}")
            print(f"Your total is {total_price}.")
        else:
            print("No items ordered.")
    # If the user enters an invalid option, print error message
    else:
        print("Invalid input. Please enter '1', '2', or 'q'.")
    
    # Prompt the user again for their role
    mode = input('''Are you a customer or an owner?
              Customer: Enter '1'
              Owner: Enter '2'
              Quit: Enter 'q' ''')