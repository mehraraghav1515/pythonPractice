class binaryTree():
    def __init__(self,obj):
        self.key = obj
        self.left = None
        self.right = None

    def insertLeft(self,obj):
        if self.left == None:
            self.left = binaryTree(obj)
        else:
            t = binaryTree(obj)
            t.left = self.left
            self.left = t
    def insertRight(self,obj):
        if self.right == None:
            self.right = binaryTree(obj)
        else:
            t = binaryTree(obj)
            t.right = self.left
            self.right = t
    def getRightChild(self):
        return self.right
    def getLeftChild(self):
        return self.left
    def getRootVal(self):
        return  self.key
    def setRootVal(self,obj):
        self.key = obj


r = binaryTree('a')
print(r.getRootVal())
print(r.getLeftChild())
r.insertLeft('b')
print(r.getLeftChild())
print(r.getLeftChild().getRootVal())
r.insertRight('c')
print(r.getRightChild())
print(r.getRightChild().getRootVal())
r.getRightChild().setRootVal('hello')
print(r.getRightChild().getRootVal())







