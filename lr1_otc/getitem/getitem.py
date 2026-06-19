class FIB_ITER:
    def __init__(self, max = None):
        self.max = max
        
    def __getitem__(self, index):
        if self.max is not None and index >= self.max:
            raise IndexError
        
        a = 0
        b = 1
        
        for i in range(index):
            temp = a
            a = b
            b = temp + b
        
        return a
     
if __name__ == "__main__":
    f = FIB_ITER(max = 10)

    for num in f:
        print(num, "\n")

