from decimal import Clamped


class Animal:
    def sound(self):
        print("Some sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

class Cat(Animal):
    def sound(self):
        print("Meow")

class Baby1(Cat, Dog): # Baby1().sound()  would print Meow due to MRO and C3 Linearization
    def baby(self):
        print("baby1") 

class Baby2(Dog, Cat): # Baby2().sound()  would print Bark due to MRO and C3 Linearization
    def baby(self):
        print("baby2") 

Dog().sound()
Cat().sound()
Baby1().sound() 
Baby2().sound()
