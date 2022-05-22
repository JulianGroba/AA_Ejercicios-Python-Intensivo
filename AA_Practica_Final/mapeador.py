import logging
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

#Comprobación de funcionamiento.

#leer_excel()


