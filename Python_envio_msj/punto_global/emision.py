from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

# Generar una clave privada
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)

# Obtener la clave pública
public_key = private_key.public_key()

# Guardar la clave privada
with open("private_key.pem", "wb") as private_pem:
    private_pem.write(private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    ))

# Guardar la clave pública
with open("public_key.pem", "wb") as public_pem:
    public_pem.write(public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    ))

print("Llaves generadas y guardadas.")
