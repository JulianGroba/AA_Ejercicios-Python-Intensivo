dias = ["lunes","martes","miercoles","jueves","viernes","sabado","domingo"]
print(dias)
dia_buscado = input("Introducir un día vde la semana:")

for dia in dias:
    if dia_buscado == dia:
        print("El día buscado es", dia.capitalize())
        break

print ("Ejercicio resuelto")