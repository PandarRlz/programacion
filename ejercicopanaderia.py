tipo_pan=input("Eligael tipo de pan [C]:corriente, [S]:sesamo, [F]:frica, [M]:molde ")
cant_kilos=int(input("Cantidad de kilos que desea: "))
precio=int(input("El precio por kilo de pan es de: $"))
tipo_pago=input("El tipo de pago es: [efectivo], [tarjeta] ")


total_apagar=cant_kilos*precio
desc=0

if tipo_pan=="C":
    desc=0
    nombre_pan="Corriente"
elif tipo_pan=="S":
    desc= precio*0.10
    nombre_pan="Sesamo"
    #total_apagar=(precio-desc)*cant_kilos
elif tipo_pan=="F":
    desc= precio*0.15
    nombre_pan="Frica"
    #total_apagar=(precio-desc)*cant_kilos
elif tipo_pan=="M":
    desc= precio*0.08
    nombre_pan="Molde"
    #total_apagar=(precio-desc)*cant_kilos

else:
    print("ERROR INVALDO")


if tipo_pago=="efectivo":
    desc2= precio*0.07
else:
    desc2=0

total_apagar=(precio-desc-desc2)*cant_kilos

print("*************** Panadería MAsitas **************")
print("Cantidad Kilos:",cant_kilos,"Tipo de pan: ",tipo_pan)
print("Total descuento:",round(desc2),"Total a pagar: $",round(total_apagar))
print("************************************************")