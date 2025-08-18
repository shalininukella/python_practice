# ✅ So in short:
# .update() is used to merge dictionaries or add/update multiple key-value pairs at once.

d1= { "a" : 1, "b" : 2}
d2 = {"c": 3, "d": 4}

d1.update({"a" : 2})
d1.update(d2)
print(d1)

d1["f"] = 6
print(d1)

d2.update(age = 23, name = "Krishna")
print(d2)

