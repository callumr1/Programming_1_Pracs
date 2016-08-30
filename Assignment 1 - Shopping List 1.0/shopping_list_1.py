"""
CP1404 Assignment 1 - Shopping List 1.0
Written by Callum Robertson
"""


def main():
    users_name = "Callum"
    print("Greetings {} and welcome to your shopping list!\n".format(users_name))

    menu = "1 - View Required items\n2 - View Completed items\n3 - Add or change an item\n4 - Exit your shopping list"
    print("What would you like to do? Enter either 1, 2, 3 or 4 from the menu options below:")
    print(menu)
    menu_condition = str(input(">>>"))

    while menu_condition != "4":
        if menu_condition == "1":
            print("Required items and total price")
            print(menu)
            menu_condition = str(input(">>>"))
        elif menu_condition == "2":
            print("Completed items and total cost")
            print(menu)
            menu_condition = str(input(">>>"))
        elif menu_condition == "3":
            print("Add or change an item from required to completed")
            print(menu)
            menu_condition = str(input(">>>"))


main()
