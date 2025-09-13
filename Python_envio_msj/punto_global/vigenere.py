def cifrar_vigenere(texto, clave):
    alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    texto = texto.upper()
    clave = clave.upper()
    texto_cifrado = []
    i = 0
    for letra in texto:
        if letra in alfabeto:
            indice_texto = alfabeto.index(letra)
            indice_clave = alfabeto.index(clave[i % len(clave)])
            texto_cifrado.append(alfabeto[(indice_texto + indice_clave) % len(alfabeto)])
            i += 1
        else:
            texto_cifrado.append(letra)
    return ''.join(texto_cifrado)

# Ejemplo de uso
mensaje = "Hola Mundo"
clave = "ClaveSecreta"
mensaje_cifrado = cifrar_vigenere(mensaje, clave)
print("Mensaje Cifrado:", mensaje_cifrado)
