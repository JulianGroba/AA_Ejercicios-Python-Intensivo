class ValidacionError(Exception):
    def __init__(self, error_code):
        mensajes = ("Nombre corto", "Menor de edad", "Mal gusto")
        self.mensaje = mensajes [error_code]
        super().__init__(self.mensaje)

def validar(nombre, edad, color):
    colores_horribles = ["NARANJA"]
    if len(nombre)<3:
        raise ValidacionError(0)
    if edad<18:
        raise ValidacionError(1)
    if color in colores_horribles:
        raise ValidacionError(2)

nombre = input("Introduce tu nombre:")
edad = int(input("Introduce tu edad:"))
color = (input("Introduce tu color favorito:")).upper()

try:
    validar(nombre, edad, color)
except ValidacionError as error_validacion:
    print(error_validacion)
else:
    print("Has pasado todos los filtros")

