
# ----------------------------------------------------------------
#                            Reservadas
# ----------------------------------------------------------------
tokens = [
    'PARENTESISDERECHO',
    'PARENTESISIZQUIERDO',
    'CORCHETEDERECHO',
    'CORCHETEIZQUIERDO',
    'LLAVEDERECHO',
    'LLAVEIZQUIERDO',
    'PUNTOCOMA',
    'DOSPUNTOS',
    'COMA',
    'MENOR',
    'MAYOR',
    'PUNTO',
    'IGUAL',
    'IGUALDAD',
    'PORCENTAJE',
    'BARRA',
    'AMPERSAND',
    'MAYORIGUAL',
    'MENORIGUAL',
    'DIFERENTE',
    'OR',
    'AND',
    'NOT',
    'WHAT',
    'TIPORETURN',
    'MAS',
    'MENOS',
    'MULTIPLICAR',
    'DIV',
    'ENTERO',
    'DECIMAL',
    'CADENA',
    'CARACTER',
    'ID',
    'COMENTARIO'
    # 'CONCATENARSTR'
]  

reservadas = {
    'String'        : 'STRING',
    'Vec'           : 'VEC',
    'println'       : 'PRINTLN',
    'i64'           : 'I64',
    'f64'           : 'F64',
    'bool'          : 'BOOL',
    'char'          : 'CHAR',
    'main'          : 'MAIN',
    'usize'         : 'USIZE',
    'let'           : 'LET',
    'mut'           : 'MUT',
    'struct'        : 'STRUCT',
    'as'            : 'AS',
    'true'          : 'TRUE',
    'false'         : 'FALSE',
    'fn'            : 'FN',
    'return'        : 'RETURN',
    'abs'           : 'ABS',
    'sqrt'          : 'SQRT',
    'to_string'     : 'TO_STRING',
    'clone'         : 'CLONE',
    'new'           : 'NEW',
    'len'           : 'LEN',
    'push'          : 'PUSH',
    'remove'        : 'REMOVE',
    'contains'      : 'CONTAINS',
    'insert'        : 'INSERT',
    'capacity'      : 'CAPACITY',
    'with_capacity' : 'WITH_CAPACITY',
    'if'            : 'IF',
    'else'          : 'ELSE',
    'while'         : 'WHILE',
    'loop'          : 'LOOP',
    'break'         : 'BREAK',
    'continue'      : 'CONTINUE',
    'pow'           : 'POW',
    'for'           : 'FOR',
    'in'            : 'IN'
}

tokens = tokens + list(reservadas.values())


# ----------------------------------------------------------------
#                              Tokens
# ----------------------------------------------------------------
# t_CONCATENARSTR         = r'&str'
t_PARENTESISDERECHO     = r'\)'
t_PARENTESISIZQUIERDO   = r'\('
t_CORCHETEDERECHO       = r'\['
t_CORCHETEIZQUIERDO     = r'\]'
t_LLAVEIZQUIERDO        = r'\{'
t_LLAVEDERECHO          = r'\}'
t_PUNTOCOMA             = r'\;'
t_DOSPUNTOS             = r'\:'
t_COMA                  = r'\,'
t_PUNTO                 = r'\.'
t_IGUALDAD              = r'=='
t_IGUAL                 = r'='
t_PORCENTAJE            = r'\%'
t_BARRA                 = r'\|'
t_NOT                   = r'\!'
t_MAYORIGUAL            = r'\>='
t_MENORIGUAL            = r'\<='
t_MENOR                 = r'<'
t_MAYOR                 = r'>'
t_DIFERENTE             = r'\!='
t_OR                    = r'\|\|'
t_AMPERSAND             = r'\&'
t_AND                   = r'\&&'
t_WHAT                  = r'\?'
t_TIPORETURN            = r'\->'
t_MAS                   = r'\+'
t_MENOS                 = r'\-'
t_MULTIPLICAR           = r'\*'
t_DIV                   = r'/'


# ----------------------------------------------------------------
#                      Expresiones Regulares
# ----------------------------------------------------------------


# MANEJO DE NUMEROS DECIMAL
def t_DECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print(f'Error al convertir a un valor tipo float {t.value}')
        t.value = 0
    return t



# MANEJO DE NUMERO ENTEROS
def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print(f'Error al convertir a un valor entero {t.value}')
        t.value = 0
    return t





# MANEJO DE IDENTIFICADORES
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reservadas.get(t.value,'ID')    # Check for reserved words
    # print(f'Palabra reservada {t.value}')    
    return t



# menjo de caracteres
def t_CARACTER(t):  
    r'\'.*?\''
    # sin comillas simples
    t.value = t.value[1:-1]
    t.value = t.value
    return t





#  MANEJO DE CADENAS PARA EL LENGUAJe
def t_CADENA(t):
    r'\".*?\"'
    # sin comillas
    t.value = t.value[1:-1]
    return t






# menjo de comptario uniliena 
def t_COMENTARIO(t):
    r'//.*\n'
    t.lexer.lineno += 1


# caracteres ignorados
t_ignore = " \t"


# manjo de salotos de linea
def t_newline(t):
    r'\n'
    t.lexer.lineno += t.value.count('\n')



# manejo de filas
def columnToken(inp, tk):
    line = inp.rfind('\n', 0, tk.lexpos) + 1
    return (tk.lexpos - line) + 1



# MANEJO DE ERRORES
def t_error(t):
    print(f'Error lexico {t.value[0]}')
    t.lexer.skip(1)


# build lexer
import Compiler.ply.lex as lex
lexer = lex.lex()


# if __name__ == '__main__':
#     import ply.lex as lex
#     import re
    
#     analizador = lex.lex()

#     f = open('./entrada.txt')
#     contenido = f.read()

#     analizador.input(contenido)

#     while True:
#         tok = analizador.token()
#         if not tok:
#             # no hay mas entradas
#             break
#         print(tok)