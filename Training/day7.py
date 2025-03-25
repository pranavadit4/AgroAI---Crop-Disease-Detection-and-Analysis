#graphs

#what is a graph

    #a graph is a collection of nodes(vertices) and edges connecting them
    #real life examples:
        #social networks(facebook,linkedin)
        #google maps
        #web crawling

#graph representation

    #Adacency list:
        #each node stores its neighbour
        #efficient for sparse graphs

    #adj matrix:
        #uses a 2d array where matrix[i][j] = 1 if an edge exists
        #efficient for dense graphs

#graph traversal

    #traversal is visiting all nodes in the systematic way.

    #two ways:
        #BFS(Breath first search):
            #level by level exploration
        #DFS(Depth first search):
            #deepest path exploration first

#Breath first search

def bfs(graph,start):
    visit = set()
    queue = [start]
    visit.add(start)
    while queue:
        node = queue.pop(0)
        print(node, end='')
        for i in graph[node]:
            if i not in visit:
                visit.add(i)
                queue.append(i)
graph = {0:[1,4],
         1:[0,2],
         2:[1,3],
         3:[2,4],
         4:[3,0]}
bfs(graph,0)

#Depth first search






