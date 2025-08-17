class Counter:
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        return self  # Iterator object returns itself
    
    def __next__(self):
        if self.current < self.high:
            self.current += 1
            return self.current - 1
        else:
            raise StopIteration
        
counter = Counter(1, 5) #it's like an iterator
for i in counter:
    print(i)