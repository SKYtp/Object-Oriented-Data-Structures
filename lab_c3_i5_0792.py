class Stack :
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
def dec2bin(decnum):
    s = Stack()
    num = float(decnum)
    bi = ""
    while(num >= 1):
        num = float(num / 2)
        if(num//1 == num/1):
            s.push('0')
        else:
            s.push('1')
        num = int(num)
    for e in range(s.size()):
        bi += s.pop()
    return bi
    
print(" ***Decimal to Binary use Stack***")
token = input("Enter decimal number : ")
print("Binary number : ",end='')
print(dec2bin(int(token)))