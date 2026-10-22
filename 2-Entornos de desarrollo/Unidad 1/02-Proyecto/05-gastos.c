/*
    Calculadora STURMPROJEKT
    Version 0.5 - Ingresos y gastos del mes
	
	
	Tengo que decir que tuve dificultades con programación en C, la ia me ayudo bastante además de depurando el codigo, 
	me oriento, y me ayudo a entender los conceptops y a hacer las variables correctamente 
	y comentar de forma precisa los bloques de codigo
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

    float electricidad = 10;
    float internet = 15;
    float gptPlus = 23;
    float costeDominio = 15;

    float ingresosWebs;
    float ingresosHosting;
    float ingresosDominios;
    float ingresosMes;
    float gastosDominios;
    float gastosMes;
    float resultadoMes;

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

    // Calculo los gastos y el resultado
    gastosDominios = dominiosCobrados * costeDominio;
    gastosMes = electricidad + internet + gptPlus + gastosDominios;
    resultadoMes = ingresosMes - gastosMes;

    // Muestro los resultados
    printf("\nRESUMEN DEL MES\n");
    printf("Ingresos por webs: %.2f euros\n", ingresosWebs);
    printf("Ingresos por hosting: %.2f euros\n", ingresosHosting);
    printf("Ingresos por dominios: %.2f euros\n", ingresosDominios);
    printf("Ingresos totales: %.2f euros\n", ingresosMes);

    printf("\nElectricidad: %.2f euros\n", electricidad);
    printf("Internet: %.2f euros\n", internet);
    printf("GPT Plus: %.2f euros\n", gptPlus);
    printf("Gastos de dominios: %.2f euros\n", gastosDominios);
    printf("Gastos totales: %.2f euros\n", gastosMes);

    printf("\nResultado del mes: %.2f euros\n", resultadoMes);

    // Indico si hay ganancias o perdidas
    if(resultadoMes > 0){
        printf("Hay ganancias.\n");
    }else if(resultadoMes < 0){
        printf("Hay perdidas.\n");
    }else{
        printf("Los ingresos y los gastos son iguales.\n");
    }

    return 0;
}