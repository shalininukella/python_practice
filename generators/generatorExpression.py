squares = (x**2 for x in range(5))
print(squares) #<generator object <genexpr> at 0x1004ab440>
print(list(squares)) #[0, 1, 4, 9, 16]


# print(next(squares))
# Traceback (most recent call last):
#   File "/Users/shalininukella/Documents/python_practice/generators/generatorExpression.py", line 4, in <module>
#     print(next(squares))
#           ~~~~^^^^^^^^^
# StopIteration

squares1 = (x**2 for x in range(5))
print(next(squares1))
print(next(squares1))
