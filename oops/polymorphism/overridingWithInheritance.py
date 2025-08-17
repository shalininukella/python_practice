class Animal:
    def sound(self):
        print('animal')

class Dog(Animal):
    def sound(self):
        print('dog')

class Cat(Animal):
    def sound(self):
        print("cat")

animals = [Dog(), Cat()]

for i in animals:
    i.sound()