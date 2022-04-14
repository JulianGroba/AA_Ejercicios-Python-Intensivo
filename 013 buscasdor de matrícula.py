C4 = ("Citroen", "C4", "Negro")
SV650A = ("Suzuki", "SV650A", "Negro")
Micra = ("Nissan", "Micra", "Cobre")
diccionario ={"4379-GKB":C4, "3701-KFH": SV650A, "8920-GBR": Micra}
matricula = input("Indicar matrícula a buscar: ")
if matricula in diccionario:
    print(diccionario[matricula])
else:
    print("Matrícula no incluida en base de datos.")