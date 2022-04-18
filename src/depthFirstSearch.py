class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight

    # def __str__(self):
    #     return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def __iter__(self):
        return iter(self.connectedTo)

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertList

    def addEdge(self,f,t,weight=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], weight)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())


class implementBreadthFirst:
    def __init__(self):
        self.graph = Graph()
        self.graph.addEdge(0, 1)
        self.graph.addEdge(0, 2)
        self.graph.addEdge(1, 2)
        self.graph.addEdge(2, 0)
        self.graph.addEdge(2, 3)
        self.graph.addEdge(3, 3)
        # self.startingNode  = v


    def dfs(self,v):
        visitedNodes = set()
        self.dfsHelper(v,visitedNodes)

    def dfsHelper(self, v,visitedNodes):
        visitedNodes.add(v)
        # print(getattr(self.graph.vertList[v],'connectedTo'))
        # for i in self.graph.vertList[v].getConnections():
            # print(dir(j))
            # print(i)
        # for i in self.graph.vertList[v].connectedTo:
        #     print(i)
        #     # for j in i.getVertices():
        #     #     print(j)


g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

# print(g.vertList[2].getConnections())


# print(g.vertList[0].getConnections())

bfs = implementBreadthFirst()
bfs.dfs(2)
# for k,v in g.verticesList.items():
#     print(v.getConnections())
#     for j in v.getConnections():
#         print(j)
