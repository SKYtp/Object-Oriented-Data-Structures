class Stack:
    def __init__(self):
        self.items = []
    def push(self,i):
        self.items.append(i)
    def pop(self):
        return self.items.pop()
    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items)
l = list(input("Enter Input : ").split(','))
ls = []
s = Stack()
for i in l:
    ls.append(i.split())
for i in ls:
    if(len(i) == 2):
        if(i[0] == 'A'):
            print("Add =",i[1])
            s.push(int(i[1]))
        elif(i[0] == 'D'):
            if(s.isEmpty()):
                print(-1)
            else:
                t = Stack()
                for e in range(s.size()):
                    a = int(s.pop())
                    if(int(i[1]) == a):
                        print("Delete =",a)
                    else:
                        t.push(int(a))
                while(not t.isEmpty()):
                    s.push(t.pop())
        elif(i[0] == 'LD'):
            if(s.isEmpty()):
                print(-1)
            else:
                t = Stack()
                for e in range(s.size()):
                    a = int(s.pop())
                    if(a < int(i[1])):
                        print("Delete =",str(a),"Because",str(a),"is less than",i[1])
                    else:
                        t.push(int(a))
                while(not t.isEmpty()):
                    s.push(t.pop())
        elif(i[0] == 'MD'):
            if(s.isEmpty()):
                print(-1)
            else:
                t = Stack()
                for e in range(s.size()):
                    a = int(s.pop())
                    if(a > int(i[1])):
                        print("Delete =",str(a),"Because",str(a),"is more than",i[1])
                    else:
                        t.push(int(a))
                while(not t.isEmpty()):
                    s.push(t.pop())
    else:
        if(i[0] == 'P'):
            if(s.isEmpty()):
                print(-1)
            else:
                print("Pop =",str(s.pop()))
print("Value in Stack = "+str(s.items))