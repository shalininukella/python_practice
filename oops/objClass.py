class Student:
    #class attribute 
    school = "kv"

    #constructor
    def __init__(self, name, marks):
        self.name = name
        self.marks = list(marks)
    
s1 = Student('Krishna', [10, 10, 10])
s2 = Student('ROn', [1,2,3,4])

#extract the class attributes
print(s1.school)
print(s2.school)
print(Student.school)

#extract the instance attributes
print(s1.name, s1.marks)
print(s2.name, s2.marks)

s1.school = 'dps'
print(s1.school)
print(s2.school)
print(Student.school)


print(s1.__dict__)
print(Student.__dict__)

print("s1.__dict__ =", s1.__dict__)
print("Student.__dict__ has 'school'? ->", "school" in Student.__dict__)

