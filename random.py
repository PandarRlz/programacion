import random
n=int(input("Ingrese la cantidad que desea generar: "))
cont=0
sumapar=0
mayor=-201
contdos=0
menor=201
conttres=0
while(cont<n):
    cont+=1
    num=random.randint(-200,200)
    print(num,end=", ")
    if(num%2==0 and num>0):
        sumapar+=num
    if(num>mayor):
        mayor=num
    if(num<menor):
        menor=num
    if(((num>-100 and num<-9) or (num>9 and num<100))):
        contdos+=1
    if(abs(num)%10==3):
        conttres+=1
print("\n***************Estadisticas****************")
print("\n\tCantidad pares positivos",sumapar)
print("\tMayor",mayor)
print("\tMenor",menor)
print("\tCantidad de numeros con dos digitos: ",contdos)
print("\tCantidad de numeros que terminan en 3: ",conttres)