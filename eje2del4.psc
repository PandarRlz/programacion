Proceso sin_titulo
	Definir x,i Como real
	Definir cuadrante Como Caracter
	Escribir "Ingerse la coordenada de x diferente de cero" Sin Saltar
	Leer x
	Escribir "Ingrese la coordenada de i diferente de cero" Sin Saltar
	leer i
	
	si(x>0 y i>0) Entonces
		Escribir "El punto ",x,",","Se encuentra en el I cuadrante."
	FinSi
	si(x<0 y i>0) Entonces
		Escribir "El punto ",x,",","Se encuentra en el II cuadrante."
	FinSi
	si(x<0 y i<0) Entonces
		Escribir "El punto ",x,",","Se encuentra en el III cuadrante."
	FinSi
	si(x>0 y i<0) Entonces
		Escribir "El punto ",x,",","Se encuentra en el IV cuadrante."
	FinSi
	
	FinProceso
