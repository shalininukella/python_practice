lst = [1,23,4]
lst1 = lst.copy()

print(lst)
print(lst1)

lst1[1] = 5
print(lst1)
print(lst)

print("--------")

dict1 = {"a":1, "b": 2}
dict2 = dict1.copy()

print(dict1)
print(dict2)

print("--------")

set1 = {1,2,3,4,5}
set2 = set1.copy()

print(set1)
print(set2)

print("--------")

# ❌ Tuples do not have a .copy() method.
# tuple1 = (1,2,3)
# tuple2 = tuple1.copy()
# print(tuple1)
# print(tuple2)

import copy 

lst2 = [1,2,3,4,5]
lst3 = copy.copy(lst2)

print(lst2)
print(lst3)

print("--------")

dict3 = {"a":1, "b": 2}
dict4 = copy.copy(dict3)

print(dict3)
print(dict4)

print("--------")

set3 = {1,2,3,4}
set4 = copy.copy(set3)

print(set3)
print(set4)

print("--------")

tuple3 = (1,2,3)
tuple4 = copy.copy(tuple3)

print(tuple3)
print(tuple4)

print("--------")
