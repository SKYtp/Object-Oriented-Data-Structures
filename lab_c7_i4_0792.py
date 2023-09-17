class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None    
    def __str__(self):
        return str(self.data)
    def getData(self):
        return self.data
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
    def levelOrder(self):
        q = Queue()
        q.enQueue(self.root)
        while(q.isEmpty() is not True):
            n = q.deQueue()
            print(n.data,end=' ')
            if(n.left is not None):
                q.enQueue(n.left)
            if(n.right is not None):
                q.enQueue(n.right)
    def inOrder(self):
        BST._inOrder(self.root)
    def _inOrder(root):
        if(root is not None):
            BST._inOrder(root.left)
            print(root.data,end=' ')
            BST._inOrder(root.right)
    def preOrder(self):
        BST._preOrder(self.root)
    def _preOrder(root):
        if(root is not None):
            print(root.data,end=' ')
            BST._preOrder(root.left)
            BST._preOrder(root.right)
    def postOrder(self):
        BST._postOrder(self.root)
    def _postOrder(root):
        if(root is not None):
            BST._postOrder(root.left)
            BST._postOrder(root.right)
            print(root.data,end=' ')
class Queue:
    def __init__(self):
        self.items = []
    def __str__(self):
        return self.items
    def getQueue(self):
        return self.items
    def enQueue(self,i):
        self.items.append(i)
    def deQueue(self):
        return self.items.pop(0)
    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items)
T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
   root = T.insert(i)
print('Preorder : ',end='')
T.preOrder()
print()
print('Inorder : ',end='')
T.inOrder()
print()
print('Postorder : ',end='')
T.postOrder()
print()
print('Breadth : ',end='')
T.levelOrder()