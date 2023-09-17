def search_FGV(arr,x):
    for i in range(len(arr)):
        if(x < arr[i]):
            print(arr[i])
            break
        elif(i >= len(arr)-1):
            print('No First Greater Value')
            break
inp = input('Enter Input : ').split('/')
inp[0] = sorted(list(map(int,inp[0].split())))
inp[1] = list(map(int,inp[1].split()))
for i in inp[1]:
    search_FGV(inp[0],i)
# print(inp)