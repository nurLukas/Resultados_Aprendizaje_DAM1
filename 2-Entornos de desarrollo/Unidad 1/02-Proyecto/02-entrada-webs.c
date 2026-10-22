/*
    Calculadora STURMPROJEKT
    Version 0.2 - Entrada de datos por teclado
*/

#include <stdio.h>

int main(){
    // Declaro las variables
    int webs;
    float precioWeb = 250;
    float ingresos;

    // Pido los datos
    printf("CALCULADORA STURMPROJEKT\n");
    printf("Cuantas webs has vendido este mes? ");
    scanf("%i", &webs);

    // Calculo los ingresos
    ingresos = webs * precioWeb;

    // Muestro los resultados
    printf("Webs vendidas: %i\n", webs);
    printf("Precio por web: %.2f euros\n", precioWeb);
    printf("Ingresos del mes por webs: %.2f euros\n", ingresos);

    return 0;
}