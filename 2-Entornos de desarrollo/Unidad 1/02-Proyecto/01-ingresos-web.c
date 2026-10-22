/*
    Calculadora STURMPROJEKT
    Version 0.1 - Ingresos por paginas web
*/

#include <stdio.h>

int main(){
    // Declaro las variables
    int webs = 3;
    float precioWeb = 250;
    float ingresos;

    // Calculo los ingresos
    ingresos = webs * precioWeb;

    // Muestro los resultados
    printf("CALCULADORA STURMPROJEKT\n");
    printf("Webs vendidas: %i\n", webs);
    printf("Precio por web: %.2f euros\n", precioWeb);
    printf("Ingresos: %.2f euros\n", ingresos);

    return 0;
}