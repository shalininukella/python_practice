class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return (self.x + other.x, self.y + other.y)
    
    def __mul__(self, other):
        return (self.x * other.x, self.y * other.y)
    
    def __str__(self):
        return f"x = {self.x}, y = {self.y}"
    
v1 = Vector(2, 3)
v2 = Vector(5, 7)

print(v1)
print(v2)

print(v1 + v2)
print(v1 * v2)