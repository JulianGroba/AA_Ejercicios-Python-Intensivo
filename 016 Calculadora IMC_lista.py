referencias = [
    [0,"Delgadez muy severa"],
    [15,"Delgadez severa"],
    [16,"Delgadez"], 
    [18.5,"Peso Saludable"], 
    [25,"Sobrepeso"],
    [30,"Obesidad Moderada"], 
    [35,"Obesidad severa"], 
    [40,"Obesidad muy severa"]]
referencias.reverse()


altura = float (input("Introduce tu altura en metros:"))
peso = float (input("Introduce tu peso en kg:"))
imc = peso/ altura**2
print("%.2f" %imc)#redondear a dos decimales
rango = ""

for ref_actual in referencias:
    if (imc>=ref_actual[0]):
        rango = ref_actual[1]
        break

print("Tu estado es:",rango)
