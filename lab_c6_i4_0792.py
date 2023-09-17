def pantip(k, n, arr, path):
    def printRe(l2):
        if(len(l2) == 1):
            print(l2[0],end='')
            print(' ',end='')
        else:
            printRe(l2[:len(l2)-1])
            print(l2[len(l2)-1],end='')
            print(' ',end='')
    if(len(arr) <= 1):
        if(sum(path+[arr[0]]) == k):
            printRe(path+[arr[0]])
            print()
            return n+1
    else:
        if(sum(path+[arr[0]]) == k):
            printRe(path+[arr[0]])
            print()
            n += 1
        n = pantip(k,n,arr[1:],path+[arr[0]])
        n = pantip(k,n,arr[1:],path)
    return n
inp = input('Enter Input (Money, Product) : ').split('/')
arr = [int(i) for i in inp[1].split()]
pattern = pantip(int(inp[0]), 0, arr, [])
print("Krisada can purchase Product: {0} with: {1} Baht | {2} Pattern".format(arr, inp[0], pattern))