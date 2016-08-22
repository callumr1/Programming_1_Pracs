def main():


    num = int(input("How many quick picks? "))

    generate_tickets(num)


def generate_tickets(num):
    import random
    for x in range(1, num + 1):
        ticket = []
        for y in range(1, 7):
            number = random.randint(1, 45)
            while number in ticket:
                number = random.randint(1, 45)
            ticket.append(number)
        print(sorted(ticket))


main()