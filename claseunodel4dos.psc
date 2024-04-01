Algoritmo sin_titulo
	definir valorcompra,desc1,desc2,totaldesc,totalpago Como Entero
	definir liquidacion Como Caracter
	Escribir "Ingrese el valor de la compra: " Sin Saltar
	leer valorcompra
	Escribir "Esta en liquidacion? S/N: " Sin Saltar
	leer liquidacion
	desc1=0
	desc2=0
	si(valorcompra >=100000 y valorcompra<=500000) Entonces
		desc1=Redon(valorcompra*0.05)
	FinSi
	si (valorcompra>=500000) Entonces
		desc1=redon(valorcompra*0.1)
	FinSi
	si (Mayusculas(liquidacion)="S") Entonces
		//si(liquidacion="S" o liquidacion"s")entonces
		desc2=redon(valorcompra*0.03)
	FinSi
	totaldesc=desc1+desc2
	totalpago=valorcompra-totaldesc
	Escribir "Valor compra: ",valorcompra
	Escribir "Total descuanto: ",totaldesc
	Escribir "Total a pagar: ",totalpago
FinAlgoritmo
