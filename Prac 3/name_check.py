def main():
    import random

    def get_name():
        name = str(input("Please enter your name: "))
        if name == "":
            print("You didn't enter your name!")

        else:
            n = random.randint(1, len(name))
            print_name(name,n)

    def print_name(name,n):
        print(name[::n])

    name = get_name()  



main()
