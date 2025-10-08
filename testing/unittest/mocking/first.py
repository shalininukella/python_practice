from unittest.mock import Mock

#instance of Mock class
#m can act as a function, instance, class, method, anything
m = Mock()

print(m) #here m is like an instance - object
print(m.foo) #here we are trying the attribute foo on the instance mock m 
print(m.bar()) #here we are trying the mehtod bar() on the instance mock m

res = m() #here m is like a function or a method
print(res) #print the result returned by the function mock m() - again a mock is returned

# output 

# <Mock id='2528260713040'>
# <Mock name='mock.foo' id='2528260716736'>
# <Mock name='mock.bar()' id='2528260717408'>
# <Mock name='mock()' id='2528261980576'>