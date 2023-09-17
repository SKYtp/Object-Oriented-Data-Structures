def bubble_C(a):
    global co
    for last in range(len(a)-1, 0,-1):
        swaped = False
        for i in range(last):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                swaped = True
        if(swaped):
            co += 1
        if not swaped:
            if(last != 1):
                co += 1
            break
        
def bubble(l):
    global c
    global co
    ce = True
    for last in range(len(l)-1, 0,-1):
        swaped = False
        keep = None
        for i in range(last):
            if l[i] > l[i+1]:
                keep = l[i]
                l[i], l[i+1] = l[i+1], l[i]
                swaped = True
        if not swaped:
            if(last != 1):
                print('last step : ',l,' move[',keep,']',sep='')
            break
        if(co == 0):
            co = 1
        if(co == c):
            print('last step : ',l,' move[',keep,']',sep='')
        else:
            print(c,' step : ',l,' move[',keep,']',sep='')
        c += 1
c = 1
co = 0
inp = [int(i) for i in input('Enter Input : ').split()]
h = list(map(int,inp))
bubble_C(h)
bubble(inp)