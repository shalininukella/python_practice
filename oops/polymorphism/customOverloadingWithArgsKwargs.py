class Profile:
    def hello(self, *args, **kwargs):
        for i in args:
            print(f"hello {i}")

        for key, val in kwargs.items(): 
            print(f"key = {key}, value = {val}")
        

p = Profile()

p.hello("Krishna", "Ram", 21)
print("-----")
p.hello("Shalini", age=34)
