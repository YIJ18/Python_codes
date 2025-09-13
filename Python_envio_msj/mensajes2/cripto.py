from cryptography.fernet import Fernet

# Generación de clave y cifrado de contraseña
clave = Fernet.generate_key()
with open('clave.key', 'wb') as key_file:
    key_file.write(clave)

# Cifra la contraseña real
fernet = Fernet(clave)
password = "kasg nvci gian mklk"
password_cifrada = fernet.encrypt(password.encode())

# Guarda la contraseña cifrada
with open('password.enc', 'wb') as enc_file:
    enc_file.write(password_cifrada)
