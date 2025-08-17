from abc import ABC, abstractmethod

# Step 1: Create an abstract base class
class Animal(ABC):

    # Step 2: Define abstract method
    @abstractmethod
    def make_sound(self):
        pass

    # Normal method (optional)
    def sleep(self):
        print("This animal is sleeping...")

# Step 3: Subclass must implement abstract method
class Dog(Animal):
    def make_sound(self):
        print("Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

# Step 4: Create objects
dog = Dog()
cat = Cat()

dog.make_sound()   # Woof!
cat.make_sound()   # Meow!
dog.sleep()        # This animal is sleeping...

# a = Animal()  # ❌ Error