from unittest.mock import Mock

m = Mock()
# when m() is called it usually returns another mock object, but we can control it, but setting a return value to iter
print(m())

m.return_value = 23
print(m())

# output 

# <Mock name='mock()' id='2259795540160'>
# 23

