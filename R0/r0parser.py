import ply.yacc as yacc
import array, sys

from r0lexer import tokens
def p_exp_negate(p):
    'EXP : NEGATE FACTOR'
    p[0] = 0 - int(p[2])


def p_scan(p):
    'EXP : SCAN'
    p[0] = int(raw_input('>'))

def p_add(p):
    'EXP : EXP PLUS EXP'
    p[0] = int(p[1]) + int(p[3])


def p_factor_exp(p):
    'FACTOR : LPAREN EXP RPAREN'
    p[0] = p[2]

def p_factor(p):
    'FACTOR : INTEGER'
    p[0] = p[1]

def p_factor_p(p):
    'EXP : FACTOR'
    p[0] = p[1]




# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")


# Build the parser
parser = yacc.yacc()

while True:
   try:
       s = raw_input('R0> ')
   except EOFError:
       break
   result = parser.parse(s)
   print(result)
