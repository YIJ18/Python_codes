from cryptography.fernet import Fernet


# Generar clave
clave = Fernet.generate_key()
fernet = Fernet(clave)


# Cifrar
with open('archivo.txt', 'rb') as file:
   datos = file.read()
cifrado = fernet.encrypt(datos)
with open('archivo_cifrado.aes', 'wb') as file:
   file.write(cifrado)


# Descifrar
with open('archivo_cifrado.aes', 'rb') as file:
   datos_cifrados = file.read()
descifrado = fernet.decrypt(datos_cifrados)
with open('archivo_descifrado.txt', 'wb') as file:
   file.write(descifrado)
