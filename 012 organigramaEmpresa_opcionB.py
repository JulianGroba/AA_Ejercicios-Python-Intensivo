"""
UTILIZANDO LISTAS, CREAR LA SIGUIENTE ESTRUCTURA:
DOS DEPARTAMENTOS (primer dpto. 2 empleados, segundo dpto. 3 empleados)
Nombre
Empleados
Nombre
Categoría
Mostrar el segundo empleado del segundo departamento
¿Todos los empleados de todos los departamentos?
"""
emp = []
dep1 = []
dep2 = []
empDep1=[]
empDep2=[]
empleado1 = ["Pablo", "Técnico"]
empleado2 = ["Cristian", "Manager"]
empleado3 = ["Pakito", "Técnico"]
empleado4 = ["Manolo", "Ayudante"]
empleado5 = ["Beaver", "Manager"]
#insertar los departamentos a la empresa
emp.append(dep1)
emp.append(dep2)
#asiganamos nombres a los departamentos
dep1.append("Ventas")
dep2.append("Informática")
#asiganamos empleados a los departamentos
empDep1.append(empleado5)
empDep1.append(empleado4)
empDep2.append(empleado3)
empDep2.append(empleado2)
empDep2.append(empleado1)
dep1.append(empDep1)
dep2.append(empDep2)
#imprimir lista completa
print(emp)
#mostrar el 2 empleado del segundo dep
print(dep2[1][1][0])
#cambiar un nombre
empleado4[0]="Javier"
#mostrar todos los datos
for depa in emp:
    print("Departamento:", depa[0])
    for empl in depa[1]:
        print("--Nombre:", empl[0])
        print("--Categoria:",empl[1])
#buscar la categoría efr un empleado
introdyce_nombre_buscar = input("Introduce el nombre del empleado:")
for depa in emp:
       for empl in depa[1]:
           if empl[0]==introdyce_nombre_buscar:
                print(empl[0],"tiene la siguiente categoria:",empl[1],"en el departame3nto:", depa[0],".")
           """"
           elif empl[0]!=introdyce_nombre_buscar:
                print("Tr5abajador no incluido en base de datos o nombre mal escrito.")
"""