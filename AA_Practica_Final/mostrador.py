import logging
import mapeador

#logging.getLogger().setLevel(logging.ERROR) #para cambiar el log mostrado en consola

def interfaz_pantalla():
    logging.debug("Apertura de datos, se llama a la función creada en mapeador.")
    diccionIni = mapeador.valores_finales()
    lista = mapeador.valor_total()
    sumatorio = lista[0]
    cantidad = lista[1]
    logging.debug("Mostrando valores por consola.")
    print("NOMBRE".ljust(25),"VALOR".rjust(75), sep="           ")
    print("======".ljust(25),"=====".rjust(75), sep="           ")
    for k,v in diccionIni.items():
        print(str(k).ljust(25),str(v).rjust(75),sep="           ")
    print("======".ljust(25),"=====".rjust(75), sep="           ")
    print((str(cantidad) +" PERSONAS").ljust(25),str(sumatorio).rjust(75), sep="           ")


    
    

    
#print("Ejecución Termianada. Parte 4.")

#Comprobación de funcionamiento.
interfaz_pantalla()