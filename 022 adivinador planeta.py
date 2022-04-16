import random
lista = ["Mercurio","Tierra","Venus","Marte","Jupiter","Saturno","Urano","Neptuno","Pluton"] 
lista_upper = [x.upper() for x in lista]
planeta_secreto = random.choice(lista_upper)
print("La siguiente lista;", lista)
planeta = input("Adivinar el planeta:").upper()
numError=0
#Para hacer comprobaciones
#print(planeta_secreto)
while planeta!=planeta_secreto:
    print("No has acertado.")
    numError+=1
    lista_upper.remove(planeta)
    print("La siguiente lista;", lista_upper)
    planeta = input("Indicar un planeta de la:").upper()
else:
    print("Has acertado con el siguiente número de intentos:", numError)
    print("El planeta secreto era:",planeta_secreto.capitalize())
if numError==0:
    print("Juego Terminado sin errores")
else:
    print("Juego Terminado")