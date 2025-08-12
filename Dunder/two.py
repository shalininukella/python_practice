class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # def __str__(self):
    #     return f"Vector({self.x}, {self.y})"
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __len__(self):
        return 2  # Always 2 dimensions

# Using the class
v1 = Vector(2, 4)
v2 = Vector(5, -2)

print(v1)          # Calls __str__ → Vector(2, 4)
print(len(v1))     # Calls __len__ → 2
print(v1 + v2)     # Calls __add__ → Vector(7, 2)
