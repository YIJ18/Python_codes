import math

def area_tri(a, b):
    return ((b*a)/2)

base = float(input("Ingresa la base de tu triangulo: "))
altura = float(input("Ingresa la altura de tu triangulo: "))
print("El área del triangulo es: ", area_tri(altura, base), "!!!!")