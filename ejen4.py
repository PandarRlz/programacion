opcion=1
while(opcion!=4):
    opcion=int(input("1.-Triangulo\n2.-Cuadrado\n3.-Circulo\n4.-Salir \n\tElija opcion:"))
    if(opcion==1):
        print("Triangulo")
        base=int(input("Ingrese la base:"))
        altura=int(input("Ingrese la altura:"))

        area=base*altura/2

        print("El area del triangulo es:",area)

    elif(opcion==2):
        print("Cuadrado")
        lado=int(input("Ingrese el lado:"))

        area=lado*lado

        print("El area del cuadrado es:",area)

    elif(opcion==3):
        print("Circulo")
        radio=int(input("Ingrese el radio:"))

        area=3.1416*radio*radio

        print("El area del circulo es:",area)

    elif(opcion==4):
        print("Gracias por usar el programa")
        breaking=input("Presione enter para continuar")
        break

    else:
        print("Opcion no valida")