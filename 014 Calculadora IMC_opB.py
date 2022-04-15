import winsound
DURACION_PITIDO = 1000
altura = float (input("Introduce tu altura en metros:"))
peso = float (input("Introduce tu peso en kg:"))
imc = peso/ altura**2
print("%.2f" %imc)#redondear a dos decimales
winsound.Beep(int(imc)*10,DURACION_PITIDO)
rango = ""
if (imc>=40):
    rango="Obesidad muy severa"
elif (imc>=35):
    rango="Obesidad severa"
elif (imc>=30):
    rango="Obesidad moderada"
elif (imc>=25):
    rango="Sobrepeso"
elif (imc>=18.5):
    rango="Peso saludable"
elif (imc>=16):
    rango="Delgadez"
elif (imc>=15):
    rango="Delgadez severa"
else:
    rango="Delgadez muy severa"
print("Tu estado es:",rango)
