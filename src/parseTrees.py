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

class stack():
    def __init__(self):
        self.stackList = []
    def push(self,element):
        self.stackList.append(element)
    def pop(self):
        return self.stackList.pop()


def buildParseTrees(fpexp):
    fplist = fpexp.split()
    pstack = stack()
    etree = binaryTree('')
    pstack.push(etree)
    currentTree =etree

    for i in fplist:
        if i == '(':
            currentTree.insertLeft('')
            pstack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i in ['+','-','*','/']:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pstack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif i == ')':
            currentTree = pstack.pop()
        elif i not in ['+', '-', '*', '/', ')']:
            try:
                currentTree.setRootVal(int(i))
                parent = pstack.pop()
                currentTree = parent
            except ValueError:
                raise ValueError("token not a value integer")
    return etree

pt = buildParseTrees("( ( 10 + 5 ) * 3 )")

