#_minimum spanning Tree

'''[2,3]
[1,5]
[1,4,6]
[3]
[2,7]
[3,7]
[5,6]
'''
'''
from collections import defaultdict




class Graph:

    def __init__(self, vertices):

        self.V = vertices  

        
        self.graph = defaultdict(list)

    
    def addEdge(self, v, w):

       
        self.graph[v].append(w)

        
        self.graph[w].append(v)

    
    def isCyclicUtil(self, v, visited, parent):

        
        visited[v] = True

       
        for i in self.graph[v]:

            
            if visited[i] == False:
                if(self.isCyclicUtil(i, visited, v)):
                    return True
          
            elif parent != i:
                return True

        return False

   
    def isCyclic(self):

       
        visited = [False]*(self.V)

        #
        for i in range(self.V):

            
            if visited[i] == False:
                if(self.isCyclicUtil
                   (i, visited, -1)) == True:
                    return True

        return False



g = Graph(7)
g.addEdge[2,3]
g.addEdge[2,3]
g.addEdge[1,5]
g.addEdge[1,4,6]
g.addEdge[3]
g.addEdge[2,7]
g.addEdge[3,7]
g.addEdge[5,6]


if g.isCyclic():
    print("Graph contains cycle")
else:
    print("Graph doesn't contain cycle ")
#g1 = Graph(3)
#g1.addEdge(0, 1)
#g1.addEdge(1, 2)


if g1.isCyclic():
    print("Graph contains cycle")
else:
    print("Graph doesn't contain cycle ")


'''

from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def addEdge(self, v, w):
        self.graph[v].append(w)
        self.graph[w].append(v)

    def isCyclicUtil(self, v, visited, parent):
        visited[v] = True
        for i in self.graph[v]:
            if not visited[i]:
                if self.isCyclicUtil(i, visited, v):
                    return True
            elif parent != i:
                return True
        return False

    def isCyclic(self):
        visited = [False] * self.V
        for i in range(self.V):
            if not visited[i]:
                if self.isCyclicUtil(i, visited, -1):
                    return True
        return False

g = Graph(7)


g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 4)
g.addEdge(2, 3)
g.addEdge(2, 5)
g.addEdge(4, 6)
g.addEdge(5, 6)


if g.isCyclic():
    print("Graph contains cycle")
else:
    print("Graph doesn't contain cycle")


