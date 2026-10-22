/*
    Calculadora STURMPROJEKT
    Version 0.3 - Webs y hosting
*/

#include <stdio.h>

int main(){
    // Declaro las variables
    int webs;
    int clientesHosting;
    float precioWeb = 250;
    float precioHosting = 35;
    float ingresosWebs;
    float ingresosHosting;
    float ingresosMes;

    // Pido los datos
    printf("CALCULADORA STURMPROJEKT\n");

    printf("Cuantas webs has vendido este mes? ");
    scanf("%i", &webs);

    printf("Cuantos clientes de hosting tienes este mes? ");
    scanf("%i", &clientesHosting);

    // Calculo los ingresos
    ingresosWebs = webs * precioWeb;
    ingresosHosting = clientesHosting * precioHosting;
    ingresosMes = ingresosWebs + ingresosHosting;

    // Muestro los resultados
    printf("\nINGRESOS DEL MES\n");
    printf("Desarrollo de webs: %.2f euros\n", ingresosWebs);
    printf("Hosting y mantenimiento: %.2f euros\n", ingresosHosting);
    printf("Total: %.2f euros\n", ingresosMes);

    return 0;
}