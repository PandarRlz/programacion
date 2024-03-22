Algoritmo tarea_enunciado_n3
	Definir monto,montoF,descuento Como Entero
	Escribir "El monto a pagar es de: $" Sin Saltar
	Leer monto
	
	descuento=monto*15/100
	montof=monto-descuento
	si monto>=50000 Entonces
		Escribir "El descuento aplicado es del 15%"
		Escribir "Y su monto final con el descuento aplicado es: $",montof
	SiNo
		Escribir "El monto final no tiene descuento y su precio final es: $",monto
	FinSi
	
FinAlgoritmo
