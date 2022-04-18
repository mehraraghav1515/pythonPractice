"""Python3 program to find n-th node of
Postorder Traversal of Binary Tree"""


# A Binary Tree Node
# Utility function to create a new tree node
class createNode:

    # Constructor to create a newNode
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


    def NthPostordernode(self,root, N):
        self.MainArray = []
        self.traverseTreePostorder(root)
        return self.MainArray[N+1]


    def  traverseTreePostorder(self,root):
        if root:
            self.traverseTreePostorder(root.left)
            self.MainArray.append(root.data)
            self.traverseTreePostorder(root.right)






# Driver Code
if __name__ == '__main__':
    root = createNode(25)
    root.left = createNode(20)
    root.right = createNode(30)
    root.left.left = createNode(18)
    root.left.right = createNode(22)
    root.right.left = createNode(24)
    root.right.right = createNode(32)

    abc = root.NthPostordernode(root, 4)
    print(abc)

