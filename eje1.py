
nota_e=(float(input("Ingrese la nota del examen: ")))
pp=(float(input("Ingrese la nota uno :")))
sp=(float(input("Ingrese la nota dos: ")))
tp=(float(input("Ingrese la nota tres: ")))
nota_p=pp*0.25+sp*0.35+tp*0.40
nf=nota_p*0.6+nota_e*0.4
print("El promedio es "+str(round(nf,1)))