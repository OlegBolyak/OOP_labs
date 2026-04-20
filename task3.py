class LRUCache:
    def __init__(self, size):
        self.size=size
        self.cache={}
    def put(self, key, value):
        if len(self.cache)<self.size:
            self.cache[key]=value
        else:
            self.cache.popitem()
    def get(self, key):
        print(self.cache[key])

cache=LRUCache(2)
cache.put(1,1)
cache.put(2,2)
print(cache.cache)
cache.get(1)       # Output: 1
cache.put(3,3)     # видаляє ключ 2
print(cache.cache)