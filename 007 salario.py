salario = input("Introduce el salario bruto anual:")
if salario[1:].isdigit() is True:
    salario= int(salario)
    if salario > 0:
        pagas = int(input("Indicar si 12 meses o 14 meses:"))
        salarioMensual = salario/pagas
        print("Salario bruto mensual es:", salarioMensual, "€ en", pagas, "pagas")
    else:
        print("salario negativo")
else:
    print("Error, datos mal introducidos")