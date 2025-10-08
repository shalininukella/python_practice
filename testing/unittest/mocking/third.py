from unittest.mock import Mock

m = Mock()

print(m()) #return a mock object
print(m.return_value) # is equal to m(), m() === m.return_value
#prints <Mock name='mock()' id='2243079748112'> for both the print statements

# m() = 21
# print(m()) #error

# m.return_value = 21
# print(m())
#prints 21

print(m().foo) #mock
# prints <Mock name='mock().foo' id='2001062066704'>

print(m().foo()) #mock
#prints <Mock name='mock().foo()' id='2001062067040'>

#but we can set what m().foo() should print
#we cant do m().foo() = 21, alternatively we can m.return_value.foo.return_value = 21, cuz m.return_value === m(), but we can't assign directly to the function form m() = something, instead do it in the attribute form
m.return_value.foo.return_value = 21
print(m().foo())
#prints 21

another = Mock()
x = another.return_value
print(x.foo())
# prints <Mock name='mock().foo()' id='1720857543744'>

x.foo.return_value = 34
print(another().foo())
#prints 34