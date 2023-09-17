class LinkedQueue:
    class _Node:
        __slot__ = '_element','_next'
        def __init__(self,element,next):
            self._element = element
            self._next = next
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0
    def __len__(self):
        return self._size
    def is_empty(self):
        return self._size == 0
    def first(self):
        if(self.is_empty()):
            return 'Queue is empty'
        return self._head._element
    def dequeue(self):
        if(self.is_empty()):
            return 'Queue is empty'
        answer = self._head
        self._head = self._head._next
        self._size -= 1
        if(self.is_empty()):
            self._tail = None
        return answer._element
    def enqueue(self,e):
        newest = self._Node(e,None)
        if(self.is_empty()):
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1
def getSt(e):
    s = ''
    for i in range(len(e)):
        if(i == (len(e) - 1)):
           s += e[i]
        else:
            s += e[i]
            s += " <- "
    return s
print(" *** Locomotive ***")
num = list(input("Enter Input : ").split())
lq = LinkedQueue()
af = []
for i in num:
    lq.enqueue(i)
for i in range(len(lq)):
    if(lq.first() == '0'):
        break
    else:
        lq.enqueue(lq.dequeue())
for i in range(len(lq)):
    af.append(lq.dequeue())
print("Before : ",getSt(num),sep='')
print("After : ",getSt(af),sep='')