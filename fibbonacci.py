def fibo(n):
    if(n > 2):
        return fibo( n - 1 ) + fibo( n - 2 )
    elif(n == 2):
        return 1
    elif(n == 1):
        return 1
    elif(n == 0):
        return 0
    
    
n = int(input("Ingresa numero iteraciones: "))
for n in range(0, n):
    print(fibo(n))