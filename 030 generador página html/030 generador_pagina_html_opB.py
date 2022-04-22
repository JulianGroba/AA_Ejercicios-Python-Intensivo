datos = (("Enero",10000),("Febrero",3000),("Marzo",5000),
    ("Enero",10000),("Febrero",3000),("Marzo",5000))

NOMBRE_FICHERO =  "salida_opB.html"

fichero = open(NOMBRE_FICHERO, "w")
primer_bloque = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <title>Tabla de ventas</title>
    </head>
    <body>
        <h1>Ventas anuales</h1>
        <table>
            <tr>
                <td>Mes</td>
                <td>Ventas</td>
            </tr>
"""
fichero.write(primer_bloque)
#Parte variable

for fila in datos:
    fichero.write("\t<tr>\n")
    fichero.write(f"        <td>{fila[0]}</td>")
    fichero.write("\n")
    fichero.write(f"        <td>{fila[1]}</td>")
    fichero.write("\n")
    fichero.write("\t</tr>\n")
#Fin de la parte variable
ultimo_bloque = """
        </table>
    </body>
    </html>
"""
fichero.write(ultimo_bloque)
fichero.close()
print("Fichero generado.")