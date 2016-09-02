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

    while menu_condition != "5":
        if menu_condition == "1":
            list_file = open("items.csv", "r")
            print(list_file.readline())
            print("Required items and total price")
            print(menu)
            menu_condition = str(input(">>>"))
        elif menu_condition == "2":
            print("Completed items and total cost")
            print(menu)
            menu_condition = str(input(">>>"))
        elif menu_condition == "3":
            print("Add an item")
            list_file = open("items.csv", "a")
            new_item = str(input("Enter a new item: "))
            new_item_price = float(input("Enter the cost of the new item: "))
            item_importance = int(input("Enter the importance of the item on a scale of 1-3: "))
            print("{},{},{}".format(new_item, new_item_price, item_importance))
            list_file.close()
            print(menu)
            menu_condition = str(input(">>>"))
        elif menu_condition == "4":
            print("Change an item from required to completed")
        else:
            print("Please select from one of the 5 menu options: ")
            print(menu)
            menu_condition = str(input(">>>"))


main()
