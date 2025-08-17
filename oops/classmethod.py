class ForClassMethod:
    count = 0 #class variable, can be modified by classMethod

    def __init__(self, name):
        self.name = name
        print(f"from constructor, {self.name}")
    
    @classmethod #alternative constructors also called
    def counting(cls):
        cls.count += 1
        print(cls.count)
        # print({self.name}) #doesn't work, can't acess the instance variable

print("By class")
ForClassMethod.counting()

print("-------")

fc = ForClassMethod("Krishna")
print("By the object")
fc.counting() # works


    