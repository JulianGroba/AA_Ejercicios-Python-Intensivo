

diccionario = {'FERNANDA': 347, 'DIEGO': 370, 'VICTOR': 338, 'CRISTIAN': 618, 'ANDRES': 638, 'JULIAN': 690, 'ANTONIO': 594, 'EMILIO': 350, 'JUAN LUIS': 556, 'KEVIN': 426}


nombres = diccionario.keys()
valores = diccionario.values()

def validador(nombres, valores):
    lista=[]
    nombre2 = ()
    valoresEliminar=[]
    for valor in valores:
        print(valor)
        if valor < 450:
            valoresEliminar.append(valor)
        else:
            print("OK")
    for nombre in nombres:
        if "A" in nombre:
            nombre2=nombre.replace("A","@")
            lista.append(nombre2)
        else:
            lista.append(nombre)
    return valoresEliminar, lista

def modificador_nombres(diccionario):
    nombres = diccionario.keys()
    valores = diccionario.values()
    for nombre in list(nombres):
        if "A" in nombre:
            nombre2 = nombre.replace("A","@")
            diccionario[nombre2] = diccionario.pop(nombre)
        else:
            pass
    return print(diccionario)

def borrar_diccionario(diccionario):
    diccionario2 = {}
    for k,v in diccionario.items():
        if v > 450:
            diccionario2[k]=v
    return diccionario2
    
#print(validador(nombres, valores))
modificador_nombres(diccionario)
print(borrar_diccionario(diccionario))
