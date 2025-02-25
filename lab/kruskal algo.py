class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
        self.nodes = []
        self.MST = []

    def addEdge(self, s, d, w):
        self.graph.append([s, d, w])

    def addNode(self, value):
        self.nodes.append(value)

    def printSolution(self):
        for s, d, w in self.MST:
            print(f"{s} - {d}: {w}")

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskalAlgo(self):
        
        self.graph = sorted(self.graph, key=lambda item: item[2])

        parent = {}
        rank = {}

        
        for node in self.nodes:
            parent[node] = node
            rank[node] = 0

        e = 0  
        i = 0  

        while e < self.V - 1:
            s, d, w = self.graph[i]
            i += 1

            x = self.find(parent, s)
            y = self.find(parent, d)

          
            if x != y:
                e += 1
                self.MST.append([s, d, w])
                self.union(parent, rank, x, y)

        self.printSolution()


g = Graph(5)

g.addNode("A")
g.addNode("B")
g.addNode("C")
g.addNode("D")
g.addNode("E")

g.addEdge("A", "B", 5)
g.addEdge("A", "C", 13)
g.addEdge("A", "E", 15)
g.addEdge("B", "C", 10)
g.addEdge("B", "D", 8)
g.addEdge("C", "E", 20)
g.addEdge("C", "D", 6)

g.kruskalAlgo()
