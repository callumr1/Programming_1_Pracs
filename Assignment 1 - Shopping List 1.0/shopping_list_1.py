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

    while menu_condition != "5":
        if menu_condition == "1":
            print("The Required Items on your shopping list are:")
            item_needed = "r"
            refine_items(items, item_needed)
            print("\n")
            print(menu)
            menu_condition = str(input(">>>"))

        elif menu_condition == "2":
            print("The Completed Items on your Shopping List are:")
            item_needed = "c"
            refine_items(items, item_needed)
            print(menu)
            menu_condition = str(input(">>>"))

        elif menu_condition == "3":
            new_item = []
            print("Add an item")
            new_item_name = str(input("Enter a new item: "))
            new_item_price = float(input("Enter the cost of the new item: "))
            item_importance = int(input("Enter the importance of the item on a scale of 1-3: "))
            print("Added {} - ${} to your shopping list.".format(new_item_name, new_item_price))
            new_item.append(new_item_name)
            new_item.append(new_item_price)
            new_item.append(item_importance)
            new_item.append("r")
            items.append(new_item)
            print(items)
            print(menu)
            menu_condition = str(input(">>>"))

        elif menu_condition == "4":
            print("Change an item from required to completed")
            print("What item would you like to change?")
            item_name = str(input(">>> "))
            change_item(items, item_name)
            print(items)
            print(menu)
            menu_condition = str(input(">>>"))

        elif menu_condition == "5":
            list_file = open("items.csv", "w")
            for item in items:
                print(item, file=list_file)

        else:
            print("Please select from one of the 5 menu options: ")
            print(menu)
            menu_condition = str(input(">>>"))


def refine_items(items, item_needed):
    line_str = items
    if item_needed in line_str:
        print(line_str)
    for line_str in items:
        if item_needed in line_str:
            print(line_str)


def change_item(items, item_name):
    global new_line_str
    for item in items:
        if item_name in item:
            new_line_str = item[:-1]
            new_line_str.append("c")
            print(new_line_str)
            items.remove(item)
    items.append(new_line_str)


def load_items(items):
    list_file = open("items.csv", "r")
    for line in list_file:
        new_line = line.strip().split(",")
        items.append(new_line)
    list_file.close()


main()
