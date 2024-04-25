
n=int(input("Ingresa la cantidad de numeros: "))
cont=0
gen=2
print("\n\tLos "+str(n)+" primeros pares positivos son: ",end=" ")#en es para usar tipo sin saltar y lea para el lado
while (cont<n):
    cont+=1
    print(gen,end=", ")
    gen+=2