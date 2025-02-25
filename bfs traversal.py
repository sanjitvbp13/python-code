from collections import deque

def bfs(graph, start):
    visited = set()  # To track visited nodes
    queue = deque([start])  # Initialize the queue with the starting node
    
    while queue:
        node = queue.popleft()  # Dequeue a node
        if node not in visited:
            print(node, end=" ")  # Process the node (print it)
            visited.add(node)  # Mark it as visited
            # Add all unvisited neighbors to the queue
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    queue.append(neighbor)

# Define the graph as an adjacency list
graph = {
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: [3]
}

print("BFS traversal:")
bfs(graph, 0)
