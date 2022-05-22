import logging
import random
#logging.getLogger().setLevel(logging.ERROR) #para cambiar el log mostrado en consola
NUMERODENOMBRES = 1000
NOMBREFICHERO = "datos.csv"

def leer_excel():
    nombres = [] #odd_i
    valores = [] #even_i
    try:
        fichero = open(NOMBREFICHERO, "r")
        logging.debug("Trasformando el fichero en carácteres.")
        linea = fichero.read().replace("\n",",")
        if linea != "":
            logging.debug("Creando lista para trabajar sobre ella.")
            separados=linea.split(sep=",")
            logging.debug("Dividiendo la lista entre nombres y valores para poder trabajar en el futuro.")
            for i in range (len(separados)):
                if i % 2:
                    valores.append(separados[i])
                else:
                    nombres.append(separados[i])
            #print(nombres, valores) # QAQC
        logging.debug("Comprobación de que ambas listas tienen el mismo número de elementos.")
        while len(nombres)!=len(valores):
            nombres.pop()
        else:
            pass
        return nombres, valores  
    except:
        print("Proceso terminado sin ejecución. Consultar al informático.")    
    fichero.close()
    print("Proceso terminado. Punto 2 Completado")

def buscador_indices(lista, elemento):
    listaIndices = []
    for i in range(len(lista)):
        if lista[i] == elemento:
            listaIndices.append(i)
    return listaIndices

def valor_indice(listaIndices, lista):
    listaValores =[]
    for i in listaIndices:
        valor=lista[i]
        listaValores.append(valor)
    return listaValores

def nombre_user():
    logging.debug("Traer los datos del excel: nombres y valores.")
    lista=leer_excel()
    nombres = lista[0]
    valores = lista[1]
    logging.debug("Cambiar que todos los nombres estan en Mayúsculas.")
    nombres_Mayus = [x.upper() for x in nombres]
    logging.debug("Crear un conjunto con los nombres incluidos en los datos.")
    nombresSinTitulo = nombres_Mayus
    if "NOMBRE" in nombresSinTitulo:
        nombresSinTitulo.remove("NOMBRE")
        conjuntoNombres = set(nombresSinTitulo)
    else:
        conjuntoNombres = set(nombres_Mayus)
    logging.debug("Pedir dato al usario.")
    print("Los nombres incluidos en los datos son:")
    print(conjuntoNombres)
    nombreComprobar = input("Incluir un nombre de la lista anterior:").upper()
    n=0 # para romper bucle infinito en caso de estupidez humana.
    
    while nombreComprobar not in conjuntoNombres:   
        if n == 3:
            listNom = list(conjuntoNombres)
            nombreComprobar = random.choice(listNom)
            print("Se ha decidido por el siguiente nombre:"+nombreComprobar)
        else:
            n+=1 
            print ("Nombre no incluido en la lista, por favor incluir nombre de la lista.")
            print(conjuntoNombres)
            nombreComprobar = input("Incluir un nombre de la lista anterior:").upper()
    else:
    
        miDiccionario = dict(nombres,valores)
        print(miDiccionario)
        print ("Nombre SI incluido en la lista.")
        print(type(nombreComprobar))
        indiceLista = nombres_Mayus.index(nombreComprobar)
        print(indiceLista)
    #print(nombres, valores)

#Comprobación de funcionamiento.

#leer_excel()
nombre_user()


