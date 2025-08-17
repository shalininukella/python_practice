class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age
    
    def set_age(self, new_age):
        if new_age > 18:
            self.__age = new_age
        else:
            print(f"can't change the age, because {new_age} is less than 18 restricted!!! So enables validation before modifying attributes.")

    def set_name(self, new_name):
        if 'i' in new_name:
            self.__name = new_name
        else:
            print(f"can't change the name, {new_name} doesn't have an 'i'!!! So enables validation before modifying attributes.")

s = Student("Rohan", 23)
print(s.get_name())
print(s.get_age())
s.set_age(2)
print(s.get_age())
s.set_age(99)
print(s.get_age())
s.set_name('Neha')
print(s.get_name())
s.set_name('Krishna')
print(s.get_name())


        
    
