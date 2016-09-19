from Prac8.taxi import SilverServiceTaxi

def main():
    taxi = SilverServiceTaxi("Taxi", 100)

    taxi.drive(10)
    print("The taxi drove {}km".format(taxi.current_fare_distance))
    print(taxi)
    print("The total cost is: ${:.2f}km".format(taxi.get_silver_fare()))

main()