# Crear el archivo amigos.txt con nombres de ejemplo
with open("amigos.txt", "w", encoding="utf-8") as file:
    file.write("Carlos\nAna\nLuis\nMaría\nPedro")

# Crear el archivo plantilla.txt con una plantilla de ejemplo
with open("plantilla.txt", "w", encoding="utf-8") as file:
    file.write("Hola {nombre},\n\nEspero que estés teniendo un gran día. ¡Nos vemos pronto!\n\nSaludos,\nTu amigo.")

# Leer los archivos y generar las cartas
with open("amigos.txt", "r", encoding="utf-8") as file:
    amigos = [line.strip() for line in file.readlines()]

with open("plantilla.txt", "r", encoding="utf-8") as file:
    plantilla = file.read()

def generar_cartas():
    for amigo in amigos:
        contenido_personalizado = plantilla.replace("{nombre}", amigo)
        nombre_archivo = f"carta_{amigo}.txt"
        with open(nombre_archivo, "w", encoding="utf-8") as carta:
            carta.write(contenido_personalizado)
    print("Cartas generadas exitosamente.")

generar_cartas()
