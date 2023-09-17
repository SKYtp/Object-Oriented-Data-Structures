print("*** Fun with Drawing ***")
num = int(input("Enter input : "))
sw1 = True
x = num #input
i = x + (x-1)
j = 1
s = 0
d = 3
use = ["#","."]
sw2 = 0
for n in range(1,i):
    j+=2
for n in range(0,i):
    sw2 = 0
    for k in range(s):
        print(use[sw2],sep='',end='')
        if(sw2 == 0):
            sw2 = 1
        else:
            sw2 =0
    for m in range(0,j):
        if(sw1):
            print("#",sep='',end='')
        else:
            print(".",sep='',end='')
    if((s%2) == 0):
        sw2 = 1
    else:
        sw2 = 0
    for k in range(s):
        print(use[sw2],sep='',end='')
        if(sw2 == 0):
            sw2 = 1
        else:
            sw2 =0
    if(sw1):
        sw1 = False
    else:
        sw1 = True
    j -= 2
    s += 1  
    print("")
#-------------------------------------------#
sw1 = False
s -= 2
for g in range(0,i-1):
    sw2 = 0
    for vb in range(s):
        print(use[sw2],sep='',end='')
        if(sw2 == 0):
            sw2 = 1
        else:
            sw2 =0
    for m in range(0,d):
        if(sw1):
            print("#",sep='',end='')
        else:
            print(".",sep='',end='')
    if((s%2) == 0):
        sw2 = 1
    else:
        sw2 = 0
    for vb in range(s):
        print(use[sw2],sep='',end='')
        if(sw2 == 0):
            sw2 = 1
        else:
            sw2 =0
    if(sw1):
        sw1 = False
    else:
        sw1 = True
    d += 2
    s -= 1
    print("")