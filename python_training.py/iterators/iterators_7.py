class even:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current > self.limit:
            raise StopIteration
        else:
            self.current += 2
            return self.current - 2
        
even_num = even(10)

for num in even_num:
    print(num)