/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package ejercicio1;
import java.util.Scanner;
public class Ejercicio1 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        int op;
        String nom;
        
        int uno,dos,res;
        char sexo;
        double altura;
        Scanner teclado=new Scanner(System.in);
        
        
        do
        {
            System.out.print("\n\nCositas\n" +
            "******\n" +
            "1.Saludar\n" +
            "2.Sumar 2 números\n" +
            "3.Estatura\n" +
            "4.Salir\n" +
            "     Elija Opción: ");
            op=teclado.nextInt();
            switch(op)
                    {
                case 1:
                System.out.print("Ingrese su nombre: ");
                teclado.nextLine();
                nom=teclado.nextLine();
                System.out.println("Hola "+nom+", bienvenido a Java");
                break;
                case 2:
                System.out.println("Ingrese un numeros para sumarlo");
                uno=teclado.nextInt();
                System.out.println("Ingrese segundo numero ");
                dos=teclado.nextInt();
                res=uno+dos;
                System.out.println("La suma total de "+uno+"+ "+dos+"Es = "+res);
                break;
                case 3:
                System.out.println("Ingrese el Sexo F o M: ");
                sexo=teclado.next().charAt(0);
                sexo=Character.toUpperCase(sexo);
                System.out.println("Ingrese la altura: ");
                altura=teclado.nextDouble();
                System.out.println("Usted midue "+altura+"Y es de sexo "+sexo);
                
                if(sexo=='F')
                {
                    if(altura>=1.63)
                    {
                        System.out.println("Su estatura es alta ");
                    }
                    if(altura<=1.55)
                    {
                        System.out.println("Su estatura es baja ");
                                            }
                    if(altura<1.63 && altura>1.55)
                    {
                        System.out.println("Su estatura es mediana ");
                    }
                      
                }
                if(sexo=='M')
                {
                    if(altura>=1.67)
                    {
                        System.out.println("Su estatura es alta ");
                    }
                    if(altura<=1.6)
                    {
                        System.out.println("Su estatura es baja ");
                                            }
                    if(altura<1.67 && altura>1.6)
                    {
                        System.out.println("Su estatura es mediana ");
                    }
                    break;
                }
                
            }
        }while(op!=4);
        
        
        
        
        
    }//main
    
}//clase
