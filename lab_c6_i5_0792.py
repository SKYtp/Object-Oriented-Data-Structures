def asteroid_collision(asts):
    def working(temp,asteroid):
        if(not temp):
            temp.append(asteroid)
        elif(asteroid < 0 and temp[-1] > 0):
            if(asteroid + temp[-1] < 0):
                temp.pop()
                working(temp, asteroid)
            elif(asteroid + temp[-1] == 0):
                temp.pop()
        else:
            temp.append(asteroid)
    if(len(asts) <= 1):
        ac = asts[0]
        temp = []
        working(temp,ac)
        return temp
    else:
        ac = asts[len(asts)-1]
        temp = list(asteroid_collision(asts[:len(asts)-1]))
        working(temp,ac)
        return temp
x = input("Enter Input : ").split(",")
x = list(map(int,x))
print(asteroid_collision(x))