import ply.lex as lex

tokens = [
    'ID', 'STRING', 'NUM',
    'MAIOR', 'MENOR', 'MAIORIGUAL', 'MENORIGUAL',
    'IGUALIGUAL', 'DIFERENTE', 'IGUAL', 'ELOGICO',
    'DOISPONTOS', 'VIRGULA', 'PONTO',
    'ABRECHAVES', 'FECHACHAVES', 'ABREPAREN', 'FECHAPAREN'
]

reserved = {
    'dispositivo': 'DISPOSITIVO',
    'set': 'SET',
    'se': 'SE',
    'entao': 'ENTAO',
    'senao': 'SENAO',
    'ligar': 'LIGAR',
    'desligar': 'DESLIGAR',
    'enviar': 'ENVIAR',
    'alerta': 'ALERTA',
    'para': 'PARA',
    'todos': 'TODOS'
}

tokens += list(reserved.values())

t_MAIOR       = r'>'
t_MENOR       = r'<'
t_MAIORIGUAL  = r'>='
t_MENORIGUAL  = r'<='
t_IGUALIGUAL  = r'=='
t_DIFERENTE   = r'!='
t_IGUAL       = r'='
t_ELOGICO     = r'&&'
t_DOISPONTOS  = r':'
t_VIRGULA     = r','
t_PONTO       = r'\.'
t_ABRECHAVES  = r'\{'
t_FECHACHAVES = r'\}'
t_ABREPAREN   = r'\('
t_FECHAPAREN  = r'\)'

def t_NUM(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'\"[^\"]+\"'
    t.value = t.value.strip('"')
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')
    return t

t_ignore = ' \t\n'

def t_error(t):
    print(f"Caractere ilegal: {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()
