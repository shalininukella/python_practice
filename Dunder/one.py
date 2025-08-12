class MyList:
    def __init__(self, data):
        self.data = list(data)

    def __repr__(self):
        return f"MyList({self.data})"

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, index, value):
        self.data[index] = value

    def __contains__(self, item):
        return item in self.data

    def __add__(self, other):
        return MyList(self.data + list(other))

    def __call__(self, *args):
        print(f"MyList called with arguments {args}")

ml = MyList([1, 2, 3])
print(len(ml))       # __len__
print(ml[1])         # __getitem__
ml[1] = 20           # __setitem__
print(ml)            # __repr__
print(2 in ml)       # __contains__
print(ml + [4, 5])   # __add__
ml("hello")          # __call__
