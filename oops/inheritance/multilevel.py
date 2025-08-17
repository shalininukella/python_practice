class Grand:
    def house(self):
        print('has a house')

class Parent(Grand):
    def car(self):
        print("owns a car")

class Child(Parent):
    def bike(self):
        print("owns a bike")

c = Child()

c.house()
c.car()
c.bike()