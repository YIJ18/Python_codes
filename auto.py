# Equivalente en Python del código C++

class Auto:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.posicion = 0

    def avanzar(self, distancia):
        self.posicion += distancia

    def imprimir(self):
        print(f"{self.marca} {self.modelo} {self.posicion} Km")

def main():
    mi_vocho = Auto("VW", "Sedan")
    mi_vocho.avanzar(100)
    mi_vocho.imprimir()
    # Crear otro objeto Auto
    mi_coche = Auto("Otro", "Modelo")
    mi_coche.avanzar(300)
    mi_coche.imprimir() 

if __name__ == "__main__":
    main()