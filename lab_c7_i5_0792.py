class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None  
    def __str__(self):
        return str(self.data)
class BST:
    def __init__(self):
        self.root = None
    def get(self):
        return self.root
    def search(self,key):
        return
    def _search(root,key):
        if(root is None or root.data == key):
            return root
        if(int(root.data) < int(key)):
            return BST._search(root.right,key)
        else:
            return BST._search(root.left,key)
    def insert(self, data):
        self.root = BST._insert(self.root,data)
        return self.root
    def _insert(root,data):
        if(root is None):
            return Node(data)
        else:
            if(data<root.data):
                root.left = BST._insert(root.left,data)
            else:
                root.right = BST._insert(root.right,data)
        return root
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
    def checkpos(self,key):
        if(int(root.data) == int(key)):
            print("Root")
        else:
            BST._checkpos(self.root,key)
    def _checkpos(root,key):
        if(root is None or int(root.data) == int(key)):
            if(root is not None):
                if(int(root.data) == int(key)):
                    if(root.left is not None or root.right is not None):
                        print("Inner")
                        return False
                    elif(root.left is None and root.right is None):
                        print("Leaf")
                        return False
            print("Not exist")
            return
        if(int(root.data) < int(key)):
            BST._checkpos(root.right,key)
        else:
            BST._checkpos(root.left,key)
T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in range(1, len(inp)):
    root = T.insert(inp[i])
T.printTree(root)
T.checkpos(inp[0])