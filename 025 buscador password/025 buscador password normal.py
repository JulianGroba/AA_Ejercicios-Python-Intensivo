import hashlib

candidatas = ["baseball","football","shadow","mustang","superman","jordan","soccer"]

hash = '136c67657614311f32238751044a0a3c0294f2a521e573afa8e496992d3786ba'

def obtener_hash(password):
    encoded = password.encode()
    resumen = hashlib.sha256(encoded)
    return resumen.hexdigest()

fichero = input("Introduce el nombre del fichero con las hash:")
password = input("Introduce una contraseña:")
password_hash = obtener_hash(password)
fichero = open(fichero)
current_hash = fichero.readline().replace("\n","")
while current_hash:
    if current_hash==password_hash:
        print("NO SIRVE")
        break
    current_hash = fichero.readline().replace("\n","")
else:
    print("NO PROBLEMO")
fichero.close()