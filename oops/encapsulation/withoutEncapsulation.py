class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
s = Student("Ram", [100, 100])

#can easily directly access without any restriction
print(s.marks) 
print(s.name)

#can directly modify, and even accidental modification is possible
s.name = "Krishna"
print(s.name)