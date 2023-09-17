def bubble(l,di):
    for last in range(len(l)-1, 0,-1):
        swaped = False
        for i in range(last):
            if (di[l[i]] > di[l[i+1]]):
                l[i], l[i+1] = l[i+1], l[i]
                swaped = True
        if not swaped:
            break
inp = input('Enter Input : ').split()
d1 = dict()
for i in inp:
    for j in i:
        if(j.isalpha()):
            d1.update({i : int(ord(j))})
bubble(inp,d1)
for i in inp:
    print(i,' ',end='',sep='')