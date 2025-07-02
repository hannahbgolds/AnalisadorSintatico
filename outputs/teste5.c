#include <stdio.h>

#define TRUE 1
#define FALSE 0

/* Funções fixas do programa */
void ligar(const char* d) { 
    printf("%s ligado!\n", d); 
}
void desligar(const char* d) { 
    printf("%s desligado!\n", d); 
}
void alerta(const char* d, const char* m) {
    printf("%s recebeu o alerta:\n", d);
    printf("%s\n", m);
}
void alerta_com_var(const char* d, const char* m, int v) {
    printf("%s recebeu o alerta:\n", d);
    printf("%s %d\n", m, v);
}
/* Fim das funções fixas */

int main() {
int lampada = 0;
int sensor1 = 0;
int sensor2 = 0;
sensor1 = 1;
sensor2 = 2;
if (sensor1 == 1 && sensor2 == 2) {
ligar("lampada");
}
return 0;
}
