MAYORIA_EDAD = 18
edad = int(input("Indicar la edad:"))
nac = input("Indicar la nacionalidad:")
idioma1 = input("Indicar el primer idioma:")
idioma2 = input("Indicar el segundo idioma:")

mayor_edad = edad >= MAYORIA_EDAD
nacionalidad_ok = (nac == "Frances" or nac =="Aleman") and nac !="Ruso"
idioma_ok = idioma1=="Ingles" and idioma2 == "Chino"

if mayor_edad and nacionalidad_ok and idioma_ok:
    print("Contratado")
else:
    print("No cumple el perfil")