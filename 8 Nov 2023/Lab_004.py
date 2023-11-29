# Parent - Child
# Father -> son
# GF -> Father -> Son
# 1BHK -> 1 BHK -> 1BHK

# Single Inheritance

class Animal:

    def car(self):
        print("Lambo")

    def speak(self):
      pass


class Dog(Animal):
    def speak(self):
        print("Bow Bow")

    def drive(self):
        Animal().car()



dog = Dog()
dog.speak()
dog.car()
dog.drive()
