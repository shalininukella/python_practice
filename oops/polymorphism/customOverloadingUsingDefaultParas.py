class Profile:
    def hello(self, name, age = None):
        if age is not None:
            print(f"hey, {name}, your age = {age}")
        else:
            print(f"hello {name}")

p = Profile()
p.hello("Krishna", 21)
p.hello("Ram")

