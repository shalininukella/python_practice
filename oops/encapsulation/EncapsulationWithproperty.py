class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    @property # getter
    def age(self):
        return self.__age
    
    @property # getter
    def name(self):
        return self.__name
    
    @age.setter # setter
    def age(self, new_age):
        if new_age > 18:
            self.__age = new_age
        else:
            print(f"invalid age - {new_age}")

    @name.setter # setter
    def name(self, new_name):
        if 'i' in  new_name:
            self.__name = new_name 
        else: 
            print(f"invalid name - {new_name}, enter a name with i in it")

s = Student('Rohan', 23)
print(s.age)
print(s.name)

s.age = 2
print(s.age)

s.age = 99
print(s.age)

s.name = "Tara"
print(s.name)

s.name = 'Krishna'
print(s.name)


