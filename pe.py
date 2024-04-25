#varibla min si quiero el menor de 7 debo iniciarla en 8 y si quiero la mayor -1 max
cant=int(input("Ingrese cantidad de personas: "))
cont=0
sumaedad=0
contedad=0
contmuj=0
mayoredad=0
while cont<cant:
    cont+=1
    print("\n\tDatos persona N°"+str(cont))
    edad=int(input("Ingrese edad: "))
    genero=input("Genero [M]: masculino, [F]: femenino ").upper()
    if(genero=="M"):
        sumaedad+=edad
        contedad+=1

    if(genero=="F" and edad>30):
        contmuj+=1
    if(edad>mayoredad):
        mayoredad=edad
    

if(contedad!=0):
    promedio=sumaedad/contedad
    print("El promedio de edad de los hombres es: ",promedio)
else:
    print("No se ingresaron hombres")

print("Cantidad de mujeres mayores a 30 años: ",contmuj)
print("La edad mayor es: ",mayoredad)