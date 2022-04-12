PALABRA_PROHIBIDA1 = "ADMIN"
PALABRA_PROHIBIDA2 = "123"
PALABRA_PROHIBIDA3 = "PASSWORD"

usuario = input("Introduce el nombre de usuario:")
contraseña = input("Introduce una contraseña:")
if PALABRA_PROHIBIDA1 or PALABRA_PROHIBIDA2 or PALABRA_PROHIBIDA3 in contraseña:
    print ("Contraseña no válida")
else:
    print("Contraeeña válida")
