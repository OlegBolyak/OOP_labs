class FactorialCache:
    def __init__(self):
        self.cache=0
    def compute(self, n):
        res=1
        for n in range(1,n+1):
            res*=n
        if res>self.cache:
            self.cache=res
        return res

fc=FactorialCache()
print(fc.compute(5))
