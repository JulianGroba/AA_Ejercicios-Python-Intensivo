import hashlib

candidatas = ["baseball","football","shadow","mustang","superman","jordan","soccer"]

hash = '136c67657614311f32238751044a0a3c0294f2a521e573afa8e496992d3786ba'

def obtener_hash(password):
    encoded = password.encode()
    resumen = hashlib.sha256(encoded)
    return resumen.hexdigest()

for p in candidatas:
    pr = obtener_hash(p)
    if pr == hash:
        print("La contraseña buscada es:", p)
        break
    #esto no haría falta:
    else:
        print("La contraseña no es:", p)
#si la contraseña encriptada no está en la lista definida. 
else:
    print("Contraseña no encontrada.")