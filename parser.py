import ply.yacc as yacc
from lexer import tokens

# Armazena linhas geradas de código C
codigo = []

# Dicionário para rastrear observações declaradas
observacoes = set()

# ---------- Regras da gramática ----------

def p_program(p):
    'program : devices cmds'
    codigo.insert(0, '#include <stdio.h>\n\n')
    codigo.insert(1, '#define TRUE 1\n#define FALSE 0\n\n')
    codigo.insert(2, gerar_funcoes_fixas())
    codigo.insert(3, '\nint main() {\n')
    codigo.append('return 0;\n}\n')

def p_devices_mult(p):
    'devices : device devices'
    pass

def p_devices_one(p):
    'devices : device'
    pass

def p_device_com_observacao(p):
    'device : DISPOSITIVO DOISPONTOS ABRECHAVES ID VIRGULA ID FECHACHAVES'
    codigo.insert(3, f'int {p[4]} = 0;\nint {p[6]} = 0;\n')
    observacoes.add(p[6])

def p_device_sem_observacao(p):
    'device : DISPOSITIVO DOISPONTOS ABRECHAVES ID FECHACHAVES'
    codigo.insert(3, f'int {p[4]} = 0;\n')

def p_cmds(p):
    'cmds : cmd PONTO cmds'
    pass

def p_cmds_last(p):
    'cmds : cmd PONTO'
    pass

def p_cmd_set(p):
    'cmd : SET ID IGUAL var'
    codigo.append(f'{p[2]} = {p[4]};\n')

def p_cmd_if(p):
    'cmd : SE obs ENTAO act'
    codigo.append(f'if ({p[2]}) {{\n{p[4]}}}\n')

def p_cmd_if_else(p):
    'cmd : SE obs ENTAO act SENAO act'
    codigo.append(f'if ({p[2]}) {{\n{p[4]}}} else {{\n{p[6]}}}\n')

def p_cmd_acao(p):
    'cmd : act'
    codigo.append(p[1])

def p_obs_simples(p):
    'obs : ID op_logic var'
    p[0] = f'{p[1]} {p[2]} {p[3]}'

def p_obs_composta(p):
    'obs : ID op_logic var ELOGICO obs'
    p[0] = f'{p[1]} {p[2]} {p[3]} && {p[5]}'

def p_op_logic(p):
    '''op_logic : MAIOR
                | MENOR
                | MAIORIGUAL
                | MENORIGUAL
                | IGUALIGUAL
                | DIFERENTE'''
    p[0] = p[1]

def p_var(p):
    '''var : NUM
           | ID'''
    p[0] = p[1]

def p_act_ligar(p):
    'act : LIGAR ID'
    p[0] = f'ligar("{p[2]}");\n'

def p_act_desligar(p):
    'act : DESLIGAR ID'
    p[0] = f'desligar("{p[2]}");\n'

def p_act_alerta_simples(p):
    'act : ENVIAR ALERTA ABREPAREN STRING FECHAPAREN ID'
    p[0] = f'alerta("{p[6]}", "{p[4]}");\n'

def p_act_alerta_var(p):
    'act : ENVIAR ALERTA ABREPAREN STRING VIRGULA ID FECHAPAREN ID'
    p[0] = f'alerta_com_var("{p[8]}", "{p[4]}", {p[6]});\n'

def p_act_broadcast(p):
    'act : ENVIAR ALERTA ABREPAREN STRING FECHAPAREN PARA TODOS DOISPONTOS lista_ids'
    p[0] = p[9]  # já vem com várias chamadas alerta(...)

def p_lista_ids(p):
    'lista_ids : ID VIRGULA lista_ids'
    p[0] = f'alerta("{p[1]}", "mensagem");\n{p[3]}'

def p_lista_ids_single(p):
    'lista_ids : ID'
    p[0] = f'alerta("{p[1]}", "mensagem");\n'

def p_error(p):
    if p:
        print(f"Erro de sintaxe em '{p.value}'")
    else:
        print("Erro de sintaxe: fim de arquivo inesperado.")

# ---------- Função auxiliar ----------

def gerar_funcoes_fixas():
    return '''\
/* Funções fixas do programa */
void ligar(const char* d) { 
    printf("%s ligado!\\n", d); 
}
void desligar(const char* d) { 
    printf("%s desligado!\\n", d); 
}
void alerta(const char* d, const char* m) {
    printf("%s recebeu o alerta:\\n", d);
    printf("%s\\n", m);
}
void alerta_com_var(const char* d, const char* m, int v) {
    printf("%s recebeu o alerta:\\n", d);
    printf("%s %d\\n", m, v);
}
/* Fim das funções fixas */
'''

# ---------- Execução ----------

parser = yacc.yacc()

def parse_input(data, arquivo_saida="output.c"):
    global codigo
    codigo = []
    parser.parse(data)

    with open(arquivo_saida, "w") as f:
        for linha in codigo:
            f.write(linha)
