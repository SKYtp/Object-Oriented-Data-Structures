def minWeight(lists, box):
    min_Weight = 99999999

    if box == 1:
        return sum(lists)

    for i in range(len(lists)):
        if len(lists[i:]) < box - 1:
            break

        thisBox = sum(lists[:i])
        otherBox = minWeight(lists[i:], box - 1)
        min_Weight = min(max(thisBox, otherBox), min_Weight)

    return min_Weight

lists, numOfBox = input("Enter Input : ").split('/')
numOfBox = int(numOfBox)
lists = list(map(int,lists.split()))
print("Minimum weigth for "+str(numOfBox)+" box(es) = "+str(minWeight(lists,numOfBox)))