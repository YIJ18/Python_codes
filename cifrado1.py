import hashlib

def hash_file(filepath):
    with open(filepath, 'rb') as f:
        data = f.read()
        print("MD5:", hashlib.md5(data).hexdigest())
        print("SHA1:", hashlib.sha1(data).hexdigest())
        print("SHA256:", hashlib.sha256(data).hexdigest())

hash_file("archivo.txt")
