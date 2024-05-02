opcion=1
cont=0
totalrec=0
cant_mayo=0
masde4=0#va afuera del while porque si esta dentro cada vez que inicie el programa partira de 0 y Cantidad de clientes que compraron más de 4 churrascos
n=int(input("Cantidad de clientes: "))
while(cont<n):
    total_apagar=0
    cont+=1
    resp="S"
    cant_compra=0
    while(resp=="S"):
        print("********* Cliente N°"+str(cont)+"***************")
        opcion=int(input("1.-Churrasco solo\n2.-Churrasco italiano\n3.-Churrasco mayo\n4.-Salir \n\tElija opcion:"))
        cant=int(input("Cantidad que desea: "))
        cant_compra+=cant#Cantidad de clientes que compraron más de 4 churrascos
        if(opcion==1):
            print("Churrasco solo")
            valor=3500

        if(opcion==2):
            print("Churrasco italiano")
            valor=4800

        else:
            valor=4000
            cant_mayo+=cant
    
        subtotal=valor*cant
        total_apagar+=subtotal
        resp=input("\n\tDesea llevar otro producto S/N ").upper()
    print("\n\tDebe cancelar $"+str(total_apagar))
    totalrec+=total_apagar
    if(cant_compra>4):#Cantidad de clientes que compraron más de 4 churrascos
        masde4+=1
print("Cantidad total recaudado es: $",totalrec)
print("Cantidad churrasco mayo es: ",cant_mayo)
print("Cantidad de clientes que compraron mas de 4 churrascos ",masde4)