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
        if(self.isEmpty()):
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
    def str_reverse(self):
        if(self.isEmpty()):
            return ''
        s = ''
        temp = self.header
        while(temp.next is not None):
            temp = temp.next
        for i in range(self.size):
            if(i == 0):
                s += temp.data
            else:
                s += '->'
                s += temp.data
            temp = temp.previous        
        return s
    def remove(self, data):
        inD = 0
        if(self.header is None):
            return "Not Found!"
        if(self.header.next is None):
            if(self.header.data == data):
                self.header = None
                self.size -= 1
                inD = 0
            else:
                return "Not Found!"
            return "removed : "+data+" from index : "+str(inD)
        if(self.header.data == data):
            self.header = self.header.next
            self.header.previous = None
            self.size -= 1
            inD = 0
            return "removed : "+data+" from index : "+str(inD)
        n = self.header
        inD = 0
        while n.next is not None:
            if(n.data == data):
                break
            n = n.next
            inD += 1
        if(n.next is not None):
            n.previous.next = n.next
            n.next.previous = n.previous
            self.size -= 1
        else:
            if(n.data == data):
                n.previous.next = None
                self.size -= 1
            else:
                return 'Not Found!'
        return "removed : "+data+" from index : "+str(inD)
dl = D_LinkedList()
st = input("Enter Input : ")
st = st.replace(' ', '')
st = list(st.split(','))
c = True
for i in st:
    if(i[:2] == 'Ab'):
        if(len(i) > 2):
            dl.insert(0,i[2:])
    elif(i[0] == 'A'):
        if(len(i) > 1):
            dl.append(i[1:])
    elif(i[0] == 'I'):
        if(len(i) > 1):
            if(':' in i):
                temp = i[1:].split(':')
                print(dl.insert(int(temp[0]),temp[1]))
    elif(i[0] == 'R'):
        if(len(i) > 1):
            print(dl.remove(i[1:]))  
    print("linked list :",dl)
    print("reverse :",dl.str_reverse())