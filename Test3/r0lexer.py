import ply.lex as lex
import array

#list of tokens

tokens = (
    'LPAREN',
    'RPAREN',
    'INTEGER',
    'NEGATE',
    'PLUS',
    'EQUALS'
)
reserved = {
   'if' : 'IF',
   'then' : 'THEN',
   'else' : 'ELSE',
   'while' : 'WHILE',
   'let' : 'LET',
   'scanf' : 'SCAN',
   'var' : 'VAR',
   'print' : 'PRINT'
}
tokens += tuple(reserved.values());
#RegExps for tokens

t_LPAREN = r'\('
t_RPAREN = r'\)'
t_INTEGER = r'[0-9]+'
t_NEGATE = r'-'
t_PLUS = r'\+'
t_EQUALS = r'\='

def t_LET(t):
    r'let'
    t.value = reserved.get(t.value,'LET')
    return t

def t_PRINT(t):
    r'print'
    t.value = reserved.get(t.value,'PRINT')
    return t

def t_VAR(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.value = reserved.get(t.value,'VAR')
    return t



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
print tokens
