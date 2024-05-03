n=int(input("\n\tIngrese cantidad de clientes: "))
cont=0
totalRec=0
cantMayo=0
masDe4=0
while(cont<n):
    cont+=1
    resp="S"
    totalAPagar=0 
    cantCompra=0
    while(resp=="S"):
        op=int(input('''\n******** Cliente   N° '''+str(cont)+''' ******** 
================================
    [1]-> Churrasco solo 
    [2]-> Churrasco italiano
    [3]-> Churrasco Mayo 
        Elija Opción:'''))
        cantidad=int(input("Cantidad: "))
        cantCompra+=cantidad
        if(op==1):
            valor=3500
        elif(op==2):
            valor=4800
        else:
            valor=4000
            cantMayo+=cantidad
        subTotal=valor*cantidad
        totalAPagar+=subTotal
        resp=input("\n\tDesea llevar otro producto S/N").upper()
    print("\n\tDebe cancelar $"+str(totalAPagar))
    totalRec+=totalAPagar
    if(cantCompra>4):
        masDe4+=1
print("\n\n\tEstadísticas")
print("Total recaudado $"+str(totalRec))
print("Cantidad Churrasco Mayo: "+str(cantMayo))
print("Cantidad de clientes que compraron más de 4: "+str(masDe4))

