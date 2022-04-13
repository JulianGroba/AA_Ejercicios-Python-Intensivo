importe1 = float(input("Incluir importe 1:"))
importe2 = float(input("Incluir importe 2:"))
iva= float(input("Indicar el IVA:"))
iva= (iva/100)+1
facturaTotal = (importe1+importe2)*iva
dif= facturaTotal-(importe1+importe2)
print("La factura es "+str(facturaTotal)+"€, de los importes "+str(importe1)+"€ y "+str(importe2)+"€ del cual el IVA es "+str(dif) +"€.")