cant_alum=int(input("Ingrese el numero de alumnos:"))
suma=0
cont=0

while(cont<cant_alum):
    edad=int(input("Ingrese la edad: "))
    cont+=1
    suma+=edad
promedio=suma/cant_alum
print("El promedio de las edades es"+str(promedio))

print("El total de alumnos es: "+str(cont))