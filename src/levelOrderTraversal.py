class Node():
    def __init__(self,key):
        self.val = key
        self.left = None
        self.right = None


    def printAllNodes(self,root):
        print(self.heightTree(root))
        for i in range(1,self.heightTree(root)+1):
            self.printCurrentValue(root,i)


    def printCurrentValue(self,root,level):
        if root == None:
            return
        if level == 1:
            print(root.val,end=" ")
        elif level > 1:
            self.printCurrentValue(root.left,level-1)
            self.printCurrentValue(root.right,level-1)


    def heightTree(self,root):
         if root is None:
             return 0
         else:
             lheight = self.heightTree(root.left)
             rheight = self.heightTree(root.right)

         if lheight > rheight:
             return lheight + 1
         else:
             return rheight + 1


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Level order traversal of binary tree is -")
root.printAllNodes(root)



