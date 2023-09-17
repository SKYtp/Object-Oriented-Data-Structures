def DtoB(n = int,p = int):
    def dTOb(n1 = int,p1 = int):
        if(n1 == 0):
            s = '0'*p1
            print(s,end='')
        elif(n1 // 2 <= 0):
            p2 = p1 - 1
            s = '0'*p2
            if(n1//2 == float(float(n1)/2)):
                print('0',end='')
            else:
                print(str(s),'1',end='',sep='')
        else:
            dTOb(n1//2,p1-1)
            if(n1//2 == float(float(n1)/2)):
                print('0',end='')
            else:
                print('1',end='')
    if(n == 0):
        dTOb(n,p)
        print()
    else:
        DtoB(n-1,p)
        dTOb(n,p)
        print()
inp = int(input('Enter Number : '))
num = 0
if(inp < 0):
    print('Only Positive & Zero Number ! ! !')
elif(inp == 0):
    print('0')
else:
    num = int(pow(2,inp)-1)
    DtoB(num,inp)