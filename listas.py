mi_lista = [3, 5, 7, 2, 9]
mi_lista.append(10)
print("Lista después de agregar 10:", mi_lista)
mi_lista.remove(5)
print("Lista después de eliminar 5:", mi_lista)
mi_lista.sort()
print("Lista ordenada:", mi_lista)

dias_semana = ("Lunes", "Martes", "Miércoles", "Jueves", "Viernes")
print("Día en el índice 2 de la tupla:", dias_semana[2])

mi_conjunto = {1, 2, 3, 4, 4, 5}
print("Conjunto sin duplicados:", mi_conjunto)
mi_conjunto.add(6)
print("Conjunto después de agregar 6:", mi_conjunto)
otro_conjunto = {7, 8, 9}
unido = mi_conjunto.union(otro_conjunto)
print("Resultado de la unión:", unido)
