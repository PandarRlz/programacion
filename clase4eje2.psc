Algoritmo sin_titulo
	definir edad Como Entero
	Definir num_p Como Real
	Definir hom,fem,sexo Como Caracter
	Escribir "Ingrese la edad que desea: " Sin Saltar
	leer edad
	Escribir "Ingrese el sexo masculino o femenino: " Sin Saltar
	leer sexo
	si Minusculas(sexo) = "femenino" Entonces
		num_p = (220 - edad) /10 
		Escribir "Su pulsacion por minuto es: ",num_p
	FinSi
	si Minusculas(sexo) = "masculino" Entonces
		num_p = (210 - edad) /10
		Escribir "Su pulsacion por minuto es: ",num_p
	FinSi
FinAlgoritmo
