import logging
import mapeador

#logging.getLogger().setLevel(logging.ERROR) #para cambiar el log mostrado en consola

def interfaz_pantalla():
    logging.debug("Apertura de datos, se llama a la función creada en mapeador.")
    lista = mapeador.leer_excel()
    nombres = lista[0]
    valores = lista[1]
    listaZip = list(zip(nombres, valores))
    logging.debug("Crear cabecera.")
    print(listaZip)
    #print(listaZip[0])
    """
    print(nombres)
    print(list(nombres))
    print(valores)
    print(list(valores))
    
    print(nombres[0].ljust(50), valores[0].rjust[50])
    print("==========".ljust(50), "==========".rjust(50))
    """
#print("Ejecución Termianada. Parte 4.")

#Comprobación de funcionamiento.
interfaz_pantalla()