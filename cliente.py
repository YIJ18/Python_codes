import socket as sock

cliente = sock.socket(sock.AF_INET, sock.SOCK_STREAM)

cliente.connect(('localhost',8000))

cliente.send(b'Hola desde el cliente de Omar en Python!!!\n')

data = cliente.recv(1000)

print(data.decode('ascii'))

