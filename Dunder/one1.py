class Mylist:
    def __init__(self, data):
        self.data = list(data)
    
    def __str__(self):
        return f"My list is {self.data}"
    
    def __repr__(self):
        return f"Alternative to str. MyList({self.data})"
    
    def __add__(self, other):
        new_list = []
        for i in range(len(self.data)):
            new_list.append(self.data[i] + other.data[i])
        return new_list

    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, idx):
        return self.data[idx]
    
    def __setitem__(self, idx, val):
        self.data[idx] = val

    def __call__(self, *args, **kwargs):
        print(f"callable with argument = {args} and key word arguments = {kwargs}")

    def __contains__(self, item):
        return item in self.data
    
    def __delitem__(self, idx):
        del self.data[idx]
    
ml = Mylist([1,2,3,4,5])
nl = Mylist([2,3,4,5,6])
print(ml) #str
print(repr(ml)) #repr
print(ml + nl) # add
print(len(ml)) # length
print(ml[2]) # getitem
ml[1] = 0 #setitem
print(ml[1])
ml() # call wihtout args
ml(1,3, "Krishna") # call wiht args
ml(56, age = 5, name = "krishna") # call wiht kwargs
print(4 in ml) # true or false = __contains__
print(45 in nl) # false
del nl[4]
print(nl)

