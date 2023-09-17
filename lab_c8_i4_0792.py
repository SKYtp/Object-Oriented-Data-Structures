class Node:
    
    def __init__(self, data): 

        self.data = data  

        self.left = None  

        self.right = None 

        self.level = None 
        
        self.c = None
        
    def __str__(self):

        return str(self.data) 
class Tree:

    def __init__(self):

        self.root = None

        self.num = 0
    def insert(self, val):  

        if self.root == None:

            self.root = Node(val)
            self.root.c = self.num
            self.num += 1

        else:

            h = height(self.root)

            max_node = pow(2,h+1)-1

            current = self.root

            if self.num+1 > max_node:

                while(current.left != None):

                    current = current.left

                current.left = Node(val)
                current.left.c = self.num
                self.num+=1

            elif self.num+1 == max_node:

                while(current.right != None):

                    current = current.right

                current.right = Node(val)
                current.right.c = self.num
                self.num+=1

            else:

                max_node-((max_node-(pow(2,h)-1))/2)

                if self.num+1 <= max_node-((max_node-(pow(2,h)-1))/2):

                    insert_subtree(current.left,self.num - round(pow(2,h)/2),val,self.num)

                else:

                    insert_subtree(current.right,self.num - pow(2,h),val,self.num)

                self.num+=1
                    

def insert_subtree(r,num,val,nums):

    if r != None:

        h = height(r)

        max_node = pow(2,h+1)-1

        current = r

        if num+1 > max_node:

            while(current.left != None):

                current = current.left

            current.left = Node(val)
            current.left.c = nums
            return

        elif num+1 == max_node:

            while(current.right != None):

                current = current.right

            current.right = Node(val)
            current.right.c = nums
            return

        if num+1 <= max_node-((max_node-(pow(2,h)-1))/2):

            insert_subtree(current.left,num - round(pow(2,h)/2),val,nums)

        else:

            insert_subtree(current.right,num - pow(2,h),val,nums)

    else:

        return



def height(root):

    if root == None:

        return -1

    else:

        left = height(root.left)

        right = height(root.right)

        if left>right:

            return left + 1

        else:

            return right + 1
def sumTree(node):
    if(node == None):
        return 0
    else:
        temp = sumTree(node.left) + sumTree(node.right)
        temp += int(node.data)
        return temp
def getCNode(node,num):
    if(node == None):
        return 
    elif(int(node.c) == int(num)):
        return node
    else:
        nl = getCNode(node.left,num)
        nr = getCNode(node.right,num)
        if(nl == None and nr != None):
            return nr
        elif(nl != None and nr == None):
            return nl
        else:
            return
        
def printTree90(node, level = 0):

    if node != None:

        printTree90(node.right, level + 1)

        print('     ' * level, node)

        printTree90(node.left, level + 1)
tree = Tree()
data = input("Enter Input : ").split('/')
data[0] = list(data[0].split())
for e in data[0]:
    tree.insert(int(e))
data[1] = data[1].split(',')
print(sumTree(tree.root))
for i in data[1]:
    g1,g2 = i.split()
    d1 = int(sumTree(getCNode(tree.root,g1)))
    d2 = int(sumTree(getCNode(tree.root,g2)))
    if(d1 > d2):
        print(g1,'>',g2,sep='')
    elif(d1 < d2):
        print(g1,'<',g2,sep='')
    else:
       print(g1,'=',g2,sep='')