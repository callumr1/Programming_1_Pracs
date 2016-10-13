"""
CP1404/CP5632 Practical
Car class
"""
import random

class Car:
    """ represent a car object """

    def __init__(self, name="", fuel=0):
        """ initialise a Car instance """
        self.name = name
        self.fuel = fuel
        self.odometer = 0

    def __str__(self):
        return "{}, fuel={}, odo={}".format(self.name, self.fuel, self.odometer)

    def add_fuel(self, amount):
        """ add amount to the car's fuel"""
        self.fuel += amount

    def drive(self, distance):
        """ drive the car a given distance if it has enough fuel or drive until fuel runs out
        return the distance actually driven """
        if distance > self.fuel:
            distance_driven = self.fuel
            self.fuel = 0
        else:
            self.fuel -= distance
            distance_driven = distance
        self.odometer += distance_driven
        return distance_driven


class Taxi(Car):
    """ specialised version of a Car that includes fare costs """
    price_per_km = 1.20

    def __init__(self, name, fuel):
        """ initialise a Taxi instance, based on parent class Car """
        super().__init__(name, fuel)
        self.current_fare_distance = 0

    def __str__(self):
        """ return a string representation like a car but with current fare distance"""
        return "{}, ${:.2f}/km, {}km on current fare".format(super().__str__(), Taxi.price_per_km,
                                                             self.current_fare_distance)

    def get_fare(self):
        """ get the price for the taxi trip """
        return Taxi.price_per_km * self.current_fare_distance

    def start_fare(self):
        """ begin a new fare """
        self.current_fare_distance = 0

    def drive(self, distance):
        """ drive like parent Car but calculate fare distance as well"""
        distance_driven = super().drive(distance)
        self.current_fare_distance += distance_driven
        return distance_driven

class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability):
        #initialise an Unreliable instance, based on parent class Car
        super().__init__(name, fuel)
        self.reliability = reliability

    def random_drive(self, distance):
        #drive like parent Car but calculate fare distance as well
        rand_drive = random.randint(0,100)
        print(rand_drive)
        if rand_drive <= self.reliability:
            if distance > self.fuel:
                distance_driven = self.fuel
                self.fuel = 0
            else:
                self.fuel -= distance
                distance_driven = distance
            self.odometer += distance_driven
            return distance_driven


class SilverServiceTaxi(Taxi):
    fanciness = 2
    flagfall = 4.50

    def __init__(self, name, fuel):
        super().__init__(name, fuel)
        Taxi.price_per_km = Taxi.price_per_km * SilverServiceTaxi.fanciness

    def get_silver_fare(self):
        return Taxi.get_fare(self) + SilverServiceTaxi.flagfall