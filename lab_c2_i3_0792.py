def range(start,stop = None,step = 1):
    start = float(start)
    if(stop == None):
        s = 0.0
        list = []
        while(s<start):
            if(s//1 == s/1): 
                list.append(round(s, 1))
            else:
                list.append(float(('%f' % s).rstrip('0').rstrip('.')))
            s += float(step)
        list = tuple(list)
        return list
    else:
        s = float(start)
        list = []
        while(s<float(stop)):
            if(s//1 == s/1): 
                list.append(round(s, 1))
            else:
                list.append(float(('%f' % s).rstrip('0').rstrip('.')))
            s += float(step)
        list = tuple(list)
        return list
print("*** New Range ***")
num = input("Enter Input : ").split()
if(len(num) == 1):
    print(range(num[0]))
elif(len(num) == 2):
    print(range(num[0],num[1]))
else:
    print(range(num[0],num[1],num[2]))