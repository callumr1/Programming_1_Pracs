"""
CP1404 Assignment 1 - Shopping List 1.0
Written by Callum Robertson
"""


def main():
    users_name = "Callum"
    print("Greetings {} and welcome to your shopping list!\n".format(users_name))

    menu = "1 - View Required items\n2 - View Completed items\n3 - Add an item\n4 - Change an item from Required to Completed\n5 - Exit your shopping list"

    print("What would you like to do? Enter either 1, 2, 3 or 4 from the menu options below:")
    print(menu)
    menu_condition = str(input(">>>"))
    # Items list
    items = []
    load_items(items)

    while menu_condition != "6":
        if menu_condition == "1":
            print("The Required Items on your shopping list are:")
            item_needed = "r"
            # Looks for the required items as item_needed = "r"
            refine_items(items, item_needed)
            menu_condition = print_menu(menu, menu_condition)

        elif menu_condition == "2":
            print("The Completed Items on your Shopping List are:")
            item_needed = "c"
            # Looks for the completed items as item_needed = "r"
            refine_items(items, item_needed)
            menu_condition = print_menu(menu, menu_condition)

        elif menu_condition == "3":
            # Runs the add_item function
            add_item(items)
            menu_condition = print_menu(menu, menu_condition)

        elif menu_condition == "4":
            # Asks the user for the name of the item they want to change and sends it to the change_item function
            print("What item would you like to change to completed?")
            item_name = str(input(">>> "))
            change_item(items, item_name)
            menu_condition = print_menu(menu, menu_condition)

        elif menu_condition == "5":
            save_items(items)
            print("Your Shopping List has been updated. \nHave a nice day {}!".format(users_name))
            # Exits the program
            menu_condition = "6"

        else:
            print("Please select from one of the 5 menu options: ")
            menu_condition = print_menu(menu, menu_condition)


def save_items(items):
    # Rewrites all the items in the items list to the items.csv file
    list_file = open("items.csv", "w")
    for item in items:
        item_str = ",".join(item)
        list_file.write(item_str + "\n")
    list_file.close()


def print_menu(menu, menu_condition):
    # Function that prints the menu
    print("\n")
    print(menu)
    menu_condition = str(input(">>>"))
    return menu_condition


def add_item(items):
    # Function for adding a new item
    new_item = []

    print("Add an item")

    # Get all the information for the new item
    new_item_name = str(input("Enter a new item: "))
    new_item_price = str(input("Enter the cost of the new item: "))
    item_importance = str(input("Enter the importance of the item on a scale of 1-3: "))
    print("Added {} - ${} to your shopping list.".format(new_item_name, new_item_price))

    # Add the new item to the items list
    new_item.append(new_item_name)
    new_item.append(new_item_price)
    new_item.append(item_importance)
    new_item.append("r")
    items.append(new_item)

    print("Your new shopping list looks like this:")
    for item in items:
        print(item)


def refine_items(items, item_needed):
    # Searches for either the required items or the completed ones depending on what item_needed is
    line_str = items
    if item_needed in line_str:
        print(line_str)
    for line_str in items:
        if item_needed in line_str:
            print(line_str)


def change_item(items, item_name):
    # Changes an item from required to completed
    global new_line_str
    for item in items:
        if item_name in item:
            new_line_str = item[:-1]
            new_line_str.append("c")
            items.remove(item)
    print("{} was change to completed \n".format(item_name))
    items.append(new_line_str)
    print("Your new shopping list looks like this:")
    for item in items:
        print(item)


def load_items(items):
    # Loads all the items from items.csv at the beginning of the program
    list_file = open("items.csv", "r")
    for line in list_file:
        new_line = line.strip().split(",")
        items.append(new_line)
    list_file.close()


main()
