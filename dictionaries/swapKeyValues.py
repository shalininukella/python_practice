dict1 = {"a": 1, "b": 2}
inverted = {}
for k, v in dict1.items():
    inverted[v] = k

print(inverted)