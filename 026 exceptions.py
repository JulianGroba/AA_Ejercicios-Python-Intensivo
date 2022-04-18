"""
Construir una lista con los números [3,8,10,23,0]
Pedir al usuario dos números entre 0 y 4.
Dividir los números que están en la lista en la posiciones indicadas.
Hay que controlar el error de número (índice) fuera de rango.
Hay que controlar el error de división entre cero.
Hay que controlar que los valores introducidos sean números.
"""
numeros = [3,8,10,23,0]


try:
    numUser1 = int (input("Introducir un número entre 0 y 4:"))
    numUser2 = int (input("Introducir un número entre 0 y 4:"))
    
    division = numeros[numUser1]/numeros[numUser2]

except IndexError:
    print("No se ha elegido un número entre 0 y 4.")
except ValueError:
    print("Se ha incluido una letra, no se puede hacer la división.")
except ZeroDivisionError:
    print("No se puede dividir entre 0.")
except:
    print("Ha ocurrido un error.")
else:
    print("El resultado es:", division)
finally:
    print("Proceso terminado.")