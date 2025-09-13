n = int(input("Cuantos números quieres promediar: "))
suma = 0
i = 0

for i in range(n):
    suma += float(input(f"Ingresa el número {i + 1}: "))

print("El promedio es: ", suma/n)
