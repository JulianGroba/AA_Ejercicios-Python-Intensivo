"""
Valores matemáticos para la práctica final.
"""

def mateSuma(listaValores):
    valor = 0
    for i in listaValores:
        valor = int(i) +valor
    return valor

def mateMedia(listaValores):
    divisor = len(listaValores)
    valor = mateSuma(listaValores)/divisor
    return valor 

def vMax(listaValores):
    valor = max(listaValores)
    return valor

def vMin(listaValores):
    valor = min(listaValores)
    return valor
#QAQC   
"""
print(mateSuma(lista))
print(mateMedia(lista))
print(vMax(lista))
print(vMin(lista))
"""