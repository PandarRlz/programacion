import random
dia=0
#sum hace que se sumen ejemplo promedio=sum(temperaturas_generadas)/len(temperaturas_generadas)
#suma las temperaturas osea todas y len cuentas cuantas temperaturas se generaron y se divide por la cantidad que se genero (si genera 5 se divide por 5)
ban=0#chanta una bandera
op=1

while(op!=7):
    op=int(input('''	        ******* Mirando el sol ******
    1.	Generar
    2.	Mostrar
    3.	Promedio semanal
    4.	Bajo cero
    5.	Día con mayor temperatura
    6.	Temperaturas ordenadas ascendentemente
    7.	Salir
    \tElija Opción:'''))

    if (op==1):#generar
        ban=1
        temperaturas_generadas = []
        for i in range(7):
            #temperaturas_generadas.append(round(random.uniform(-10, 39), 1))
             temperaturas_generadas = [round(random.uniform(-10, 39), 1) for i in range(7)]
        print("Temperatura generada satifactoriamente! ")

    if (op==2):#mostrar
        if(ban==0):
            print("Debe generar las temperaturas! ")
        else:
            for i in range(len(temperaturas_generadas)):
                print(f"Dia N° {i+1} = {temperaturas_generadas[i]}")

    if (op==3):#promedio
        if(ban==0):
            print("Debe generar las temperaturas! ")
        else:
            suma=0
            for e in temperaturas_generadas:
                suma+=e
            promedio=suma/len(temperaturas_generadas)
            print(f"El promedio es: {round(promedio,1)}")

    if (op==4):#mostrar bajo cero
        if(ban==0):
            print("Debe generar las temperaturas! ")
        else:
            dia=[]
            for i in range (len(temperaturas_generadas)):
                if(temperaturas_generadas[i]<0):
                    dia.append(i)
            if(len(dia)==0):
                print(f"No hubo temperatura bajo cero")
            else:
                print(f"Las temperaturas bajo cero fueron: ")
                for elem in dia:#elem toma el indice de dia osea elem=dia
                    print(f"Dia N° {elem+1} = {temperaturas_generadas[elem]}")

    if (op==5):
        if(ban==0):
            print("Debe generar las temperaturas! ")
        else:
            dia=[]
            for i in range (len(temperaturas_generadas)):
                if(temperaturas_generadas[i]>0):
                    dia.append(i)
            if(len(dia)==0):
                print(f"No hubo temperatura maxima")
            else:
                print(f"Las temperaturas maximas fueron: ")
                for elem in dia:#elem toma el indice de dia osea elem=dia
                    print(f"Dia N° {elem+1} = {temperaturas_generadas[elem]}")
    if (op==6):
        if(ban==0):
            print("Debe generar las temperaturas! ")
        else:
            print("Debe ingresar la opcion 1")