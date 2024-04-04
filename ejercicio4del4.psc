Proceso sin_titulo
	Definir t_entrada,t_p Como Caracter
	Definir valor_t Como Entero
	Escribir "Ingrese el tipo de entrada que desea: [PLATEA] [TRIBUNA] [GALERIA] " Sin Saltar
	Leer t_entrada
	t_entrada=Mayusculas(t_entrada)
	//si quieres que sea mayuscula primero pides t_entrada y despues el t_entrada=mayuscula(t_entrada)
	
	Escribir "Ingrese el tipo de público: [ESTUDIANTE] [GENERAL]" Sin Saltar
	leer t_p
	t_p=Mayusculas(t_p)
	
	
	si (t_entrada="PLATEA" y t_p="ESTUDIANTE")Entonces
		valor_t=9000
	FinSi
	Si (t_entrada="PLATEA" y t_p="GENERAL")Entonces
		valor_t=15000
	FinSi
	
	si (t_entrada="TRIBUNA" y t_p="ESTUDIANTE")Entonces
		valor_t=5000
	FinSi
	Si (t_entrada="TRIBUNA" y t_p="GENERAL")Entonces
		valor_t=9000
	FinSi
	
	si (t_entrada="GALERIA" y t_p="ESTUDIANTE")Entonces
		valor_t=3500
	FinSi
	Si (t_entrada="GALERIA" y t_p="GENERAL")Entonces
		valor_t=5200
	FinSi
	
	Escribir "****** VAMOS A DISFRURAR ********"
	Escribir "Tipo de entrada => ",t_entrada
	Escribir "Tipo de público => ",t_p
	Escribir "Valor a pagar: $ ",valor_t

FinProceso
