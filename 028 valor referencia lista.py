"""
Dos funciones
[x] Resolver con el paso de parámetros por referencia
[x] Resolver con el "paso de parámetros por valor" (No modificar la lista pasada como parámetro en la función)
agregar_item
	Recibe como parámetro una lista y un elemento a agregar
La versión por refencia modifica la lista original
La versión por valor hay que conseguir que modifique la lista original
"""


lista_original = [1,2,3,4,5]

def agregarItemRef (lista,item):
    lista.append(item)

def agregarItemValor (lista,item):
    lista_local = lista[:]
    lista_local.append(item)
    return lista_local

print(lista_original)
agregarItemRef(lista_original,6)
print(lista_original)

lista_original = agregarItemValor(lista_original,7)
print(lista_original)