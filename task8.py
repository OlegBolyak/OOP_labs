class BoundedStack:
    def __init__(self, size):
        self.size=size
        self.stack=[]
    def push(self, n):
        if len(self.stack)<self.size:
            self.stack.append(n)
        else:
            raise Exception("Error")

stack=BoundedStack(3)
stack.push(2)
stack.push(2)
stack.push(2)

stack.push(2)


