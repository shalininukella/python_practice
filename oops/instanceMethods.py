
class Student:
    school = 'kv'

    def __init__(self, name, marks):
        self.name = name
        self.marks = list(marks)

    def average(self):
        return sum(self.marks)/len(self.marks)

    def grade(self):
        avg = self.average()
        if avg > 90: return 'a'
        elif avg > 80: return 'b'
        else: return 'k'

s = Student('jo', [89, 80, 67, 45])
print(s.name)
print(s.marks)
print(s.average())
print(s.grade())