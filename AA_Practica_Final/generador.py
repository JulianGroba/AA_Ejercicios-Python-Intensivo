import random
import logging
#logging.getLogger().setLevel(logging.ERROR) #para cambiar el log mostrado en consola
NUMERODENOMBRES = 1000
NOMBREFICHERO = "datos.csv"
n = 0
#TODO crear un archivo de log para hacer seguimiento de los errores.

def generar_listado_personas(numero):
    logging.debug("Creando lista de nombres")
    nombres = ("Julian","Fernando","Andres","Juan Luis", "Victor", "Emilio", "Antonio", "Cristian", "Kevin", "Diego")
    personas=[]
    logging.debug("Generando una lista al azar de nombres conforme a la lista entregada.")
    for i in range(numero):
        nueva_persona = random.choice(nombres)
        personas.append(nueva_persona)
    return personas

def generar_valores_aleatorios(n):
    nuevo_valor = 0
    logging.debug("Comprobando el valor n es válido.")
    try:
        if n!=0:
            rango = range(n)
        else:
            rango = range(NUMERODENOMBRES)
    except:
        pass
    logging.debug("Generando un valor aleatorio.")
    for i in rango:
        nuevo_valor = random.choice(rango)
    return nuevo_valor

def generar_excel():
    logging.debug("Abriendo y creando fichero si no existe.")
    fichero = open(NOMBREFICHERO, "w")
    logging.debug("Generando encabezado.")
    fichero.write("NOMBRE,VALOR\n")
    try:
        logging.debug("Introduciendo valor n por el usuario.")
        n = int(input("Intruzduca el valor n:"))
        personas = generar_listado_personas(n)
        for p in personas:
            v = generar_valores_aleatorios(n)
            fichero.write( p + "," + str(v) + "\n")      
    except ValueError:
        logging.debug("Valor introducido incorrecto se procede con valor por defecto.")  
        print("Valor introducido no es un entero, se procede con 1000")
        personas = generar_listado_personas(NUMERODENOMBRES)
        for p in personas:
            v = generar_valores_aleatorios()
            fichero.write( p + "," + str(v) + "\n")
    except:
        logging.debug("Valor introducido incorrecto. Crear log y ver posible solución.") 
        print("Proceso terminado sin ejecución")    
    fichero.close()
    print("Proceso terminado. Excel Creado.")

#print("Parte 1 terminada.")

#Comprobación de funcionamiento.
#generar_excel()

