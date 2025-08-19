# ✅ So in short:
# .update() is used to merge dictionaries or add/update multiple key-value pairs at once.
# If keys overlap, the second dictionary overwrites values.

d1 = {"a" : 1, "b": 2}
d2 = {"c" : 3, "d": 4}

d1.update(d2)
print(d1)

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

dict1.update(dict2)
print(dict1)


# {'a': 1, 'b': 3, 'c': 4}
# 👉 Notice:
# "b" was updated from 2 → 3
# "c" was added

#or python 3.7+
merged = {**dict1, **dict2}
print(merged)