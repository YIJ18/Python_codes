from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization

# Cargar la clave pública
with open("public_key.pem", "rb") as pub_file:
    public_key = serialization.load_pem_public_key(pub_file.read())

# Verificar la firma
message = b"Mensaje original"
signature = b"firma_en_bytes"

try:
    public_key.verify(
        signature,
        message,
        padding.PKCS1v15(),
        hashes.SHA256()
    )
    print("La firma es válida.")
except Exception as e:
    print("La firma no es válida:", e)
