# 15. How to remove duplicates from a dictionary (by values or keys)?

# By keys → already unique.

# By values → invert dict, keeping unique values.

d = {"a": 1, "b": 2, "c": 1}
print(d)

#invert, and it automatically removes 
new_d = {v:k for k,v in d.items()}
print(new_d)

d = {k:v for k, v in new_d.items()}
print(d)