personas = [
    ["Ferjando",1971,"Madrid"],
    ["Francisco",1988,"Badajoz"],
    ["Javier",1990,"Tarragona"],
    ["Jose",1973,"Guadalajara"],
    ["Federica",1999,"Lugo"]
    ]
inicial = input("Introduce la inicial del nombre a consultar:")
año = input("Indicar el año hasta el que se realiza la consulta:")

#Opción 1. Utilizando filter y una función de validación
def validos(p):
    return p[0].startswith(inicial) and int(año)>p[1]

filtrados = filter(validos, personas)
print(list(filtrados))

#Opción 2. Utilizando filter y una función lambda
filtrados2 = filter(lambda p: p[0].startswith(inicial) and int(año)>p[1], personas)
print(list(filtrados2))
