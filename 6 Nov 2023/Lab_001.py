class Car:
    name = "Sania" # Class Varaible
# in this assign the value of make and model
    def __init__(self,make,model): # Default constructor
        self.make = make  #  Instance Variable
        self.model = model # Instance Variable
        print("I will be called first")

# in this reuse the value of make and model
    def start_engine(self):
        print("Starting a car", self.make, self.model)


car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "Civic")

car1.start_engine()
car2.start_engine()

print(id(car1))
print(id(car2))


# Object is created a Special Function is called automatically __int__()
# All the attribute Object you can initilize - add some initial value to them