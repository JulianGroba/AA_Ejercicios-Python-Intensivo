NOMBRE_FICHERO = "cotizacion.dat"
LIMITE = 0

def cotizaciones (nombre_fichero):
    monedas = {}
    with open (NOMBRE_FICHERO, "r") as fichero:
        moneda = fichero.readline()
        while moneda != "":
            moneda = moneda.replace("\n", "")
            abreviatura = fichero.readline().replace("\n", "")
            cotizacion = float(fichero.readline().replace("\n", ""))
            #print(moneda, abreviatura, cotizacion)
            monedas[abreviatura]=(moneda, cotizacion)
            moneda = fichero.readline()
    #print(monedas)
    return monedas

def cot_pantalla(diccionario):
    for k,v in monedas.items():
    #print("Clave:",k,":Valor:",v[1])
        if v[1] < LIMITE:
            print("AVISO\n")
            print(v[0], "menor de", LIMITE, "\n")
            print("La clave", k, "se debería vender\n")

def fichero_venta_negativo(diccionario):
    global fichero_datos
    try:
        fichero_datos = open("datos_negativo.txt","w")
        for k,v in diccionario.items():
            if v[1] < LIMITE:
                linea1 = fichero_datos.write("AVISO:\n")
                linea2 = fichero_datos.write(str(v[0]) + " menor de " + str(LIMITE) + "\n")
                linea3 = fichero_datos.write("La clave " + k + " se debería vender.\n\n")
                linea4 = fichero_datos.write("La cotización del día es " + str(v[1]) + ".\n\n")
                #print(linea1,linea2,linea3, linea4)
            elif fichero_datos.closed == True:
                fichero_datos.close()
    except:
        print("Error en la ejecución.")
    finally:
        print("Fichero creado.")

def fichero_venta_positivo(diccionario):
    global fichero_datos
    try:
        fichero_datos = open("datos_positivo.txt","w")
        for k,v in diccionario.items():
            if v[1] > LIMITE:
                linea1 = fichero_datos.write("AVISO:\n")
                linea2 = fichero_datos.write(str(v[0]) + " mayor de " + str(LIMITE) + "\n")
                linea3 = fichero_datos.write("La clave " + k + " se debería vender.\n")
                linea4 = fichero_datos.write("La cotización del día es " + str(v[1]) + ".\n\n")
                #print(linea1,linea2,linea3, linea4)
            elif fichero_datos.closed == True:
                fichero_datos.close()
    except:
        print("Error en la ejecución.")
    finally:
        print("Fichero creado.")

def pedir_cotizacion(diccionario):
    print(monedas.keys())
    valor=input("Indicar la cotización a consultar:").upper()
    for k,v in monedas.items():
        try:    
            if valor in k:
                print("La cotización del", v[0], "es", v[1],".")
        except:
            print("Valor desconocido.")

#PRIMERA PARTE DEL EJERCICIO
monedas = cotizaciones(NOMBRE_FICHERO)
#cot_pantalla(monedas)

#SEGUNDA PARTE DEL EJERCICIO
fichero_venta_negativo(monedas)

#TERCERA PARTE DEL EJERCICIO
fichero_venta_positivo(monedas)

#ULTIMA PARTE DEL EJERCICIO
pedir_cotizacion(monedas)