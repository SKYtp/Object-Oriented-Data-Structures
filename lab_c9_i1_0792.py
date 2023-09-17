def bubble(l):
    for last in range(len(l)-1, 0,-1):
        swaped = False
        keep = None
        for i in range(last):
            if l[i] > l[i+1]:
                keep = l[i]
                l[i], l[i+1] = l[i+1], l[i]
                swaped = True
        if not swaped:
            print('last step : ',l,' move[',keep,']',sep='')
            break
        elif(last <= 1):
            print('last step : ',l,' move[',keep,']',sep='')
            break
        else:
            print(int(len(l)-last),' step : ',l,' move[',keep,']',sep='')
inp = [int(i) for i in input('Enter Input : ').split()]
h = list(map(int,inp))
bubble(inp)