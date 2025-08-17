class Animal:
    def sound(self):
        print("animal")

class Dog(Animal):
    def bark(self):
        print('dog')

class Cat(Animal):
    def meow(self):
        print('cat')

c = Cat()
c.meow()
c.sound()

d = Dog()
d.bark()
d.sound()
