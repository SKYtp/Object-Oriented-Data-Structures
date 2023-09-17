class Queue:
    def __init__(self):
        self.items = []
    def enQueue(self,i):
        self.items.append(i)
    def deQueue(self):
        return self.items.pop(0)
    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items)
q = Queue()
l = list(input("Enter Input : ").split(','))
ls = []
for i in l:
    ls.append(i.split())
for i in ls:
    if(i[0] == 'E'):
        a = str(q.size())
        q.enQueue(i[1])
        print("Add "+i[1]+" index is "+a)
    elif(i[0] == 'D'):
        if(q.size() == 0):
            print("-1")
        else:
            print("Pop "+q.deQueue()+" size in queue is "+str(q.size()))
if(q.isEmpty()):
    print("Empty")
else:
    c = []
    for e in range(q.size()):
        c.append(q.deQueue())
    print("Number in Queue is :  ",sep='',end='')
    print(c)