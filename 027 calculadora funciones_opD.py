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

calculadora = {
    "1":("Sumar",sumar), 
    "2":("Restar",restar),
    "3":("Multiplicar",multiplicar),
    "4":("Dividir",dividir),
    "0":("Salir",)}

opcion = -1
while opcion!=0:
    for opcion_menu in calculadora:
        print(opcion_menu+":"+calculadora[opcion_menu][0])
    opcion = input("Introduce una opcion:")
    if opcion=="0":
        break
    operando1 = float(input("Operando 1:"))
    operando2 = float(input("Operando 2:"))
    resultado = calculadora[opcion][1](operando1, operando2)
    print("Resultado:",resultado)