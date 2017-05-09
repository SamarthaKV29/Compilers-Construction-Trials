import ply.lex as lex
import array

#list of tokens

tokens = (
    'NEXTBIT',
    'PREVBIT',
    'PLUS',
    'MINUS',
    'DOT',
    'COMMA',
    #'SEMI',
    'EXIT',
    'GETIC',
    'COPY',
    'JUMPFWD',
    'JUMPBACK',
)

#RegExps for tokens
t_NEXTBIT = r'>'
t_PREVBIT = r'<'
t_PLUS = r'\+'
t_MINUS = r'-'
t_DOT = r'\.'
t_COMMA = r','
#t_SEMI = r';'
t_EXIT = r'exit'
t_GETIC = r'p'
t_COPY = r'c'
t_JUMPFWD = r'\['
t_JUMPBACK = r'\]'


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
