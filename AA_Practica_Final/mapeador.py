import random
NUMERODENOMBRES = 1000
NOMBREFICHERO = "datos.csv"

def leer_excel():
    try:
        fichero = open(NOMBREFICHERO, "r")
        fichero.read()
    except:
        print("Proceso terminado sin ejecución")    
    fichero.close()
    print("Proceso terminado. Punto 2 Completado")

#Comprobación de funcionamiento.
leer_excel()

