Proceso sin_titulo
	Definir t_usuario,horario Como Caracter
	Definir Valor_p Como Entero
	Escribir "Ingrese su tipo de usuario: (ADULTO MAYOR) (ESTUDIANTE) (ADULTO)" Sin Saltar
	leer t_usuario
	Escribir "Ingrese horario: (PUNTA) o (NORMAL)" Sin Saltar
	leer horario
	si(Mayusculas(t_usuario)="ESTUDIANTE" y Mayusculas(horario)="NORMAL") Entonces
		Valor_p=490
	FinSi
	si(Mayusculas(t_usuario)="ESTUDIANTE" y Mayusculas(horario)="PUNTA") Entonces
		Valor_p=590
	FinSi
	si(Mayusculas(t_usuario)="ADULTO" y Mayusculas(horario)="NORMAL") Entonces
		Valor_p=790
	FinSi
	si(Mayusculas(t_usuario)="ADULTO" y Mayusculas(horario)="PUNTA") Entonces
		Valor_p=890
	FinSi
	si(Mayusculas(t_usuario)="ADULTO MAYOR" y Mayusculas(horario)="NORMAL") Entonces
		Valor_p=390
	FinSi
	si(Mayusculas(t_usuario)="ADULTO MAYOR" y Mayusculas(horario)="PUNTA") Entonces
		Valor_p=490
	FinSi
	Escribir "*****************************************"
	Escribir "Usuario=>",t_usuario
	Escribir "Horario=>",horario
	Escribir "Valor Pasaje: $",Valor_p
	Escribir "*****************************************"
	Escribir "Gracias por Viajar con nosotros"
	
FinProceso
