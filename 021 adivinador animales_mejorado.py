animals = ["Dog", "Cat", "Bird", "Cow", "Snake"]
animal = input("Introduce un animal en inglés:")
numError = 0
#asegurar que todo será en mayúsculas.
animals_upper = [x.upper() for x in animals]
while animal.upper() not in animals_upper:
    numError+=1
    print("No incluido en lista")
    animal = input("Introduce un animal en inglés:")
else:
    print("Has acertado, con el siguiente número de errores:", numError)
print("Juego Terminado")