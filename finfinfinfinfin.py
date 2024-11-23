# Graph start -----------------------0

from collections import defaultdict #importing default dictionary

class Graph: #graph class
    def __init__(self): #init
        self.graph = defaultdict(list)

    def createEdge(self, u,v): #creating the edges (the connections)
        self.graph[u].append(v)

    def DFSUtil(self, v, visited):
        visited.add(v)
        print(v)
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)

    def DFS(self, v): #dfs function depth first search
        visited = set() #visited turns into a set (basically a fancy list with only unique values)
        self.DFSUtil(v, visited)

# Graph end --------------------------0

# Object start -----------------------0

g = Graph() #object
g.createEdge(0, 1) #creating edges
g.createEdge(0, 2) #line 28
g.createEdge(0, 3) #line 28
g.createEdge(1, 3) #line 28
g.createEdge(2, 3) #line 28
g.createEdge(1, 2) #line 28
g.createEdge(1, 3) #line 28

g.DFS(0) #call dfs function to print the graph

# Object end -------------------------0