# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": 0.99,
        "Banana": 0.69,
        "Apple": 0.49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# Initialize the order list
order = []

# Launch the store and present a greeting to the customer
print("Welcome to the variety food truck.")

# Customers may want to order multiple items, so let's create a continuous loop
place_order = True
while place_order:
    # Ask the customer from which menu category they want to order
    print("From which menu would you like to order? ")

    # Create a variable for the menu item number and a dictionary to store the menu for later retrieval
    i = 1
    menu_items = {}
    for key in menu.keys():
        print(f"{i}: {key}")
        menu_items[i] = key
        i += 1

    # Get the customer's input
    menu_category = input("Type menu number: ")

    # Check if the customer's input is a number and a valid option
    if menu_category.isdigit() and int(menu_category) in menu_items.keys():
        menu_category_name = menu_items[int(menu_category)]
        print(f"You selected {menu_category_name}")

        # Print out the menu options from the menu_category_name
        print(f"What {menu_category_name} item would you like to order?")
        i = 1
        menu_items = {}
        print("Item # | Item name                | Price")
        print("-------|--------------------------|-------")
        for key, value in menu[menu_category_name].items():
            # Handle items with sub-options
            if isinstance(value, dict):
                for key2, value2 in value.items():
                    num_item_spaces = 24 - len(key + key2) - 3
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                    menu_items[i] = {"Item name": key + " - " + key2, "Price": value2}
                    i += 1
            else:
                num_item_spaces = 24 - len(key)
                item_spaces = " " * num_item_spaces
                print(f"{i}      | {key}{item_spaces} | ${value}")
                menu_items[i] = {"Item name": key, "Price": value}
                i += 1

        # Ask customer to input menu item number and validate
        menu_selection = input("Please enter the number of your choice: ")
        if menu_selection.isdigit() and int(menu_selection) in menu_items.keys():
            menu_selection = int(menu_selection)
            selected_item = menu_items[menu_selection]["Item name"]
            price = menu_items[menu_selection]["Price"]
            quantity = input(f"How many of '{selected_item}' would you like? (default 1): ")
            try:
                quantity = int(quantity)
            except ValueError:
                quantity = 1
            order.append({"Item name": selected_item, "Price": price, "Quantity": quantity})
        else:
            print("Invalid selection or not a number. Please try again.")

        # Ask the customer if they would like to order anything else
        while True:
            keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o: ").lower()
            if keep_ordering == 'y':
                break
            elif keep_ordering == 'n':
                place_order = False
                print("Thank you for your order")
                break
            else:
                print("Please enter 'Y' for Yes or 'N' for No.")
    else:
        print("Invalid input. Please enter a number corresponding to the menu options.")

# Print out the customer's order
print("This is what we are preparing for you.\n")
print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")
total_price = 0
for item in order:
    item_name = item["Item name"]
    price = item["Price"]
    quantity = item["Quantity"]
    num_item_spaces = 24 - len(item_name)
    item_spaces = " " * num_item_spaces
    print(f"{item_name}{item_spaces} | ${price:.2f} | {quantity}")
    total_price += price * quantity

print(f"\nTotal price of the order: ${total_price:.2f}")

