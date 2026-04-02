class Graph:
    def __init__(self):
        self.graph=[]
    def add_edge(self, node1, node2):
        self.graph.append((node1,node2))
    def neighbors(self, node):
        for n in self.graph:
            if n[0]==node:
                return f"neighbour node {node} is {n[1]}"
            elif n[1]==node:
                return f"neighbour node {node} is {n[0]}"
            else:
                return f"no found neighbour for {node}"

g=Graph()
g.add_edge("A", "B")
print(g.neighbors("C"))




