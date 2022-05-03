class NombreCortoError(Exception):
    pass

class EdadInsuficienteError(Exception):
    pass

class MalGustoError(Exception):
    pass


def calculadora_persona(nombre : str, edad : int, color: str):
    """
    Ejercicio clase para los TypeErrors creados por un Usuario.
    """
    if len(nombre) < 3:
        raise NombreCortoError
    if edad < 18:
        raise EdadInsuficienteError
    if color.upper() == "NARANJA":
        raise MalGustoError
    #else:
        #print(("El nombre {n} tiene la siguiente edad {e} y su color favorito es {c}.").format(n = nombre, e = edad, c = color))

nombre = input("Indtroducir nombre:")
edad = int(input("Introducir edad:"))
color = input("Introducir color preferido:")

try:
    calculadora_persona(nombre, edad, color)
except NombreCortoError:
    print("El nombre no es suficientemente largo")
except EdadInsuficienteError:
    print("No se admiten menores de edad")
except MalGustoError:
    print("Tienes un gusto pésimo para los colores")
else:
    print("Has pasado todos los filtros")
