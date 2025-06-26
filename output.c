#include <stdio.h>

void ligar(const char* d) { printf("%s ligado!\n", d); }
void desligar(const char* d) { printf("%s desligado!\n", d); }
void alerta(const char* d, const char* m) {
    printf("%s recebeu o alerta:\n", d);
    printf("%s\n", m);
}
void alerta_com_var(const char* d, const char* m, int v) {
    printf("%s recebeu o alerta:\n", d);
    printf("%s %d\n", m, v);
}
int main() {
int alarme = 0;
int movimento = 0;
int sensor = 0;
int luz = 0;
movimento = 1;
luz = 20;
if (movimento == 1 && luz < 30) {
ligar("alarme");
}
return 0;
}
