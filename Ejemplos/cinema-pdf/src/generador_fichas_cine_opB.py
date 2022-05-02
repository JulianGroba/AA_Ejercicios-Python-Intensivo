import lector_json_generico as lector
import descargador_imagenes as descargador
import generador_pdf as generador
import ratings as ratings

url = "https://it-python-admin.github.io/peliculas/indiana-last-crusade.json"

def generar_ficha(url):
    #Obtener los datos JSON del servidor y generar diccionario
    diccionario_pelis = lector.get_dict_from_json_url(url)
    #Obtener los datos
    titulo = diccionario_pelis["Title"]
    director = diccionario_pelis["Director"]
    fecha = diccionario_pelis["Released"]
    datos = ratings.ratings(diccionario_pelis)
    imagen = diccionario_pelis["Poster"]
    #Generar el título del fichero PDF de salida
    nombre_fichero_salida = "./src/"+titulo+".pdf"
    #Obtener el fichero de imagen
    nombre_fichero_imagen = "./src/imagen.jpg"
    descargador.get_image_from_url(imagen, nombre_fichero_imagen)
    #Montamos la lista con los datos
    lista_datos = [titulo, director, fecha]
    #Añadimos los rattings a la lista ya creada
    ratings.añadir_lista(datos, lista_datos)
    #Generar el pdf
    generador.generar_pdf(nombre_fichero_salida, lista_datos, nombre_fichero_imagen)
    print("Fichero creado")


generar_ficha(url)

