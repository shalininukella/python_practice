import copy

lst1 = [1,2,3]
lst2 = copy.deepcopy(lst1)

dict1 = {"a":1, "b":2, "c": {"d":4}}
dict2 = copy.deepcopy(dict1)
dict2.update({"c" : {"d":5}})

print(dict2)
print(dict1)

set1 = {1,2,3}
set2 = copy.deepcopy(set1)

tuple1 = (1,2,3)
tuple2 = copy.deepcopy(tuple1)

print(lst1, lst2, set1, set2, dict1, dict2, tuple1, tuple2)