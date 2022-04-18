"""
Hacer una calculadora con funciones
Sumar dos números, Restar dos números, Multiplicar dos números, Dividir dos números
1. Sumar
2. Restar
3. Multiplicar
4. Dividir.
¿0. Salir.?
Introduce la operación que quieras realizar.
"""
def sumar(s1,s2):
    return s1+s2
def restar(s1,s2):
    return s1-s2
def multiplicar(s1,s2):
    return s1*s2
def dividir(s1,s2):
    return s1/s2

def mostrar_menu():
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("0. Salir")

def menu():
    opcion = -1
    while opcion !=0:
        mostrar_menu()
        try:
            opcion = int(input("Elegir la opción deseada:"))
            if opcion in (1,2,3,4):
                try:
                    n1 = float(input("Indicar el primer operador:"))
                    n2 = float(input("Indicar el primer operador:"))
                    if opcion == 1:
                        print("El resultado de la suma es:", sumar(n1,n2))
                    elif opcion == 2:
                        print("El resultado de la resta es:", restar(n1,n2))
                    elif opcion == 3:
                        print("El resultado de la multiplicación es:", multiplicar(n1,n2))
                    elif opcion == 4:
                        print("El resultado de la división es:", dividir(n1,n2))
                    else:
                        print("Saliendo del sistema.")
                except:
                    print("Error inesperado")
            elif opcion == 0:
                print("Saliendo del sistema.")
            else:
                print("Opción no válida.")
        except (IndexError,ValueError):
            print("No se ha elegido un número entre 0 y 4.")
        except:
            print("Error inesperado")

        


menu()

print("Ejercicio terminado.")