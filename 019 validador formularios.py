#Importar el año actual con el reloj
import datetime as dt 
ano_actual = dt.date.today().year

nombre = input("Introducir el nombre completo:")
ano_nacimiento =int(input("Introduce el año de nacimiento:"))
correo = input("Introduce el correo electrónico:")
telf = input("Introduce el número de teléfono:")
edad = ano_actual-ano_nacimiento

nombre_correcto = len(nombre)>=10
ano_correcto = edad >=18.
correo_correcto = "@" in correo
telefono_correcto = telf.isdigit()

#Solucion INICIAL
"""
if nombre_correcto and ano_correcto and correo_correcto and telefono_correcto:
    print("Cumple")
else:
    print("No cumple")
"""
#Solucion ACEPTABLE
"""
if not ombre_correcto:
    print("El nombre no tienen la longitud adecuada (al menos 10 caracteres)")
elif not ano_correcto:
    print("Tiene que ser mayor de edad")
elif not correo_correcto:
    print("Tiene que introducir una dirección de correo electrónico válida")
elif not telefono_correcto:
    print("El número de teléfono es incorrecto")
else:
    print("El formulario es correcto")
"""

#Solucion COMPLETA
hayError=False #Flag
if not nombre_correcto:
    print("El nombre no tienen la longitud adecuada (al menos 10 caracteres)")
    hayError=True
if not ano_correcto:
    print("Tiene que ser mayor de edad")
    hayError=True
if not correo_correcto:
    print("Tiene que introducir una dirección de correo electrónico válida")
    hayError=True
if not telefono_correcto:
    print("El número de teléfono es incorrecto")
    hayError=True
if not hayError:
    print("Todo ok.")