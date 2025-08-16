a = [1,2,3,4,5]

#List
squared_list = [x**2 for x in a]

#filtered list
even_squared_list = [x**2 for x in a if x%2 == 0]

#Dictionary
squared_dict = {x: x**2 for x in a}

#filtered dict
even_squared_dict = {x:x**2 for x in a if x%2 == 0}

#Set
squared_set = {x**2 for x in a}

#filtered set
even_squared_set = {x**2 for x in a if x%2 ==0}

#Generators 
squared_generator = (x**2 for x in a)

#filtered generator
even_squared_generator = (x**2 for x in a if x%2 == 0)

#Nested Comprehension - on any ds, let's take list here
nested_list = [[1,2,3], [4,5,6], [7,8,9]]
flatten_list = [x for row in nested_list for x in row]

#filtered nested list
flatten_even = [x for row in nested_list for x in row if x%2 == 0]

print("squared_list:", squared_list)
print("even_squared_list:", even_squared_list)

print("squared_dict:", squared_dict)
print("even_squared_dict:", even_squared_dict)

print("squared_set:", squared_set)
print("even_squared_set:", even_squared_set)

# Generators need to be converted to a list to display
print("squared_generator:", list(squared_generator))
print("even_squared_generator:", list(even_squared_generator))

print("flatten_list:", flatten_list)
print("flatten_even:", flatten_even)
