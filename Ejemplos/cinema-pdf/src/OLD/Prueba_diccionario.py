import logging
import lector_json_generico as lector

url = "https://it-python-admin.github.io/peliculas/indiana-last-crusade.json"

diccionario_pelis = lector.get_dict_from_json_url(url)

titulo = diccionario_pelis["Title"]
director = diccionario_pelis["Director"]
fecha = diccionario_pelis["Released"]
ratings = diccionario_pelis["Ratings"]
list = []

"""
for k, v in ratings.items():
    variable = ratings[0]+ratings[1]
    list.append(variable)
    print(list)


"""
def ratings():
    r=diccionario_pelis["Ratings"]
    keys= []
    values = []

    for i in r:
        logging.debug("Entrando en primer buclu for")
        for k,v in i.items():
            keys.append(k)
            values.append(v)
    return values
        
#print (keys, values)
print (ratings())


ratingskey = diccionario_pelis["Ratings"][0]


#print(ratings.count())

#print(ratings)


def ratings():
    r=diccionario_pelis["Ratings"]
    keys= []
    values = []

    for i in r:
        
        for k,v in i.items():
            keys.append(k)
            values.append(v)
    return values

def añadir_lista(datos, lista_datos):
    for i in range(len(datos)):
        print(datos[i])
        lista_datos.append(datos[i])
    return lista_datos