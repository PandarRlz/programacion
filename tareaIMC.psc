Algoritmo sin_titulo
	Definir peso,altura,IMC Como Real
	Escribir "Ingrese el peso: " Sin Saltar
	leer peso
	Escribir "Ingrese la altura: " Sin Saltar
	leer altura
	//calculamos el imc
	IMC = peso/altura^2
	
	Si imc < 18.5 Entonces
		escribir "Usted tiene BAJO PESO"
	FinSi
	si imc >= 18.5 y imc > 24.9 Entonces
		Escribir "Usted tiene PESO SALUDABLE"
	FinSi
	si imc >= 24.9 y imc < 29.9 Entonces
		Escribir "Usted tiene SOBRE PESO"
	FinSi
	si imc >= 29.9 Entonces
		Escribir "Usted es OBESO);"
	FinSi

	
FinAlgoritmo
