"""
https://www.gutenberg.org/files/2000/2000-0.txt
1.Descargar el quijote del enlace.
2.Convertir el texto a string
3.Guardarlo en una lista (utilizando split)
4. Pedir al usuario una palabra y le vamos a decir cuantas veces aparece la palabra en el libro.
Tiene que ser independiente de si está escrito en mayúsculas o minúsculas (utilizando count de string)
5. Indicar si la palabra está o no (utilizando la lista) (utilizando in de la lista)
"""
import urllib.request
#conseguir la info
webUrl = urllib.request.urlopen ('https://www.gutenberg.org/files/2000/2000-0.txt')
data = webUrl.read()
#trabajar la info
data =str(data)
dataMayusculas= data.upper()
lista = dataMayusculas.split()
#pedir la palbra clave
palabraClave = input("Indicar la palabra clave:").upper()
recuento = data.count(palabraClave)
print("aparece "+str(recuento))
#comprobar si la palabra clave está en la lista
if palabraClave in lista:
    print("La palabra elegida aparece en el Quijote, la siguiente cantidad de veces: "+str(recuento))
else:
    print("La palabra clave no aparece en el Quijote")