"""
CP1404 Assignment 1 - Shopping List 1.0
Written by Callum Robertson
"""


def main():
    list_file = open("items.csv", "r")
    users_name = "Callum"
    print("Greetings {} and welcome to your shopping list!\n".format(users_name))

    menu = "1 - View Required items\n2 - View Completed items\n3 - Add an item\n4 - Change an item from Required to Completed\n5 - Exit your shopping list"
    print("What would you like to do? Enter either 1, 2, 3 or 4 from the menu options below:")
    print(menu)
    menu_condition = str(input(">>>"))

    while menu_condition != "5":
        if menu_condition == "1":
            item_needed = ",r"
            print("The Required Items on your Shopping list are:")
            refine_items(list_file, item_needed)
            print(menu)
            menu_condition = str(input(">>>"))

        elif menu_condition == "2":
            print("The Completed Items on your Shopping List are:")
            item_needed = ",c"
            refine_items(list_file, item_needed)
            print(menu)
            menu_condition = str(input(">>>"))

        elif menu_condition == "3":
            print("Add an item")
            new_item = str(input("Enter a new item: "))
            new_item_price = float(input("Enter the cost of the new item: "))
            item_importance = int(input("Enter the importance of the item on a scale of 1-3: "))
            print("{},{},{},r".format(new_item, new_item_price, item_importance))
            print(menu)
            menu_condition = str(input(">>>"))

        elif menu_condition == "4":
            print("Change an item from required to completed")

        else:
            print("Please select from one of the 5 menu options: ")
            print(menu)
            menu_condition = str(input(">>>"))


def refine_items(list_file, item_needed):
    line_str = list_file.readline()
    if item_needed in line_str:
        print(line_str)
    for line_str in list_file:
        if item_needed in line_str:
            print(line_str)


main()
