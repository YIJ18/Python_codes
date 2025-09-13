from cryptography.fernet import Fernet

# Cargar clave
with open('clave.key', 'rb') as key_file:
    clave = key_file.read()

fernet = Fernet(clave)

# Cargar contraseña cifrada
with open('password.enc', 'rb') as enc_file:
    password_cifrada = enc_file.read()

# Descifrar la contraseña
password_descifrada = fernet.decrypt(password_cifrada).decode('utf-8')
print("Contraseña descifrada:", password_descifrada)
