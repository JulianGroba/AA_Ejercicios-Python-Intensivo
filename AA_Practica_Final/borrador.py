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
       
    nombreComprobar = "JULIAN"
    cantidad = nombres_Mayus.count(nombreComprobar)
    print(cantidad)
    #print(nombres)
    #print(valores)
    print(buscador_indices(nombres_Mayus,nombreComprobar))
    print(valor_indice(buscador_indices(nombres_Mayus,nombreComprobar),nombres_Mayus))
    print(valor_indice(buscador_indices(nombres_Mayus,nombreComprobar),valores))


nombre_user()


