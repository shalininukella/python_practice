class MyList:
    def __init__(self, items):
        self.items = items
    
    def __len__(self):
        return len(self.items)
    
    def __getitem__(self, index):
        return self.items[index]
    
    def __setitem__(self, index, value):
        self.items[index] = value
    
    def __delitem__(self, index):
        del self.items[index]

lst = MyList([1, 2, 3]) 
print(lst.items)      #[1, 2, 3]
print(len(lst))       # 3
print(lst[1])         # 2
lst[1] = 20
print(lst[1])         # 20
del lst[1]
print(lst.items)      # [1, 3]
