class Stack():
    def __init__(self, ls = None):
        if(ls == None):
            self.ls = []
        else:
            self.ls = ls
    def push(self,i):
        self.ls.append(i)
    def pop(self):
        return self.ls.pop()
    def isEmpty(self):
        return self.ls == []
    def size(self):
        return len(self.ls)
def postFixeval(st):
    s = Stack()
    o = ['+','-','*','/']
    for e in st:
        if e in o:
            if(e == '+'):
                b = float(s.pop())
                a = float(s.pop())
                s.push(a + b)
            elif(e == '-'):
                b = float(s.pop())
                a = float(s.pop())
                s.push(a - b)
            elif(e == '*'):
                b = float(s.pop())
                a = float(s.pop())
                s.push(a * b)
            else:
                b = float(s.pop())
                a = float(s.pop())
                s.push(a / b)
        else:
            s.push(e)
    return s.pop()
print(" ***Postfix expression calcuation***")
token = list(input("Enter Postfix expression : ").split())
print("Answer : ",'{:.2f}'.format(postFixeval(token)))