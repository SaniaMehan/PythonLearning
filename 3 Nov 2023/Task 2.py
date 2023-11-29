# Create a Class Person , Two Objects by taking (name, age, address)
# Input from users and print details in the end.
class Person:
    name = None
    age = None
    address = None

    def details(self):
        print("Details of the person is = ", self.name, self.age, self.address)


name = input("Enter your name")
age = input("Enter age")
address = input("Enter address")

obj = Person()
obj.name = name
obj.age = age
obj.address = address

obj.details()