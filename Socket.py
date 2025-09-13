import socket as sock

miSocket=sock.socket(sock.AF_INET,sock.SOCK_STREAM)

#AF_INET Familia de protocolo IP V4
#SOCK_STREAM -> TCP
#SOCK_DGRAM  -> UDP

miSocket.bind(('',8000))
miSocket.listen()
#'192.168.127.228'

print('Escuchando conexion ...')

while True:
    con,addr = miSocket.accept()
    print("Conexion recibida de",addr)
    con.send(b'Hola desde el servidor de Iris Jasso de Python')
    con.close()




