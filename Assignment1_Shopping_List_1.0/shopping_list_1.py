"""
CP1404 Assignment 1 - Shopping List 1.0
Written by Callum Robertson, 7/09/2016

This program read items from a .csv file and adds them to a shopping list. The user is able to add to this list, change
items in the list, and view the required or completed items. Once the user chooses to exit the program will rewrite the
new shopping list to the same .csv file.

Link to GitHub repository:
https://github.com/callumr1/Programming_1_Pracs/tree/master/Assignment%201%20-%20Shopping%20List%201.0
"""


def main():
    users_name = "Callum"
    print("Greetings {} and Welcome to your Shopping List!\n".format(users_name))

    menu = "1 - View Required items\n2 - View Completed items\n3 - Add an item\n4 - Change an item from Required to Completed\n5 - Exit your shopping list"

    print("What would you like to do? Enter 1 through to 5 from the menu options below:")
    print(menu)
    menu_condition = str(input(">>>"))
    # Items list
    items = []
    load_items(items)

    while menu_condition != "6":
        if menu_condition == "1":
            print("\nThe Required Items on your Shopping List are:")
            item_needed = "r"
            # Looks for the required items as item_needed = "r"
            refine_items(items, item_needed)
            menu_condition = print_menu(menu, menu_condition)

        elif menu_condition == "2":
            print("\nThe Completed Items on your Shopping List are:")
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
            print("\nWhat item would you like to change to completed?")
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

    # Get all the information for the new item
    new_item_name = str(input("\nEnter a new item: "))
    new_item_price = str(input("Enter the cost of the new item: "))
    item_importance = str(input("Enter the importance of the item on a scale of 1-3: "))
    print("\nAdded {} - ${} to your shopping list.".format(new_item_name, new_item_price))

    # Add the new item to the items list
    new_item.append(new_item_name)
    new_item.append(new_item_price)
    new_item.append(item_importance)
    new_item.append("r")
    items.append(new_item)


def refine_items(items, item_needed):
    # Searches for either the required items or the completed ones depending on what item_needed is
    total_cost = 0.0
    longest_name = max(len(item) for item in items)
    sorted_items = sorted(items, key=lambda item: item[2])
    for item in sorted_items:
        if item_needed in item:

            print('{:20} $ {:6.2f} {:>3}{}{}'.format(str(item[0]), float(item[1]), "(", int(item[2]), ")"))
            total_cost += float(item[1])
    print("{:20} $ {:6.2f}".format("The total cost is:", total_cost))
    # if item_needed in line_str:
    # item = line_str
    # print(item[:-1])


"""
Pseudocode for complete an item:
for every item in items:
    if itemName in item:
        new_item_list = item - "r"
        add "c" to new_item_list
        remove item from items
print " the item was changed to completed"
add new_item_list to items
"""


def change_item(items, item_name):
    # Changes an item from required to completed
    global new_line_str
    for item in items:
        if item_name in item:
            new_line_str = item[:-1]
            new_line_str.append("c")
            items.remove(item)
            print("{} was change to completed".format(item_name))
            items.append(new_line_str)


"""
Pseudocode for load items:
open items.csv
for every line in list_file
    new_line = line stripped and split(",")
    add new_line to items
close items.csv

"""


def load_items(items):
    # Loads all the items from items.csv at the beginning of the program
    list_file = open("items.csv", "r")
    for line in list_file:
        new_line = line.strip().split(",")
        items.append(new_line)
    list_file.close()


if __name__ == "__main__":

    main()
