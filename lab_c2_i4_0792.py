def Getlist(gl):
    mList = []
    sum = 0
    ch = True
    for i in range(0, len(gl)-2):
        for j in range(i + 1, len(gl)-1):
            for k in range(j + 1, len(gl)):
                if (int(gl[i]) + int(gl[j]) + int(gl[k]) == sum):
                    temp = []
                    temp.append(int(gl[i]))
                    temp.append(int(gl[j]))
                    temp.append(int(gl[k]))
                    mList.append(list(temp))
    result = [] 
    for i in mList: 
        if i not in result: 
            result.append(i) 
    return list(result)
    
inNum = list(input("Enter Your List : ").split())
if(len(inNum) > 2):
    print(Getlist(inNum))
else:
    print("Array Input Length Must More Than 2")