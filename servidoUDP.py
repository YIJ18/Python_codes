import socket as sock

# Crear socket UDP
miSocket = sock.socket(sock.AF_INET, sock.SOCK_DGRAM)

# Enlazar el socket a un puerto específico
miSocket.bind(('', 8000))

print('Servidor UDP esperando mensajes...')

while True:
    data, addr = miSocket.recvfrom(1024)  # Recibe mensaje y dirección del cliente
    print(f"Mensaje recibido de {addr}: {data.decode('utf-8')}")
    
    # Enviar respuesta al cliente
    miSocket.sendto(b'Hola desde el servidor de Iris Jasso en Python', addr)
