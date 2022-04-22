tupla = (("Enero",10000),("Febrero",3000),("Marzo",5000),
    ("Enero",10000),("Febrero",3000),("Marzo",5000))

NOMBRE_FICHERO =  "salida.html"

fichero = open(NOMBRE_FICHERO, "w")

fichero.write("<!DOCTYPE html>\n")
fichero.write("<html lang=\"es\">\n")
fichero.write("<head>\n")
fichero.write("\t<title>Tabla de ventas</title>\n")
fichero.write("</head>\n")
fichero.write("<body>\n")
fichero.write("\t<h1>Ventas anuales</h1>\n")
fichero.write("\t<table>\n")
fichero.write("\t<tr>\n")
fichero.write("\t\t<td>Mes</td>\n")
fichero.write("\t\t<td>Ventas</td>\n")
fichero.write("\t</tr>\n")
#Parte variable

for fila in tupla:
    fichero.write("\t<tr>\n")
    fichero.write(f"        <td>{fila[0]}</td>")
    fichero.write("\n")
    fichero.write(f"        <td>{fila[1]}</td>")
    fichero.write("\n")
    fichero.write("\t</tr>\n")
#Fin de la parte variable
fichero.write("\t</table>\n")
fichero.write("</body>\n")
fichero.write("</html>")

fichero.close()
print("Fichero generado.")