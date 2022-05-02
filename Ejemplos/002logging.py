import requests
# instalar con pip install requests
import logging
#logging.getLogger().setLevel(logging.ERROR)#cambiar el mostrar en consola

logging.basicConfig(
    filename="fichero_salida.log", 
    filemode="a",
    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
    datefmt='%H:%M:%S', 
    level=logging.DEBUG)



def get_image_from_url(url : str, file_name : str):
    """
    Te aparece como ayuda cuando llamas a la función.
    Puedes indicar la salida de dicha función y lo que se espera para que funciones
    """
    logging.debug("Entrando en la función get_image_froom_url")
    logging.debug(f"Wl valor de la url es {url}")
    with open(file_name,"wb") as fichero:
        logging.debug("Entrando en el with get_image_froom_url")
        if ("WIKIPEDIA" in url.upper()):
            logging.warning("El usuario esta accediendon a un sitio web no aceptado.")
        else:
            #TODO mejorar el control de escepciones
            try:
                rq = requests.get(url)
                fichero.write(rq.content)
            except:
                logging.error("Ha ocurrido un error al ejecutar la función")