 # Graph start -------------------------0

graph ={ #graph function 
    'A':['B','C','D'], # Connections
    'B':['E'], #line 2
    'C':['D','E'], #line 2
    'D':[], #line 2
    'E':[] #line 2
}  #stored in a set

 # Graph end ---------------------------0

 # Main code start -----------------------------------------------------------0

visited = set()

def dfs(graph, visited, root): #Depth first search
    if root not in visited: #if root hasnt been found
        print(root) #print root
        visited.add(root) #add root to make found
        for neighbour in graph[root]: #for every neighbour (passable node) in the graph
            dfs(graph, visited, neighbour) #recall dfs

dfs(graph, visited, 'A') #recall dfs to print 'A'

# Main code end --------------------------------------------------------------0

