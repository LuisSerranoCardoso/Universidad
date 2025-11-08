//INCLUDES
#include <LPC17XX.H>
#include <math.h>
#include <stdio.h>
#include <string.h>

//DEFINICIÓN DE MACROS Y CONSTANTES
#define pi 3.14159265358979323846
#define g 9.81

//DEFINICIÓN DE VARIABLES GLOBALES => CON CUIDADO, Y UTILIZANDO LOS MENOS POSIBLES. IDELAMENTE, SÓLO PARA COMUNICACIÓN ENTRE HANDLERS
uint_8t indice = 0;
uint_8t contador = 0;

//DEFINICIÓN DE FUNCIONES
void activa_pin(void) {
    //Función que activa un pin concreto
}

void desactiva_pin(void) {
    //Función que desactiva un pin concreto
}

//DEFINICIÓNDE LAS FUNCIONES DE CONFIGURACIÓN
//TANTAS COMO INTERRUPCIONES UTILICEMOS
void config_EINT0(void) {
    LPC_PINCON->PINSEL4 |= (1 << 20); //P2.10 como EINT0
    LPC_SC->EXTMODE |= (1 << 0);      //EINT0 como borde
    LPC_SC->EXTPOLAR |= (1 << 0);     //EINT0 como flanco de subida
    NVIC_EnableIRQ(EINT0_IRQn);       //Habilitamos la interrupción en el NVIC
}
 
void SysTick_config(void) {
    SysTick->CTRL = 0;                             //Deshabilitamos el SysTick
    SysTick->LOAD = (SystemCoreClock / 1000) - 1; //Cargamos el valor para que salte cada 1ms
    SysTick->VAL = 0;                              //Limpiamos la cuenta actual
    SysTick->CTRL = 0x07;                          //Habilitamos el SysTick con interrupción y reloj de CPU
}

//PROGRAMAMOS ISR`S (HANDLERS) DE CADA INTERRUPCIÓN
void EINT0_IRQHandler(void) {
    activa_pin();
    contador++;
    if (contador >= 5) {
        desactiva_pin();
        contador = 0;
    }
    LPC_SC->EXTINT |= (1 << 0); //Limpiamos la interrupción
}

void SysTick_Handler(void) {
    indice++;
    if (indice >= 1000) {
        indice = 0;
    }
}

//PROGRAMA PRINCIPAL
int main() {
    //Llamamos a las funciones de configuración
    config_EINT0();
    SysTick_config();
    //Tarea cíclica del programa principal
    while (1) {
        // Aquí va el código de la tarea cíclica
    }
    return 0;
}