num = int(input("Enter Input : "))
dot1 = num
h1 = 2
p1 = num+1
dot2 = 1
for i in range(num+1):
    print(".",sep='',end='')
print("#",sep='',end='')
for i in range(num+2):
    print("+",sep='',end='')
print("")
    #------------------------------------#
for i in range(num):
    for i1 in range(dot1):
        print(".",sep='',end='')
    for i2 in range(h1):
        print("#",sep='',end='')
    print("+",sep='',end='')
    for i3 in range(num):
        print("#",sep='',end='')
    print("+",sep='',end='')
    dot1 -= 1
    h1 += 1
    print("")
    #------------------------------------#
for i in range(2):
    for i1 in range(num+2):
        print("#",sep='',end='')
    for i2 in range(num+2):
        print("+",sep='',end='')
    print("")
    #------------------------------------#
for i in range(num):
    print("#",sep='',end='')
    for i1 in range(num):
        print("+",sep='',end='')
    print("#",sep='',end='')
    for i1 in range(p1):
        print("+",sep='',end='')
    for i1 in range(dot2):
        print(".",sep='',end='')
    p1 -= 1
    dot2 += 1
    print("")
    #-------------------------------------#
for i in range(num+2):
    print("#",sep='',end='')
print("+",sep='',end='')
for i in range(num+1):
    print(".",sep='',end='')