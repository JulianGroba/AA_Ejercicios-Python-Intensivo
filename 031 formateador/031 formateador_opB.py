NOMBRE_FICHERO = "tabla_opB.txt"

def abrir_fichero (nombreFichero):
    fichero = open(nombreFichero, "a")
    return fichero

def escribir_fichero (f1, linea):
    f1.write(linea)
    f1.write("\n")

def cerrar_fichero (fichero):
    fichero.close()


ventas = {"Lunes":(2083,38), "Martes":(10,183), "Miércoles":(-283,19), "Jueves":(2023,11), "Viernes":(10,18)}

linea1 = "Ventas".center(50)
linea2 = ""
linea3 = ""
linea4 = ""

for key, value in ventas.items():
    linea2 = linea2 + key.ljust(10)
    linea3 = linea3 + str(value[0]).rjust(10)
    linea4 = linea4 + str(value[1]).rjust(10)

try:
    fichero = abrir_fichero(NOMBRE_FICHERO)
    escribir_fichero(fichero,linea1)
    escribir_fichero(fichero,linea2)
    escribir_fichero(fichero,linea3)
    escribir_fichero(fichero,linea4)
    cerrar_fichero(fichero)
except:
    print("Ha ocurrido un error.")