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
def closestValue(root,value):
    return closestValueRe(root, value, root.data)

def closestValueRe(root, value, closest):
	if root is None:
		return closest
	if abs(closest - value) > abs(root.data - value):
		closest = root.data
	if value < root.data:
		return closestValueRe(root.left, value, closest)
	elif value > root.data:
		return closestValueRe(root.right, value, closest)
	else:
		return closest
T = BST()
inp = list(input('Enter Input : ').split('/'))
inp1 = [int(i) for i in inp[0].split()]
inp2 = int(inp[1])
for i in inp1:
   root = T.insert(i)
   T.printTree(root)
   print('--------------------------------------------------')
print('Closest value of',inp2,':',closestValue(root,inp2))