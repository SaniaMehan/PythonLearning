class Person:

    def __init__(self):
        print("Can I use you?")  # Not able to use this because we can use only one which is parametrize

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("You created an Object with name and age")

    def printDetails(self):
        print("Your details are", self.name, self.age)

    def printDetails2(self):
        print("Your details are", self.name * 2)


amit = Person("amit", 34)
amit.printDetails()
amit.printDetails2()

nikhil = Person("nikhil", 45)
nikhil.printDetails()
nikhil.printDetails2()