class vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}

    def addNeighbour(self, nbr, weight ):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]


class graph:
    def __init__(self,id):
        self.numberOfvertices = 0
        self.verticesLists = {}
    def addVertex(self,vertex):
        v = vertex(vertex)
        self.numberOfvertices += 1
        self.verticesLists[vertex] = v
        return v
    def addEdge(self,fromVert, toVert, weight):
        if fromVert not in self.verticesLists:
            nv = self.addVertex(fromVert)

        if toVert not in self.verticesLists:
            fv = self.addVertex(toVert)

        self.verticesLists[fromVert].addNeighbour






