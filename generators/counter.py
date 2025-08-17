def counter(n):
    while n > 0 :
        yield n
        n -= 1

cd = counter(4)
for i in cd:
    print(i) 

cd1 = counter(2)
print(next(cd1))
print(next(cd1))

# print(next(cd1)) 
# Traceback (most recent call last):
# File "/Users/shalininukella/Documents/python_practice/generators/counter.py", line 13, in <module>
#     print(next(cd1))
#           ~~~~^^^^^
# StopIteration

