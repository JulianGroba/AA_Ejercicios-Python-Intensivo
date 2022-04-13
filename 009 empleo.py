MAYORIA_EDAD = 18
edad = int(input("Indicar la edad:"))
nac = input("Indicar la nacionalidad:")
idioma1 = input("Indicar el primer idioma:")
idioma2 = input("Indicar el segundo idioma:")

if edad >= MAYORIA_EDAD:
    if nac == "frances" or nac == "aleman" and nac !="ruso":
        if idioma1 == "ingles" or idioma1 == "chino" and idioma2 == "chino" or idioma2 == "ingles":
            print("Contratado")
        else:
            print("No habla inglés o chino. No contratado")
    else:
        print("No es francés o alemán o es ruso. No contratado")
else:
    print("Menor de edad, no puede ser contratado")