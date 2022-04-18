class vertex:
    def __init__(self,key):
        self.id = key
        self.adjKeys = {}

    def addNeighbour(self,nbr, weight):
        self.adjKeys[nbr] = weight



class graph:
    def __init__(self):
        self.verticesList = {}
        self.vertices = 0

    def addVertex(self,key):
        self.vertices += 1
        newvertex = vertex(key)
        self.verticesList[key] = newvertex
        return newvertex

    def addEdge(self, fromvertex, tovertex, weight):
        if fromvertex not in self.verticesList:
            fromNewVertex = self.addVertex(fromvertex)
        if tovertex not in self.verticesList:
            tovNewertex = self.addVertex(tovertex)

        self.verticesList[fromvertex].addNeighbour(tovertex)











