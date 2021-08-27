"""
test data:

                     1 ---> node
                  /  |  \  
                6    1    5 ---> weight
              /      |      \
             2---5---3---7---4
             \     /  \     /
              3   5    4   2
               \ /      \ /
                5---6----6
"""

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [set() for i in range(self.V)]
        self.adjacentMatrix = [[0 for i in range(self.V)] for i in range(self.V)]
    
    def addEdge(self,src,des, weight):
        src-=1 #source
        des-=1 #destination
        self.adjacentMatrix[src][des] = weight
        self.graph[src].add(des)
        self.graph[des].add(src)

    
    def printGraph(self):
        for i in range(len(self.graph)):
            print("vertex: ",i+1)
            print("head ",end="")
            for j in self.graph[i]:
                print("-> {}".format(j+1),end=" ")
            print()


    def printMatrix(self):
        for i in range(len(self.adjacentMatrix)):
            for j in self.adjacentMatrix[i]:
                print(j,end=" ")
            print("\n")


    def printBFS(self,startingNode):
        startingNode-=1
        queue = []
        visited = [False]*self.V
        queue.append(startingNode)
        visited[startingNode] = True

        while len(queue) >0:
            # print(queue)
            v = queue.pop(0)
            print((v+1), end=" ")
            
            for i in self.graph[v]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True

    
    def printDFS(self,startingNode):
        startingNode-=1
        stack = []
        visited = [False]*self.V
        stack.append(startingNode)
        visited[startingNode] = True

        while len(stack) >0:
            # print(stack)
            v = stack.pop()
            print((v+1), end=" ")
            
            for i in self.graph[v]:
                if not visited[i]:
                    stack.append(i)
                    visited[i] = True

    def MST(self):
        visited = [False]*self.V
        visited[0] = True
        num_of_edges = 0
        minimumCost = 0

        while num_of_edges < self.V -1:
            minimum = 999999
            x = 0
            y = 0
            for i in range(self.V):
                if visited[i]:
                    for j in range(self.V):
                        if self.adjacentMatrix[i][j] !=0 and not visited[j]:
                            if minimum > self.adjacentMatrix[i][j]:
                                minimum = self.adjacentMatrix[i][j]
                                x=i
                                y=j
            num_of_edges+=1
            visited[y] = True
            minimumCost+=minimum
            print(str(x+1) + "-" + str(y+1) + " : " + str(self.adjacentMatrix[x][y]))
        print("Total minimum cost: ", minimumCost)

# this is different graph data
graph = Graph(7)

graph.addEdge(0,1,28)
graph.addEdge(0,5,10)
graph.addEdge(1,2,16)
graph.addEdge(1,6,14)
graph.addEdge(1,0,28)
graph.addEdge(5,0,10)
graph.addEdge(5,4,25)
graph.addEdge(6,1,14)
graph.addEdge(6,3,18)
graph.addEdge(6,4,24)
graph.addEdge(2,1,16)
graph.addEdge(2,3,12)
graph.addEdge(4,3,22)
graph.addEdge(4,5,25)
graph.addEdge(4,6,24)
graph.addEdge(3,2,12)
graph.addEdge(3,4,22)
graph.addEdge(3,6,18)



print("Adjacent List")
print('-------------')
graph.printGraph()
print("\nAdjacent Matrix: ")
print('----------------')
graph.printMatrix()
print("BFS: ", end = "")
graph.printBFS(6)
print("\nDFS: ", end = "")
graph.printDFS(6)
print("\n\n\nMinimum Spanning Tree")
print('---------------------')
graph.MST()