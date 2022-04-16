#Importar el año actual con el reloj
import datetime as dt 
ano_actual = dt.date.today().year

MENOR_DE_EDAD = 18
ADULTO=40
JUBILADO=65

ano_nacimiento = int(input("Indicar el año de nacimiento:"))
#ano_actual = int (input("Indicar el año actual:"))

edad = ano_actual-ano_nacimiento
categoria =""

if edad > JUBILADO:
   categoria = "Jubilado"
elif edad > ADULTO:
    categoria = "Adulto"
elif edad >= MENOR_DE_EDAD:
    categoria = "Joven"
else:
    categoria = "Menor de edad"
 
print("Para los datos introducidos, el usuario tiene una edad de "+str(edad)+" y está consisderado como",categoria)