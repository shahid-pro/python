# Inheritance
class Person:
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print(self.name)
        print(self.idnumber)

# Child class
class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post
        super().__init__(name, idnumber)  # invoking the init of the parent class

    def details(self):
        print("My name is {}".format(self.name))
        print("IdNumber: {}".format(self.idnumber))
        print("Post: {}".format(self.post))

# Object instantiation
a = Employee('Rahul', 886012, 200000, "Intern")
# calling a function of the class Person using its instance
a.display()
a.details()

# Polymorphism/Overriding
class Bird:
    def intro(self):
        print("There are many types of birds.")

    def flight(self):
        print("Most of the birds can fly, but some cannot.")

class Sparrow(Bird):
    def flight(self):
        print("Sparrows can fly.")

class Ostrich(Bird):
    def flight(self):
        print("Ostriches cannot fly.")

# Creating objects and calling their methods
bird1 = Bird()
bird1.intro()
bird1.flight()

sparrow1 = Sparrow()
sparrow1.intro()
sparrow1.flight()

ostrich1 = Ostrich()
ostrich1.intro()
ostrich1.flight()