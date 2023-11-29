# Collection -

# list, dic, tuple, set, OrderedDict - Data Type

regular_tuple = (1, 2, 3)
#regular_tuple[0] = 20 # They are not mutable

print(regular_tuple[0])

from collections import namedtuple

Person = namedtuple("Person", ["name", "age", "gender"])



person = Person(name="Sania", age=32, gender="F")

print("Name", person.name)
print("Age", person.age)
print("Gender", person.gender)


class Person2:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def print_details(self):
        print(f"Person details {self.name, self.age}")


person2 = Person2("Sania", 32, "M")
person2.print_details()
