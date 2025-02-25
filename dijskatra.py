from collections import defaultdict

class Graph:
    def init(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def addNode(self, value):
        self.nodes.add(value)

    def addEdge(self, fromNode, toNode, distance):
        self.edges[fromNode].append(toNode)
        self.distances[(fromNode, toNode)] = distance


def dijkstra(graph, initial):
    visited = {initial: 0}  
    path = defaultdict(list)  
    nodes = set(graph.nodes)

    while nodes:
        minNode = None
       e
        for node in nodes:
            if node in visited:
                if minNode is None:
                    minNode = node
                elif visited[node] < visited[minNode]:
                    minNode = node

        if minNode is None:
            break

        nodes.remove(minNode)
        currentWeight = visited[minNode]

        for edge in graph.edges[minNode]:
            weight = currentWeight + graph.distances[(minNode, edge)]
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge] = path[minNode] + [minNode]

    return visited, path



customerGraph = Graph()
customerGraph.addNode("A")
customerGraph.addNode("B")
customerGraph.addNode("C")
customerGraph.addNode("D")
customerGraph.addEdge("A", "B", 1)
customerGraph.addEdge("A", "C", 4)
customerGraph.addEdge("B", "C", 2)
customerGraph.addEdge("B", "D", 6)
customerGraph.addEdge("C", "D", 3)

distances, paths = dijkstra(customerGraph, "A")
print("Shortest distances:", distances)
print("Paths:")
for destination, path in paths.items():
    print(f"{destination}: {' -> '.join(path + [destination])}")from collections import defaultdict

class Graph:
    def init(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def addNode(self, value):
        self.nodes.add(value)

    def addEdge(self, fromNode, toNode, distance):
        self.edges[fromNode].append(toNode)
        self.distances[(fromNode, toNode)] = distance


def dijkstra(graph, initial):
    visited = {initial: 0}  
    path = defaultdict(list)  
    nodes = set(graph.nodes)

    while nodes:
        minNode = None
       e
        for node in nodes:
            if node in visited:
                if minNode is None:
                    minNode = node
                elif visited[node] < visited[minNode]:
                    minNode = node

        if minNode is None:
            break

        nodes.remove(minNode)
        currentWeight = visited[minNode]

        for edge in graph.edges[minNode]:
            weight = currentWeight + graph.distances[(minNode, edge)]
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge] = path[minNode] + [minNode]

    return visited, path



customerGraph = Graph()
customerGraph.addNode("A")
customerGraph.addNode("B")
customerGraph.addNode("C")
customerGraph.addNode("D")
customerGraph.addEdge("A", "B", 1)
customerGraph.addEdge("A", "C", 4)
customerGraph.addEdge("B", "C", 2)
customerGraph.addEdge("B", "D", 6)
customerGraph.addEdge("C", "D", 3)

distances, paths = dijkstra(customerGraph, "A")
print("Shortest distances:", distances)
print("Paths:")
for destination, path in paths.items():
    print(f"{destination}: {' -> '.join(path + [destination])}")