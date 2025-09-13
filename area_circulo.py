import math

def area_circulo(r):
    return (math.pi * r ** 2)

radio = float(input("Ingresa el radio de tu circulo: "))
print("El área delc irculo es: ", area_circulo(radio), "!!!!")