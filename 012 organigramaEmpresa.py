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
dep1 = ["Contabilidad"]
dep2 = ["Técnicos"]

empleado1 = ["Pablo", "Técnico"]
empleado2 = ["Cristian", "Manager"]
empleado3 = ["Pakito", "Técnico"]
empleado4 = ["Manolo", "Ayudante"]
empleado5 = ["Beaver", "Manager"]
empDep1 = [empleado5,empleado4]
empDep2 = [empleado1,empleado2,empleado3]
dep1.append(empDep1)
dep2.append(empDep2)
emp.append(dep1)
emp.append(dep2)
#mostrar el 2 empleado del segundo dep
print(dep2[1][1][0])
#mostrar todos los datos
for depa in emp:
    print("Departamento:", depa[0])
    for empl in depa[1]:
        print("--Nombre:", empl[0])
        print("--Categoria:",empl[1])

