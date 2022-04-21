"""
Utilizando generador_cosas_random.py, crear un fichero
con extensión csv que contenta 100 nombres y 100 contraseñas
mostradas en columnas separadas.
Las columnas tendrán como título: NOMBRE y CONTRASEÑA
"""
import generador_cosas_random as gcr
NUMERODENOMBRES = 100
NOMBREFICHERO = "salida.csv"

fichero = open(NOMBREFICHERO, "w")
fichero.write("NOMBRE,PASSWORD\n")
personas = gcr.generar_listado_personas(NUMERODENOMBRES)
for persona in personas:
    password = gcr.generar_contrasenya()
    fichero.write(persona + "," + password + "\n")
fichero.close()
print("Proceso terminado")
