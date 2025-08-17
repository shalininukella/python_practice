class Parent:
    def __init__(self, name):
        self.name = name

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age


c = Child("Krishna", 234)
print(c.age)
print(c.name)
