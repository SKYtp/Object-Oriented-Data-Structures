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
    def insert(self, data):
        self.root = BST._insert(self.root,data)
        return self.root
    def _insert(root,data):
        if(root is None):
            print('*')
            return Node(data)
        else:
            if(data<root.data):
                print('L',end='')
                root.left = BST._insert(root.left,data)
            else:
                print('R',end='')
                root.right = BST._insert(root.right,data)
        return root
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
   root = T.insert(i)