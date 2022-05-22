"""
Ejercicio Final

1) Un programa que genere un fichero con "n" registros compuestos por nombres y valores aleatorios.
    Los nombres deben ser de una lista de 10.
    Los valores de un rango entre 0 y n. El valor "n" debe ser solicitado al usuario mediante teclado.
    Usar Filas y Tuplas.
2) Un programa que solicite un nombre al usario y muestre el valor asociado, mediante el uso de un mapa.
3) Un programa que calcule la suma, la media, el valor máximo y minimo de los "n" números incluidos en el fichero.
4) Un programa que muestre el listado de la siguiente forma.
    -Ordenados Alfaéticamente.
    -Todos los nombres en Mayusculas.
    -Nombres a la izquierda y valores a la derecha.
    -Letras A remplezadas por @
    -Sólo los individuos con valores superiores o iguales a 1000.

El código debe estar estructurado en funciones.
Controlar errores en los accesos a ficheros.
Incluir dos pruebas unitarias.
Incluir un manual de instrucciones de los diferentes programas.

"""
import generador
import mapeador
#import operadores

def mostrar_menu():
    print("1. Generar Valores y Exportar a Excel")
    print("2. Comprobar un valor introducido por el usuario.")
    print("3. Entrega de los valores medios, máximos y mínimos incluidos en el Excel.")
    print("4. Mostrar por consola conforme a informe predefinido.")
    print("0. Salir")

def controlador():
    opcion = -1
    while opcion !=0:
        mostrar_menu()
        try:
            opcion = int(input("Elegir la opción deseada:"))
            try:
                if opcion in (1,2,3,4):
                    print("Procediendo con la opción deseada.\n")
                    if opcion == 1:
                        #Parte 1
                        generador.generar_excel()
                        print("\nEjecución Terminada\n".rjust(150))
                    elif opcion == 2:
                        #Parte 2
                        mapeador.nombre_user()
                        print("\nEjecución Terminada\n".rjust(150))
                    elif opcion == 3:
                        #Parte 3
                        mapeador.valores_excel()
                        print("\nEjecución Terminada\n".rjust(150))
                    elif opcion == 4:
                        mapeador.valores_finales()
                        #mostrador.interfaz_pantalla()
                        print("\nEjecución Terminada\n".rjust(150))
                    #else:    
                        print("Error. Póngase en contacto con ITTI")
                elif opcion == 0:
                    print("Saliendo del sistema.")
                else:
                    print("Opción no válida.")
            except:
                "Error. Póngase en contacto con ITTI"
        except ValueError:
            print("Se debe introducir un número entre 0 y 4")
        except:
            print("Error inesperado")    



#TODO Interfaz gráfica.
#Parte 1
#generador.generar_excel()
#Parte 2
#mapeador.nombre_user()
#Parte 3
#mapeador.valores_finales()

#Parte 4
#TODO mostrador.interfaz_pantalla()

controlador()
