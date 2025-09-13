from cryptography.fernet import Fernet

# Generar clave y guardarla
clave = Fernet.generate_key()
with open("clave.key", "wb") as key_file:
    key_file.write(clave)

# Encriptar la contraseña
fernet = Fernet(clave)
password = "tu_contraseña_de_correo".encode()
password_encriptada = fernet.encrypt(password)

# Guardar la contraseña encriptada
with open("password_encriptado.txt", "wb") as f:
    f.write(password_encriptada)
