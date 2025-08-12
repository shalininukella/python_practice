import re

m = re.search(r"(\d{3})-(\d{2})-(\d{4})", "SSN: 123-45-6789")
print(m.group(0))  # '123-45-6789'
print(m.group(1))# '123'
print(m.group(2)) #45
print(m.group(3)) #6789
print(m.groups())  # ('123','45','6789')

