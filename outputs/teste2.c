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
int monitor = 0;
int celular = 0;
int Termometro = 0;
int temperatura = 0;
temperatura = 37;
alerta_com_var("Termometro", "Temperatura em", temperatura);
alerta("monitor", "mensagem");
alerta("celular", "mensagem");
return 0;
}
