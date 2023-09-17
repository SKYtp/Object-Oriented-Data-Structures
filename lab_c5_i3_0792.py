class LinkedStack:
    class Node:
        def __init__(self,data,next = None):
            self.data = data
            self.next = next
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    def __len__(self):
        return self.size
    def isEmpty(self):
        return self.size == 0
    def getSize(self):
        return self.size
    def push(self,data):
        self.head = self.Node(data,self.head)
        self.size += 1
    def pop(self):
        if(self.isEmpty()):
            return("list empty")
        temp = self.head.data
        self.head = self.head.next
        self.size -= 1
        return temp
ml  = LinkedStack()
l = LinkedStack()
st = list(input("Enter Input : ").split())
c = 0
for i in st:
    l.push(i)
for i in range(len(l)):
    ml.push(l.pop())
for i in range(len(ml)):
    k = None
    r = 0
    for e in range(len(ml)):
        temp = ml.pop()
        if(k != temp):
            r = 0
        k = temp
        if(k == temp):
            r += 1
        if(r >= 3):
            l.pop()
            l.pop()
            c += 1
            break
        else:
            l.push(temp)
    for i2 in range(len(l)):
        ml.push(l.pop())
for i in range(len(ml)):
    l.push(ml.pop())
print(len(l))
if(l.isEmpty()):
    print("Empty")
else:
    for i in range(len(l)):
        print(l.pop(),sep='',end='')
    print()
if(c >= 2):
    print("Combo :",str(c),"! ! !")