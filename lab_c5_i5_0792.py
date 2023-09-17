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
                s += str(temp.data)
            else:
                s += ' -> '
                s += str(temp.data)
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
    def getData(self):
        s = ''
        n = self.header
        s += str(n.data)
        while(n.next != None):
            n = n.next
            if(n != None):
                s += ' '
                s += str(n.data)
        return s
    def getDataR(self):
        s = ''
        n = self.header
        while(n.next != None):
            n = n.next
        s += str(n.data)
        while(n.previous != None):
            n = n.previous
            if(n != None):
                s += ' '
                s += str(n.data)
        return s
def get_digit(n,r):
    if(n >= 0):
        n = int(n)
        for i in range(r-1):
            n //= 10
        return n % 10
    else:
        n = int(n)
        n = (n * -1)
        for i in range(r-1):
            n //= 10
        return n % 10
def get_max_digit(n):
    e = 0
    while(n>0):
        n //= 10
        e += 1
    return e
num = list(input("Enter Input : ").split())
rad = [D_LinkedList(),D_LinkedList(),D_LinkedList(),D_LinkedList(),D_LinkedList()\
    ,D_LinkedList(),D_LinkedList(),D_LinkedList(),D_LinkedList(),D_LinkedList()]
radM = [D_LinkedList(),D_LinkedList(),D_LinkedList(),D_LinkedList(),D_LinkedList()\
    ,D_LinkedList(),D_LinkedList(),D_LinkedList(),D_LinkedList(),D_LinkedList()]
ch = True
tran = []
for i in num:
    if(int(i) >= 0):
        tran.append(int(i))
    else:
        tran.append(int(int(i) * -1))
maxD = int(get_max_digit(max(tran)))
Num = D_LinkedList()
kNum = D_LinkedList()    
for i in num:
    Num.append(i)
    kNum.append(i)
for ro in range(maxD):
    print("------------------------------------------------------------")
    print("Round :",(ro + 1))
    for i in range(len(Num)): #get in each
        kn = int(Num.delB())
        if(kn >= 0):
            rad[get_digit(kn,(ro+1))].append(kn)
        else:
            radM[get_digit(kn,(ro+1))].insert(0,kn)
    for i in range(10): #display
        if(not rad[i].isEmpty() and not radM[i].isEmpty()):
            print(i,':',radM[i].getDataR(),rad[i].getData())
        elif(not rad[i].isEmpty() and radM[i].isEmpty()):
            print(i,':',rad[i].getData())
        elif(not radM[i].isEmpty() and rad[i].isEmpty()):
            print(i,':',radM[i].getDataR())
        else:
            print(i,':')
    for i in range(10): #collect
        while(not radM[i].isEmpty()):
            # Num.append(radM[i].delB())
            Num.insert(0,radM[i].delB())
    for i in range(10):
        while(not rad[i].isEmpty()):
            Num.append(rad[i].delB())
for i in range(len(Num)):
        kn = int(Num.delB())
        if(kn >= 0):
            rad[get_digit(kn,(maxD+1))].append(kn)
        else:
            radM[get_digit(kn,(maxD+1))].append(kn)
cn = 0
for i in range(10):
        while(not radM[i].isEmpty()):
            Num.append(radM[i].delB())
for i in range(10):
        while(not rad[i].isEmpty()):
            Num.append(rad[i].delB())
print("------------------------------------------------------------")
print(maxD,"Time(s)")
print("Before Radix Sort :",kNum)
print("After  Radix Sort :",Num)