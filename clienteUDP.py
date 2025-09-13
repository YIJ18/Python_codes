import socket as sock

# Crear socket UDP
cliente = sock.socket(sock.AF_INET, sock.SOCK_DGRAM)

# Enviar mensaje al servidor
mensaje = b'Hola desde el cliente de Omar en Python!!!'
cliente.sendto(mensaje, ('localhost', 8000))

# Recibir respuesta del servidor
data, server = cliente.recvfrom(1024)

print("Respuesta del servidor:", data.decode('utf-8'))
