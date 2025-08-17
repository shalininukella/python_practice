class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = list(marks)

    def average(self):
        return sum(self.marks)/len(self.marks)
    
    def grade(self):
        avg = self.average()
        if avg > 90: return "pass"
        else: return 'fail'
        
    def __str__(self):
        return f"name is {self.name}, marks is {self.marks}, avg is {self.average()}, grade is {self.grade()}"
    
    def __repr__(self):
        return f"Student({self.name}, {self.marks})"
    

s = Student('jon', [78, 78, 99, 98, 98])
print(s.name, s.marks, s.average(), s.grade())
print(s)
print(repr(s))
print(str(s))