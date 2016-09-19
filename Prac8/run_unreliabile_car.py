from Prac8.taxi import UnreliableCar


def main():
    car = UnreliableCar("Bad Car", 100, 50)

    car.drive(60)
    print(car)


main()
