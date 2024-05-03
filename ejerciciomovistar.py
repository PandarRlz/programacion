cont=0
cant_cliente=0
total_recaudado=0
mayor_venta=0
cant_totalprimerafila=0
cont_diamante=0
cont_diamantel=0
cont_plateabajadiamante=0
opcion=0
cargo=0
cant_ventaonline=0
cont_entradas=0
while(cont==opcion):

    opcion=int(input('''******* MOVISTAR ARENA *******
==============================
[1]-> Primeras Filas
[2]-> Diamante
[3]-> Diamante Lateral
[4]-> Platea Baja Diamante
[5]-> Reportes
[6]-> Salir del Sistema
==============================
Elija Opción:'''))
    cantidad_entradas=int(input("Cuantas entradas desea: "))
    if(opcion==1):
        valor=180000
        cargo=18000
        total_apagar=cantidad_entradas*valor
        cant_totalprimerafila+=1
        cant_ventaonline+=1
        cont_entradas+=cantidad_entradas
        print("Ubicacion: Primera Filas ")
        print("El monto total a pagar es: $",total_apagar)
    if(total_apagar>=mayor_venta):
        mayor_venta=total_apagar  

    elif(opcion==2):
        valor=165000
        cargo=16500
        total_apagar=cantidad_entradas*valor
        cant_ventaonline+=1
        cont_entradas+=cantidad_entradas
        print("Ubicacion: Diamante ")
        print("El monto total a pagar es: $",total_apagar)
    if(total_apagar>=mayor_venta):
        mayor_venta=total_apagar  

    elif(opcion==3):
        valor=145000
        cargo=14500
        total_apagar=cantidad_entradas*valor
        cant_ventaonline+=1
        cont_entradas+=cantidad_entradas
        print("Ubicacion: Diamante Lateral ")
        print("El monto total a pagar es: $",total_apagar)
    if(total_apagar>=mayor_venta):
        mayor_venta=total_apagar   

    elif(opcion==4):
        valor=115000
        cargo=11500
        total_apagar=cantidad_entradas*valor
        cant_ventaonline+=1
        cont_entradas+=cantidad_entradas
        print("Ubicacion: Platea Baja Diamante ")
        print("El monto total a pagar es: $",total_apagar)
    if(total_apagar>=mayor_venta):
        mayor_venta=total_apagar    

    tipo_compra=input("[Presencial] [Online] ")
    if(tipo_compra=="Presencial"):
        cargo*=cantidad_entradas
        total_apagar+=cargo
        print("El total a pagar es de: $",total_apagar,"más el cargo\nque es $",cargo)

    else:
        print("Su compra no tiene recargo ")

        