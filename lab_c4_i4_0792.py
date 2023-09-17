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
st = list(input("Enter Input : ").split('/'))
stF = list(st[0].split(','))
stS = list(st[1].split(','))
ql = []
fDict = {}
fNum = []
for i in range(len(stF)):
    if(stF[i][0] not in fNum):
        fNum.append(stF[i][0])
for i in range(len(fNum)):
    temp = []
    for i1 in range(len(stF)):
        if(fNum[i] == stF[i1][0]):
            temp.append(stF[i1][2:])
    fDict[i] = temp
for i in range(len(stS)):
    if(stS[i][0] == 'E'):
        for i1 in range(len(fDict)):
            if(stS[i][2:] in fDict[i1]):
                if(len(ql) > 0):
                    for i2 in range(len(ql)):
                        if((i1+1) == ql[i2][0]):
                            ql[i2][1].enQueue(stS[i][2:])
                            break
                        elif(i2 == len(ql) - 1):
                            temp = []
                            temp.append(i1+1)
                            temp.append(Queue())
                            temp[1].enQueue(stS[i][2:])
                            ql.append(temp)
                else:
                    temp = []
                    temp.append(i1+1)
                    temp.append(Queue())
                    temp[1].enQueue(stS[i][2:])
                    ql.append(temp)
    elif(stS[i][0] == 'D'):
        if(len(ql) > 0):
            print(ql[0][1].deQueue())
            if(ql[0][1].isEmpty()):
                for i3 in range(len(ql)-1):
                    ql[i3][0] = ql[i3 + 1][0]
                    ql[i3][1] = ql[i3 + 1][1]
                ql.pop(-1)
        else:
            print("Empty")