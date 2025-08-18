keys = ["a", "b", "c"]
values = [1, 2, 3]

# x = zip(keys, values)
# print(x) # <zip object at 0x1044dccc0>

x = dict(zip(keys, values))
print(x)