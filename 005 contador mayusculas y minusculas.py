texto = input("introduce tu texto a buscar:")
textomayus= texto.upper()
frase = "En un lugar de La Mancha, LA MANCHA ES UNA REGION"
frasemayus = frase.upper()
numocu = frasemayus.count(textomayus)
print("El texto", texto, "ha aparecido", numocu, "veces.")