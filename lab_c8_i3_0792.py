class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


class roughTree:
    def __init__(self):
        self.root = None

    def create_complete_tree(self, n, value):
        self.root = Node('*')
        queue = [self.root]
        temp_n = n
        n -= 1
        while True:
            node = queue.pop(0)

            if n > int(temp_n/2)+1:
                node.left = Node('*')
            else:
                node.left = Node(value.pop(0))
            n -= 1
            if n == 0:
                break
            queue.append(node.left)

            if n > int(temp_n/2)+1:
                node.right = Node('*')
            else:
                node.right = Node(value.pop(0))
            n -= 1
            if n == 0:
                break
            queue.append(node.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            if root.left and root.right:
                if root.left.data > root.right.data:
                    root.data = root.right.data
                else:
                    root.data = root.left.data
                root.left.data -= root.data
                root.right.data -= root.data

    def findsum(self, root, data):
        if root:
            data = self.findsum(root.left, data)
            data = self.findsum(root.right, data)
            data += root.data
        return data


inp = input("Enter Input : ").split('/')
inp[1] = inp[1].split()
inp[0], inp[1] = int(inp[0]), list(map(int, inp[1]))
tree = roughTree()
if (int(inp[0]/2))+1 != len(inp[1]):
    print("Incorrect Input")
    exit()
tree.create_complete_tree(inp[0], inp[1])
tree.postorder(tree.root)
print(tree.findsum(tree.root, 0))