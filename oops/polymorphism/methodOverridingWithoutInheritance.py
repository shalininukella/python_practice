class Animal:
    def sound(self):
        print('animal makes sound')
    
class Dog:
    def sound(self):
        print("dog barks")

class Cat:
    def sound(self):
        print("cats meows")

animals = [Animal(), Dog(), Cat()]

for animal in animals:
    animal.sound()