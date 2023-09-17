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
    def getRoot(self):
        return self.root
def searchResult(root,key):
    global keep
    if(root != None):
        searchResult(root.right,key)
        if(root.data <= int(key)):
            keep += 1
        searchResult(root.left,key)
T = BST()
inp1 = list(input('Enter Input : ').split('/'))
inp2 = [int(i) for i in inp1[0].split()]
inp3 = int(inp1[1])
for i in inp2:
   root = T.insert(i)
T.printTree(root)
keep = 0
searchResult(root,inp3)
print('--------------------------------------------------')
print(keep)