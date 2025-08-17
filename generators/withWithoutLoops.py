def gen_func():
    yield 1
    yield 2
    yield 3
gen = gen_func()
# print(gen) #<generator object gen_func at 0x102246610>

print(next(gen))
print(next(gen))
print(next(gen))


#expires and runs only if we create another generator again
for i in gen:
    print(i)

#so 
gen1 = gen_func()
for i in gen1:
    print(i)