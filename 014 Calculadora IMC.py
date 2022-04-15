import winsound
altura = float (input("Introduce tu altura en metros:"))
peso = float (input("Introduce tu peso en kg:"))
imc = peso/ altura**2
print("%.2f" %imc)#redondear a dos decimales
winsound.Beep(350,500)
rango = ""
if (imc>=40):
    rango="Obesidad muy severa"
    winsound.Beep(800,1000)
elif (imc>=35):
    rango="Obesidad severa"
    winsound.Beep(700,1000)
elif (imc>=30):
    rango="Obesidad moderada"
    winsound.Beep(600,1000)
elif (imc>=25):
    rango="Sobrepeso"
    winsound.Beep(500,1000)
elif (imc>=18.5):
    rango="Peso saludable"
    winsound.Beep(400,1000)
elif (imc>=16):
    rango="Delgadez"
    winsound.Beep(300,1000)
elif (imc>=15):
    rango="Delgadez severa"
    winsound.Beep(200,1000)
else:
    rango="Delgadez muy severa"
    winsound.Beep(100,1000)
print("Tu estado es:",rango)
winsound.Beep(250,500)