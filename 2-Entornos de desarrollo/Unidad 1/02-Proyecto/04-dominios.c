/*
    Calculadora STURMPROJEKT
    Version 0.4 - Webs, hosting y dominios
*/

#include <stdio.h>

int main(){
    // Declaro las variables
    int webs;
    int clientesHosting;
    int dominiosCobrados;

    float precioWeb = 250;
    float precioHosting = 35;
    float precioDominio = 35;

    float ingresosWebs;
    float ingresosHosting;
    float ingresosDominios;
    float ingresosMes;

    // Pido los datos
    printf("CALCULADORA STURMPROJEKT\n");

    printf("Cuantas webs has vendido este mes? ");
    scanf("%i", &webs);

    printf("Cuantos clientes de hosting tienes este mes? ");
    scanf("%i", &clientesHosting);

    printf("Cuantos servicios anuales de dominio has cobrado este mes? ");
    scanf("%i", &dominiosCobrados);

    // Calculo los ingresos
    ingresosWebs = webs * precioWeb;
    ingresosHosting = clientesHosting * precioHosting;
    ingresosDominios = dominiosCobrados * precioDominio;

    ingresosMes = ingresosWebs + ingresosHosting + ingresosDominios;

    // Muestro los resultados
    printf("\nINGRESOS DEL MES\n");
    printf("Desarrollo de webs: %.2f euros\n", ingresosWebs);
    printf("Hosting y mantenimiento: %.2f euros\n", ingresosHosting);
    printf("Servicios de dominio: %.2f euros\n", ingresosDominios);
    printf("Total: %.2f euros\n", ingresosMes);

    return 0;
}