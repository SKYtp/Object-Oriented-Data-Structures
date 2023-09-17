def calPoint(d):
    return int((3*d['wins'])+(0*d['loss'])+(1*d['draws']))
def calGd(d):
    return int(d['scored'] - d['conceded'])
def leagueSort(l):
    for last in range(len(l)-1, 0,-1):
        swaped = False
        for i in range(last):
            if(calPoint(l[i]) == calPoint(l[i+1])):
                if(calGd(l[i]) < calGd(l[i+1])):
                    l[i], l[i+1] = l[i+1], l[i]
                    swaped = True
            elif calPoint(l[i]) < calPoint(l[i+1]):
                l[i], l[i+1] = l[i+1], l[i]
                swaped = True
        if not swaped:
            return l
        elif(last <= 1):
            return l
inp = input('Enter Input : ').split('/')
arr = []
for i in inp:
    temp = list(i.split(','))
    arr.append(dict({ "name": temp[0], "wins": int(temp[1]), "loss": int(temp[2]), "draws": int(temp[3]), "scored": int(temp[4]), "conceded": int(temp[5]) }))
arr = leagueSort(arr)
for i in range(len(arr)):
    arr[i] = [str(arr[i]['name']),dict({'points':calPoint(arr[i])}),dict({'gd':calGd(arr[i])})]
print('== results ==')
for i in arr:
    print(i)