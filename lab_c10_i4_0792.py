class hash:
    def __init__(self,tSize,mCol,threshold):
        self.tSize = tSize
        self.mCol = mCol
        self.threshold = threshold
        self.number = 0
        self.table = list([None]*tSize)
    def printHash(self):
        for i in range(self.tSize):
            s = ' '*(7-len(str(i+1)))
            print('#',i+1,s,self.table[i],sep='')
    def reHash(self,arr):
        self.number = 0
        keep = self.tSize * 2
        while(True):
            if(is_prime(keep)):
                break
            keep += 1
        self.tSize = keep
        self.table = [None] * keep
        for i in arr:
            self.add_n(i)
    def isFull(self):
        return not(None in self.table)
    def add(self,value):
        if(float(((self.number+1)/self.tSize)*100) >= self.threshold):
            print('****** Data over threshold - Rehash !!! ******')
            temp = []
            for i in range(self.tSize-1,-1,-1):
                if(self.table[i] != None):
                    temp.append(self.table[i])
            self.reHash(temp)
        co = 0
        t = int(int(value)%self.tSize)
        for i in range(self.mCol+1):
            t2 = (t + (i*i))%self.tSize
            if(self.table[t2] == None):
                    self.table[t2] = value
                    self.number += 1 
                    break
            else:
                co += 1
                print('collision number',co,'at',t2)
                if(co == self.mCol):
                    print('****** Max collision - Rehash !!! ******')
                    temp = []
                    for i in range(self.tSize-1,-1,-1):
                        if(self.table[i] != None):
                            temp.append(self.table[i])
                    self.reHash(temp)
                    self.add_n(value)
                    break 
    def add_n(self,value):
        co = 0
        t = int(int(value)%self.tSize)
        for i in range(self.mCol+1):
            t2 = (t + (i*i))%self.tSize
            if(self.table[t2] == None):
                    self.table[t2] = value
                    self.number += 1  
                    break
            else:
                co += 1
                print('collision number',co,'at',t2)
                if(co == self.mCol):
                    break
def is_prime(n):
    for i in range(2,n):
        if (n%i) == 0:
            return False
    return True
print(' ***** Rehashing *****')
inp = input('Enter Input : ').split('/')
tSize,mCol,threshold = list(map(int,inp[0].split()))
h = hash(tSize,mCol,threshold)
arr = list(map(int,inp[1].split()))
print('Initial Table :')
h.printHash()
print('----------------------------------------')
for i in arr:
    print('Add :',i)
    h.add(i)
    h.printHash()
    print('----------------------------------------')