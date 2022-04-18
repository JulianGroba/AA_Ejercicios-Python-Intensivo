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

def menu():
    try:
        opcion = int(input("Elegir la opción deseada: 1-Suma, 2-Resta, 3-Multiplicación, 4-División, 0-Salir"))
        if opcion !=0:
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
        else:
            print("Opción seleccionada es salir del sistema.")
    except (IndexError,ValueError):
        print("No se ha elegido un número entre 0 y 4.")
    except:
        print("Error inesperado")
    finally:
        print("Ejercicio terminado.")

menu()

