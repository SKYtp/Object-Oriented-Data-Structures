def selection(l):
    for last in range(len(l)-1, 0, -1):
        biggest = l[0]
        biggest_i = 0
        if(l[last] >= 0):
            for i in range(1, last+1):
                if l[i] > biggest:
                    biggest = l[i]
                    biggest_i = i
            l[last], l[biggest_i ] = l[biggest_i], l[last]
inp = [int(i) for i in input('Enter Input : ').split()]
selection(inp)
for i in inp:
    print(i,end=' ')