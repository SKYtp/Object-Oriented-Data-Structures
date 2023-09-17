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
st = list(input("Enter people : "))
qm = Queue()
q1 = Queue()
q2 = Queue()
for i in range(len(st)):
    qm.enQueue(st[i])
c1 = -1
c2 = 0
stc = 0
for i in range(qm.size()):
    c1 += 1
    if(not q2.isEmpty()):
        c2 += 1
    if(c1 == 3 and not q1.isEmpty()):
        q1.deQueue()
        c1 = 0
    if(c2 == 2 and not q2.isEmpty()):
        q2.deQueue()
        c2 = 0
    if(q1.size() < 5):
        q1.enQueue(qm.deQueue())
    elif(q2.size() < 5):
        q2.enQueue(qm.deQueue())
    stc += 1
    print(stc,end='')
    print('',qm.getQueue(),end='')
    print('',q1.getQueue(),'',end='')
    print(q2.getQueue())