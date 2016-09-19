from Prac8.taxi import Taxi


def main():
    taxi = Taxi("Prius 1", 100)

    taxi.drive(40)
    print("The taxi drove {}km".format(taxi.current_fare_distance))
    print(taxi)

    taxi.start_fare()
    taxi.drive(100)
    print("The taxi drove {}km".format(taxi.current_fare_distance))
    print(taxi)
    print(taxi.get_fare())


main()
