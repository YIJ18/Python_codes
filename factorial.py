def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)
    
a = int(input("Hasta qué número quieres llegar: ")) 
print("El resultado es: ", fact(a))


