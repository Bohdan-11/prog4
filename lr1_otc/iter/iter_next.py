class FIB_ITER:
    def __init__(self, max = None):
        self.max = max
        self.count = 0
        self.a = 0
        self.b = 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.max is not None and self.count >= self.max:
            raise StopIteration
        
        result = self.a 
        self.a = self.b
        self.b = result + self.b
        self.count += 1 
        
        return result

if __name__ == "__main__":
    f = FIB_ITER(max = 10)
    for num in f:
        print(num, "\n")
