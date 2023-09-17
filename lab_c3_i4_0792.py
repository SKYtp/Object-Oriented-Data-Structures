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
class StackCalc:
    s = Stack()
    p = False
    def run(self,ls):
        self.ls = ls.split()
        o = ['+','-','*','/','DUP','POP','PSH']
        for e in self.ls:
            if(e in o):
                if(e == '+'):
                    b = float(StackCalc.s.pop())
                    a = float(StackCalc.s.pop())
                    StackCalc.s.push(a + b)
                elif(e == '-'):
                    StackCalc.s.push(float(StackCalc.s.pop()) - float(StackCalc.s.pop()))
                elif(e == '*'):
                    b = float(StackCalc.s.pop())
                    a = float(StackCalc.s.pop())
                    StackCalc.s.push(a * b)
                elif(e == '/'):
                    StackCalc.s.push(float(StackCalc.s.pop()) / float(StackCalc.s.pop()))
                elif(e == 'DUP'):
                    a = float(StackCalc.s.pop())
                    StackCalc.s.push(a)
                    StackCalc.s.push(a)
                elif(e == 'POP'):
                    StackCalc.s.pop()
                    
                #else:
            elif(e.isnumeric()):
                StackCalc.s.push(e)
            else:
                StackCalc.p = True
                self.k = e
                break
    def getValue(self):
        if(StackCalc.p):
            return "Invalid instruction: " + self.k 
        elif(StackCalc.s.isEmpty()):
            return 0   
        else:
            a = float(StackCalc.s.pop())
            if(a//1 == a/1):
                return int(a)
            else:
                return float(('%f' % float(a)).rstrip('0').rstrip('.'))
            
print("* Stack Calculator *")
arg = input("Enter arguments : ")
machine = StackCalc()
machine.run(arg)
print(machine.getValue())