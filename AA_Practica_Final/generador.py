import random
NUMERODENOMBRES = 1000
NOMBREFICHERO = "datos.csv"
n = 0

def generar_listado_personas(numero):
    nombres = ("Julian","Fernando","Andres","Juan Luis", "Victor", "Emilio", "Antonio", "Cristian", "Kevin", "Diego")
    personas=[]
    for i in range(numero):
        nueva_persona = random.choice(nombres)
        personas.append(nueva_persona)
    return personas

def generar_valores_aleatorios():
    nuevo_valor = 0
    try:
        if n!=0:
            rango = range(n)
        else:
            rango = range(NUMERODENOMBRES)
    except:
        pass
    for i in rango:
        nuevo_valor = random.choice(rango)
    return nuevo_valor

def generar_excel():
    fichero = open(NOMBREFICHERO, "w")
    fichero.write("NOMBRE,VALOR\n")
    try:
        n = int(input("Intruzduca el valor n:"))
        personas = generar_listado_personas(n)
        for p in personas:
            v = generar_valores_aleatorios()
            fichero.write( p + "," + str(v) + "\n")      
    except ValueError:
            print("Valor introducido no es un entero, se procede con 1000")
            personas = generar_listado_personas(NUMERODENOMBRES)
            for p in personas:
                v = generar_valores_aleatorios()
                fichero.write( p + "," + str(v) + "\n")
    except:
        print("Proceso terminado sin ejecución")    
    fichero.close()
    print("Proceso terminado")
#Comprobación de funcionamiento.
#generar_excel()

