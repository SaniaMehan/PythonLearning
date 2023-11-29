# Multilevel Inheritance
#Level - GF -> Father -> Son


class Grandparent:
    def grandparent_method(self):
        return "Grandparent's method"


class Parent(Grandparent):
    def parent_method(self):
        return "Parent's method"

class Child(Parent):
    def child_method(self):
        return "Child's method"

child = Child()
parent= Parent()
gp= Grandparent()
print(child.grandparent_method())
print(child.parent_method())
print(child.child_method())
print(parent.parent_method())
print(parent.grandparent_method())
print(gp.grandparent_method())
