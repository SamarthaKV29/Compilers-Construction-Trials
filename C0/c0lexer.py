import ply.lex as lex
import array

#list of tokens

tokens = (
    'LPAREN',
    'RPAREN',
    'INTEGER',
    'NEGATE',
    'PLUS',
    'EQUALS',
    'VAR',
    'BOOL'
)
reserved = {
   'if' : 'IF',
   'program' : 'PROGRAM',
   'else' : 'ELSE',
   'while' : 'WHILE',
   'let' : 'LET',
   'scanf' : 'SCAN',
   'print' : 'PRINT',
   'type' : 'TYPE'
}
tokens += tuple(reserved.values());
#RegExps for tokens

t_LPAREN = r'\('
t_RPAREN = r'\)'
t_INTEGER = r'[0-9]+'
t_NEGATE = r'-'
t_PLUS = r'\+'
t_EQUALS = r'\='
t_BOOL = r'\#t|\#f'
t_VAR = r'[a-zA-Z_][a-zA-Z_0-9]*'

def t_LET(t):
    r'let'
    t.value = reserved.get(t.value,'LET')
    return t

def t_PRINT(t):
    r'print'
    t.value = reserved.get(t.value,'PRINT')
    return t

def t_TYPE(t):
    r'int|bool'
    t.value = reserved.get(t.value,'TYPE')
    return t

def t_PROGRAM(t):
    r'program'
    t.value = reserved.get(t.value,'PROGRAM')
    return t

precedence = (
    ('left', 'PROGRAM'),
    ('left', 'LET', 'SCAN', 'PRINT', 'TYPE'),
    ('left', 'PLUS', 'NEGATE'),
)

#Rule for line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()
