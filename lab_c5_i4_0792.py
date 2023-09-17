class D_LinkedList:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
            self.previous = None
    def __init__(self):
        self.header = None
        self.size = 0
    def __str__(self):
        if(self.size == 0):
            return ''
        s = ''
        temp = self.header
        g = True
        for i in range(self.size):
            if(i == 0):
                s += temp.data
            else:
                s += '->'
                s += temp.data
            temp = temp.next
        return s
    def __len__(self):
        return self.size
    def isEmpty(self):
        return self.size == 0
    def insert(self, index, data):
        if(index < 0):
            return "Data cannot be added"
        if(self.isEmpty()):
            if(index == 0):
                self.header = self.Node(data)
                self.size += 1
                return "index = "+str(index)+" and data = "+str(data)
            return "Data cannot be added"
        if(index == 0):
            temp = self.Node(data)
            temp.next = self.header
            self.header.previous = temp
            self.header = temp
            self.size += 1
            return "index = "+str(index)+" and data = "+str(data)
        if(index == self.size and self.size != 0):
            self.append(data)
            return "index = "+str(index)+" and data = "+str(data)
        if(index > (self.size - 1)):
            return "Data cannot be added"
        temp = self.Node(data)
        n = self.header
        for i in range(index):
            n = n.next
        temp.previous = n.previous
        n.previous.next = temp
        temp.next = n
        n.previous = temp
        self.size += 1
        return "index = "+str(index)+" and data = "+str(data)
    def append(self, data):
        if(self.header is None):
            newest = self.Node(data)
            self.header = newest
            self.size += 1
            return
        n = self.header
        while(n.next is not None):
            n = n.next
        newest = self.Node(data)
        n.next = newest
        newest.previous = n
        self.size += 1
    def delB(self):
        if(self.isEmpty()):
            return
        if(self.header.next == None):
            temp = self.header.data
            self.header = None
            self.size -= 1
            return temp
        temp = self.header.data
        self.header.next.previous = None
        self.header = self.header.next
        self.size -= 1
        return temp
    def delD(self):
        if(self.isEmpty()):
            return
        if(self.size == 1):
            temp = self.header.data
            self.header = None
            self.size -= 1
            return temp
        n = self.header
        while(n.next != None):
            n = n.next
        temp = n.data
        n.previous.next = None
        self.size -= 1
        return temp
ml = D_LinkedList()
l = D_LinkedList()
st = list(input("Enter Input : ").split(','))
for i in st:
    if(i[0] == 'I'):
        ml.append(i[2:])
    elif(i[0] == 'L'):
        if(not ml.isEmpty()):
            l.insert(0,ml.delD())
    elif(i[0] == 'R'):
        if(not l.isEmpty()):
            ml.append(l.delB())
    elif(i[0] == 'B'):
        if(not ml.isEmpty() or not l.isEmpty()):
            if(not ml.isEmpty()):
                ml.delD()
    elif(i[0] == 'D'):
        if(not ml.isEmpty() or not l.isEmpty()):
            if(not l.isEmpty()):
                l.delB()
for i in range(len(ml)):
    print(ml.delB(),'',end='')
print('| ',end='')
for i in range(len(l)):
    print(l.delB(),'',end='')