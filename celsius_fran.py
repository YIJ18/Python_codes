def cel_far(t):
    return (9/5 * t) + 32

def far_cel(t):
    return (t - 32) * 5/9  

print("1. celsius_a_fahrenheit")
print("2. fahrenheit_a_celsius")
op = int(input("Ingresa opcion: "))
temp = float(input("Ingresa los grados: "))

if(op == 1):
    print("Son", cel_far(temp), "°F")
elif(op == 2):
    print("Son", far_cel(temp), "°C")
else:
    print("Opciones incorrectas")
