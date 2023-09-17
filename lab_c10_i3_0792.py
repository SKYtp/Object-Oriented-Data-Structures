def findSum(st,size):
    temp = []
    for i in st:
        temp.append(ord(i))
    return int(sum(temp)%int(size))
class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)

class hash:
    def __init__(self,tSize,mCol):
        self.tSize = tSize
        self.mCol = mCol
        self.table = list([None]*tSize)
    def printHash(self):
        for i in range(self.tSize):
            print('#',i+1,'      ',self.table[i],sep='')
    def isFull(self):
        return not(None in self.table)
    def add(self,key,value):
        co = 0
        t = int(findSum(key,self.tSize)) 
        for i in range(self.mCol+1):
            t2 = (t + (i*i))%self.tSize
            if(self.table[t2] == None):
                    self.table[t2] = Data(key,value)
                    break
            else:
                co += 1
                print('collision number',co,'at',t2)
                if(co == self.mCol):
                    print('Max of collisionChain')
                    break
print(' ***** Fun with hashing *****')
inp = input('Enter Input : ').split('/')
tableSize,MaxCol = list(map(int,inp[0].split()))
arr = inp[1].split(',')
H = hash(tableSize,MaxCol)
for i in range(len(arr)):
    k,v = arr[i].split()
    H.add(k,v)
    H.printHash()
    print('---------------------------')
    if(H.isFull()):
        print('This table is full !!!!!!')
        break
    