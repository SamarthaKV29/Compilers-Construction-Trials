import ply.lex as lex
import array

#list of tokens

tokens = (
    'INTEGER',
    'SCAN',
    'NEGATE',
    'PLUS',
    'LPAREN',
    'RPAREN'

)

#RegExps for tokens
t_INTEGER = r'[0-9]+'
t_SCAN = r'scanf'
t_NEGATE = r'-'
t_PLUS = r'\+'
t_LPAREN = r'\('
t_RPAREN = r'\)'



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
