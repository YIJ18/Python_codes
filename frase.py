from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64
import itertools
import string

ciphertext_b64 = "IsPj6+9V66gKwRSZ5b0ONzrzl9+jvDOYNKnrZjmZFt0OK0/qGB8UIU1AKy1QvLQXRj4Ls1MvA2TYg7Ti9sc4vaCubVzDbwLK3eLajSieRiMu1fKdm0Iw1b51OvVLvLYMr0FTWpr1EKklvrIWecpdqw=="
ciphertext = base64.b64decode(ciphertext_b64)
iv = b'\x00' * 16
known_start = "Tu calificación aún no es de 10"

# Caracteres a probar (ajusta si quieres más)
charset = string.ascii_lowercase + string.digits  # a-z + 0-9

min_len = 4  # longitud mínima de la clave a probar
max_len = 6  # longitud máxima de la clave a probar

def try_key(pw):
    key_bytes = pw.encode('utf-8').ljust(32, b'\0')
    cipher = AES.new(key_bytes, AES.MODE_CBC, iv)
    decrypted = cipher.decrypt(ciphertext)
    try:
        text = unpad(decrypted, AES.block_size).decode('utf-8')
    except (UnicodeDecodeError, ValueError):
        return False
    if text.startswith(known_start):
        print(f"\n✅ ¡Clave encontrada!: '{pw}'")
        print("Texto descifrado:\n")
        print(text)
        return True
    return False

def brute_force():
    for length in range(min_len, max_len + 1):
        print(f"Probando claves de longitud {length}...")
        for attempt in itertools.product(charset, repeat=length):
            pw = ''.join(attempt)
            if try_key(pw):
                return

brute_force()
