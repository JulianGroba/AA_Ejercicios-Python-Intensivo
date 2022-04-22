NOMBRE_FICHERO = "tabla.txt"

ventas = {"Lunes":(2083,38), "Martes":(10,183), "Miércoles":(-283,19), "Jueves":(2023,11), "Viernes":(10,18)}

linea1 = "Ventas".center(50)
linea2 = ""
linea3 = ""
linea4 = ""

for key, value in ventas.items():
    linea2 = linea2 + key.ljust(10)
    linea3 = linea3 + str(value[0]).rjust(10)
    linea4 = linea4 + str(value[1]).rjust(10)

fichero = open(NOMBRE_FICHERO, "w")
fichero.write(linea1)
fichero.write("\n")
fichero.write(linea2)
fichero.write("\n")
fichero.write(linea3)
fichero.write("\n")
fichero.write(linea4)
fichero.close()

print(linea1)
print(linea2)
print(linea3)
print(linea4)