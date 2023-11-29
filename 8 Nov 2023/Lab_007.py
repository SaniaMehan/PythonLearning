# Hierarchical Inheritance:
class Vehicle:  #father
    def info(self):
        return "This is a vehicle."


class Car(Vehicle): # son of father
    def info(self):
        return "This is a car."


class Bicycle(Vehicle): # daughter of father
    def info(self):
        return "This is a bicycle."


car = Car()
bicycle = Bicycle()
vehicle = Vehicle()
print(car.info())
print(bicycle.info())
print(vehicle.info())