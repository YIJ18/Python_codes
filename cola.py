class Auto:
    def __init__(self, modelo):
        self.modelo = modelo
        
        
    def __repr__(self):
        return self.modelo

class Cola:
    
    def __init__(self):
        self.elementos = []
    
    def encolar(self, auto):
        self.elementos.append(auto)
        
    def desencolar(self):
        if not self.esta_vacia():
            return self.elementos.pop(0)  
        return "La cola está vacía"
    
    def esta_vacia(self):
        return len(self.elementos) == 0

    
ferrari = Auto("Ferrari")
vocho = Auto("Vocho")
tsuru = Auto("Tsuru")
sentra = Auto("Sentra")
camaro = Auto("Camaro")

cola = Cola()
cola.encolar(ferrari)
cola.encolar(vocho)
cola.encolar(tsuru)
cola.encolar(sentra)
cola.encolar(camaro)


print("Elementos restantes en la cola:", cola.elementos)
print("Desencolando:", cola.desencolar())

print("Elementos restantes en la cola:", cola.elementos)