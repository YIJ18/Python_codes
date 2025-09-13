# Diccionario con productos y precios fijos
tienda = {
    "Rosas rojas": 15,
    "Chocolates": 10,
    "Collar": 50,
    "Cena romántica": 100,
    "Peluche": 20,
    "Perfume": 30
}

# Función para mostrar los productos disponibles
def mostrar_tienda():
    print("Bienvenido a la tienda de regalos para San Valentín. Aquí están los productos disponibles:")
    for producto, precio in tienda.items():
        print(f"{producto}: ${precio} MXN")

# Función para calcular el costo total basado en la selección del usuario
def calcular_total(seleccion):
    total = 0
    for producto, cantidad in seleccion.items():
        total += tienda[producto] * cantidad
    return total

# Función para que el usuario seleccione los regalos
def seleccionar_regalos():
    seleccion = {}
    while True:
        mostrar_tienda()
        producto = input("\n¿Qué producto te gustaría comprar? (escribe 'salir' para terminar): ")
        
        if producto.lower() == "salir":
            break
        
        if producto in tienda:
            cantidad = int(input(f"¿Cuántos {producto} deseas? "))
            seleccion[producto] = cantidad
        else:
            print("Lo siento, no tenemos ese producto en la tienda.")
    
    return seleccion

# Función principal
def main():
    print("¡Bienvenido a la tienda de San Valentín!")
    seleccion = seleccionar_regalos()
    
    if seleccion:
        total = calcular_total(seleccion)
        print("\nResumen de tu compra:")
        for producto, cantidad in seleccion.items():
            print(f"{producto} x{cantidad}: ${tienda[producto] * cantidad} MXN")
        print(f"Total a pagar: ${total} MXN")
    else:
        print("No has seleccionado ningún producto. ¡Hasta la próxima!")

if __name__ == "__main__":
    main()
