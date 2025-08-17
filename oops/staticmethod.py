class ForStaticMethod:
    def __init__(self, name):
        self.name = name
        print(self.name)

    @staticmethod
    def add(a,b):
        print(a+b)
        # print(name) #NameError: name 'name' is not defined

ForStaticMethod.add(3,4) # ✅ works without creating an object

fs = ForStaticMethod("Krishna")  
fs.add(2,3) # ✅ works but instance is not used

# add(5,6) #NameError: name 'add' is not defined
