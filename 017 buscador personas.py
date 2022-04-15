personas = [
    ["Ferjando",1971,"Madrid"],
    ["Francisco",1988,"Badajoz"],
    ["Javier",1990,"Tarragona"],
    ["Jose",1973,"Guadalajara"],
    ["Federica",1999,"Lugo"]
    ]
inicial = input("Introduce la inicial del nombre a consultar:")
año = input("Indicar el año hasta el que se realiza la consulta:")

resultado= []
temporal=""
for persona in personas:
    #print(persona)
    temporal = persona[0][0]
    #print(temporal)
    if inicial==temporal:
        if int(año) > persona[1]:
            resultado.append(persona)
        """"
        else:
            print("error2")
    else:
        #print(inicial)
        print("error1")
"""
print ("Mostrar todos los items cuya letra coincida con la introducida y hayan nacido antes del año indicado")
print(resultado)