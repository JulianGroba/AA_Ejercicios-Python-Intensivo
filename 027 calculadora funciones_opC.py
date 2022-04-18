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

def gestionar_operaciones(opcion, operando1, operando2):
    if opcion == 1:
        resultado = sumar(operando1, operando2)
    elif opcion == 2:
        resultado = restar(operando1, operando2)
    elif opcion == 3:
        resultado = multiplicar(operando1, operando2)
    elif opcion == 4:
        resultado = dividir(operando1, operando2)
    return resultado

def funcion_main():
    opcion = -1
    while opcion !=0:
        mostrar_menu()
        try:
            opcion = int(input("Elegir la opción deseada:"))
            if opcion in (1,2,3,4):
                try:
                    n1 = float(input("Indicar el primer operador:"))
                    n2 = float(input("Indicar el primer operador:"))
                    resultado = gestionar_operaciones(opcion, n1,n2)
                    print("El resultado de la operación es", resultado)
                except:
                    print("Error inesperado")
            elif opcion == 0:
                print("Saliendo del sistema.")
            else:
                print("Opción no válida.")
        except:
            print("Error inesperado")  

funcion_main()

print("Ejercicio terminado.")