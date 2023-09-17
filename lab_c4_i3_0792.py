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
q1 = Queue()
q2 = Queue()
st = list(input("Enter code,hint : ").split(','))
code = list(st[0])
hint = str(st[1])
for i in range(len(code)):
    q1.enQueue(code[i])
for i in range(q1.size()):
    k = q1.deQueue()
    if(i == 0):
        op = ord(hint) - ord(k)
        q2.enQueue(hint)
    else:
        q2.enQueue(chr(ord(k)+op))
    print(q2.getQueue())