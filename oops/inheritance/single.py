class Animal:
    def sound(self):
        print('Animal makes sound')

class Dog(Animal):
    def bark(self):
        print("Dog makes sound")

d = Dog()
d.sound()
d.bark()
