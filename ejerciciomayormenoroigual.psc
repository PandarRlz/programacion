Proceso ejerciciomayormenoroigual
	definir num,numm Como Entero
	Escribir "Ingrese el primer numero: "
	leer num
	Escribir "Ingrese el segundo numero: "
	leer numm
	si (num mod numm =0) Entonces
		Escribir "el primer numero ",num," es divisible por ",numm
	sino 
		Escribir " el segundo ",num," no es divisible por ",numm
	FinSi
	si (numm mod num =0) Entonces
		Escribir " el primer ",numm," es divisible por ",num
	sino 
		Escribir " el primer ",numm," no es divisible por ",num
	FinSi
	si num>numm Entonces
		Escribir " El ",num," es mayor a ",numm
	FinSi
	si numm>num Entonces
		Escribir " El ",numm," es mayor a ",num
	FinSi
	si num=numm Entonces
		Escribir " Ambos numeros son iguales"
	FinSi
FinProceso
