Algoritmo ejercicio1siysino
	definir alumno Como Caracter
	definir notaP,notaE,notaF Como real
	Escribir "Ingrese el nombre del alummno: "
	leer alumno
	escribir "El alumno ",alumno, " en su nota de presentacion saco: " Sin Saltar
	leer notaP
	Escribir "Y la nota de examen fue de: " Sin Saltar
	leer notaE
	notaP=0.6*notaP
	notaE=0.4*notaE
	notaF=notaE+notaP
	Si notaF >= 3.95 Entonces
		Escribir "Felicidades " ,alumno, " aprobo con una nota de: ",notaF
		
	SiNo
		Escribir "Lamentablemente ",alumno," Repobro con un: ",notaF
	FinSi
	
FinAlgoritmo
