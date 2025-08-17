class Person:
    def __init__(self, age):
        self.age = age
    
    def __eq__(self, other):
        return self.age == other.age
    
    def __lt__(self, other):
        return self.age < other.age
    
    def __gt__ (self, other):
        return self.age > other.age
    
p1 = Person(23)
p2 = Person(34)

print(p1 == p2)
print(p1 < p2)
print(p1 > p2)
