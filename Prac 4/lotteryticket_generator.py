def main():


    number_of_tickets = int(input("How many quick picks? "))

    generate_tickets(number_of_tickets)

def generate_tickets(number_of_tickets):
    import random
    for x in range(1, number_of_tickets + 1):
        rangeMax = 45
        rangeMin = 1
        ticketMax = 7

        ticket = []
        for y in range(1, ticketMax):
            number = random.randint(rangeMin, rangeMax)
            while number in ticket:
                number = random.randint(rangeMin, rangeMax)
            ticket.append(number)
        print(sorted(ticket))


main()