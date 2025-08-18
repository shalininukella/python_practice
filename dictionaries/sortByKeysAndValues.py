dict1 = {"a": 1, "b": 99, "c":3, "d": -3}

#by keys
sorted_dict = dict(sorted(dict1.items()))
print(sorted_dict)

#by keys
sorted_dict_val = dict(sorted(dict1.items(), key=lambda x: x[1]))
print(sorted_dict_val)

sorted_key_val = dict(sorted(sorted_dict.items(), key = lambda x: x[1], reverse=True))
print(sorted_key_val)


