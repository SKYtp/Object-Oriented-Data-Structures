class Stack:
    def __init__(self):
        self.items = []
    def push(self,i):
        self.items.append(i)
    def getQueue(self):
        return self.items
    def pop(self):
        return self.items.pop()
    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items)
    def reverse(self):
        self.items.reverse()
class Queue:
    def __init__(self):
        self.items = []
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
    def reverse(self):
        self.items.reverse()
st = list(input("Enter Input (Normal, Mirror) : ").split())
mi = Stack()
miI = Queue()
nor = list(st[0])
k1 = []
k2 = []
x = 0
it = 0
fa = 0
for i in range(len(st[1])):
    mi.push(st[1][i])
k1 = mi.getQueue()
k1.reverse()
#get item
for i in range(len(k1)):
    for i1 in range(len(k1) - 2):              
        if(len(k1) >= 3):                
            if(k1[i1] == k1[i1+1] == k1[i1+2]):
                miI.enQueue(k1.pop(i1))
                k1.pop(i1)
                k1.pop(i1)
                it += 1
                break
# use item
for i in range(miI.size()):
    for i1 in range(len(nor) - 2):
        if(len(nor) >= 3):
          if(nor[i1] == nor[i1+1] == nor[i1+2]):
                if(not miI.isEmpty()):
                    nor.insert((i1+2),miI.deQueue())
                    if(nor[i1] == nor[i1+1] == nor[i1+2]):
                        nor.pop(i1)
                        nor.pop(i1)
                        nor.pop(i1)  
                        fa += 1 
                    break
#boom
for i in range(len(nor)):
    for i1 in range(len(nor) - 2):
        if(nor[i1] == nor[i1+1] == nor[i1+2]):
            nor.pop(i1)
            nor.pop(i1)
            nor.pop(i1)
            x += 1 
            break
nor.reverse()
k1.reverse()
print("NORMAL :")
print(len(nor))
if(nor != []):
    for i in nor:
        print(i,sep='',end='')
    print()
else:
    print("Empty")
print(x,"Explosive(s) ! ! ! (NORMAL)")
if(fa != 0):
    print("Failed Interrupted",fa,"Bomb(s)")
print("------------MIRROR------------")
print(": RORRIM")
print(len(k1))
if(k1 != []):
    for i in k1:
        print(i,sep='',end='')
    print()
else:
    print("ytpmE")
print("(RORRIM) ! ! ! (s)evisolpxE",it)