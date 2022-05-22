import logging
import random
import operadores

#logging.getLogger().setLevel(logging.ERROR) #para cambiar el log mostrado en consola
NUMERODENOMBRES = 1000
NOMBREFICHERO = "datos.csv"
VALORLIMITE = 1000 #Cambiar conforme al enunciado a 1000 después de las pruebas.

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
    print("Proceso terminado.")

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
        logging.debug("Sacar valores para mostrar en pantalla.")
        valorNombreElegido= valor_indice(buscador_indices(nombres_Mayus,nombreComprobar),valores)
        valorSuma=operadores.mateSuma(valorNombreElegido)
        valorMedia=operadores.mateMedia(valorNombreElegido)
        valorMax=operadores.vMax(valorNombreElegido)
        valorMin=operadores.vMin(valorNombreElegido)
        cantidad = len(valorNombreElegido)
        logging.debug("Mostrar por pantalla los resultados elegidos.")
        print(("El nombre elegido: {nombre} ha aparecido el siguiente número de veces: {numero}.").format(nombre=nombreComprobar, numero=cantidad))
        print(("El valor medio es: {vm}, el valor máximo es: {vmax}, el valor mínimo es: {vmin} y el valor de la suma es {sum} para el nombre elegido: {nombre}.").format(nombre=nombreComprobar, sum=valorSuma, vm = valorMedia, vmax = valorMax, vmin = valorMin))

#print("Ejecución Termianada. Parte 2.")
def valor_total():
    logging.debug("Traer los datos del excel: nombres y valores.")
    lista=leer_excel()
    valores = lista[1]
    logging.debug("Retirar el string.")
    if "VALOR" in valores:
        valores.remove("VALOR")
    else:
        pass
    logging.debug("Sacar valores.")
    valorSuma=operadores.mateSuma(valores)
    cantidad = len(valores)
    logging.debug("Guardar resultados elegidos.")
    return valorSuma, cantidad

def valores_excel():
    logging.debug("Traer los datos del excel: nombres y valores.")
    lista=leer_excel()
    valores = lista[1]
    logging.debug("Retirar el string.")
    if "VALOR" in valores:
        valores.remove("VALOR")
    else:
        pass
    logging.debug("Sacar valores para mostrar en pantalla.")
    valorSuma=operadores.mateSuma(valores)
    valorMedia=operadores.mateMedia(valores)
    valorMax=operadores.vMax(valores)
    valorMin=operadores.vMin(valores)
    cantidad = len(valores)
    logging.debug("Mostrar por pantalla los resultados elegidos.")
    print(("Hay el siguiente número de valores: {numero}.").format(numero=cantidad))
    print(("El valor medio es: {vm}, el valor máximo es: {vmax}, el valor mínimo es: {vmin} y el valor de la suma es {sum} incluidos en el excel.").format(sum=valorSuma, vm = valorMedia, vmax = valorMax, vmin = valorMin))
    return valorSuma
#print("Ejecución Termianada. Parte 3.")

def modificador_nombres(diccionario):
    nombres = diccionario.keys()
    valores = diccionario.values()
    for nombre in list(nombres):
        if "A" in nombre:
            nombre2 = nombre.replace("A","@")
            diccionario[nombre2] = diccionario.pop(nombre)
        else:
            pass
    return diccionario

def borrar_diccionario(diccionario):
    diccion2 = {}
    for k,v in diccionario.items():
        if v > VALORLIMITE: 
            diccion2[k]=v
    return diccion2

def valores_finales():
    logging.debug("Traer los datos del excel: nombres y valores.")
    lista=leer_excel()
    nombres = lista[0]
    valores = lista[1]
    logging.debug("Cambiar que todos los nombres estan en Mayúsculas.")
    nombres_Mayus = [x.upper() for x in nombres]
    logging.debug("Retirar encabezados.")
    if "VALOR" in valores:
        valores.remove("VALOR")
    if "NOMBRE" in nombres_Mayus:
        nombres_Mayus.remove("NOMBRE")
    logging.debug("Obtener lista de nombres únicos y valores asociados.")
    conjuntoNombres = set(nombres_Mayus)
    valoressumados = []
    for nombre in conjuntoNombres:
        logging.debug("QAQC", nombre)
        valorNombreElegido= valor_indice(buscador_indices(nombres_Mayus,nombre),valores)
        valorSumaElegido=operadores.mateSuma(valorNombreElegido)
        valoressumados.append(valorSumaElegido)
        logging.debug("QAQC", valorSumaElegido)
    logging.debug("Obtener lista de nombres únicos y valores asociados.")
    diccionario = dict(zip(list(conjuntoNombres),valoressumados))
    logging.debug("QAQC", diccionario)
    resultado = modificador_nombres(borrar_diccionario(diccionario))
    logging.debug("QAQC", resultado)
    logging.debug("Ordenaro por orden alfabético.")
    valores_ord = {k: v for k, v in sorted(resultado.items())}
    logging.debug("QAQC",valores_ord)
    #print("Elemento termiando.")
    #print(valores_ord)
    return valores_ord
    
#Comprobación de funcionamiento.

#leer_excel()
#nombre_user()
#valores_excel()
#valores_finales()
