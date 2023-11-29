#Create a Car class and Create 2 Objects of the class with attributes 5 and 5 methods

class Car:
    name = None
    price = None
    model = None
    tyrecompany  = None
    seatcover = None

    def tyre(self):
        print("Company tyre name is = " + self.tyrecompany)

    def seat_belt(self):
        print("Proper aligned")

    def break_quality(self):
        print("High break")

    def engine(self):
        print("Start engine")

    def light(self):
        print("High beam light")

creta_obj = Car()
kia_obj =  Car()

creta_obj.tyrecompany =  "Mrf"
kia_obj.tyrecompany = "Apollo"

creta_obj.tyre()
kia_obj.tyre()