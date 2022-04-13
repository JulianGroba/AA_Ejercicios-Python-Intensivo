#Cuando se detecten 3 veces la misma IP se incluye a la misma en una lista negra.
#A partir de entonces, cuando se introduzca esa dirección IP se le muestra un mensaje de rechazo.
IP_SALIDA = 0
NUM_INT=3
x=-1
lista=[]
listaNegra=[]
while x!=IP_SALIDA:
    x=input("Introduce una direción IP:")
    if x in listaNegra:
        print("Usuario Bloqueado")
    elif (x != IP_SALIDA):
        lista.append(x)
        if (lista.count(x) == NUM_INT):
           listaNegra.append(x)
           print("Ip en lista negra")
        else:
            print(lista)
    else:
        print("Continue")
    

