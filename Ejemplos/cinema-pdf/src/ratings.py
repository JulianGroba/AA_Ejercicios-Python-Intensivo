def ratings(diccionario):
    try:
        r=diccionario["Ratings"]
        keys= []
        values = []

        for i in r:
            
            for k,v in i.items():
                keys.append(k)
                values.append(v)
        return values
    except:
        print("Error")

def añadir_lista(datos, lista_datos):
    for i in range(len(datos)):
        #print(datos[i])
        lista_datos.append(datos[i])
    return lista_datos