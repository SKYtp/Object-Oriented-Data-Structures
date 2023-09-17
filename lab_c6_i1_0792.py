def fibo(n = int):
    if(n <= 1):
        return n
    else:
        return fibo(n - 1) + fibo(n - 2)
inp = int(input('Enter Number : '))
print('fibo(',inp,')',' = ',fibo(inp),sep='')