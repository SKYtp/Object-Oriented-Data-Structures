def insertionSort(arr,p,c):
    def insertionSort_2(arr,key,j):
        if(j < 0 or key >= arr[j]):
            return j
        else:
            arr[j+1] = arr[j]
            return insertionSort_2(arr,key,j-1)
    if(p >= len(arr)):
        return
    else:
        key = arr[p]
        j = p-1
        i = insertionSort_2(arr,key,j)
        arr[i+1] = key
        if(c < len(arr)):
            print('insert ',key,' at index ',i+1,' : ',arr[:c],' ',arr[c:],sep='')
        else:
            print('insert ',key,' at index ',i+1,' : ',arr[:c],sep='')
        insertionSort(arr,p+1,c+1)
arr = [int(i) for i in input('Enter Input : ').split()]
insertionSort(arr,1,2)
print('sorted') 
print(arr)