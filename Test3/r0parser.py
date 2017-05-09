import ply.yacc as yacc
import array, sys

from r0lexer import tokens

variables = {}


def p_ints(p):
    'EXP : INTEGER'
    p[0] = int(p[1])

def p_scan(p):
    'EXP : SCAN'
    p[0] = raw_input('>')

def p_neg(p):
    'EXP : NEGATE EXP'
    if p[2] in variables.keys():
        variables[p[2]] = 0 - variables[p[2]]
    else:
        try:
            p[0] = 0 - int(p[2])
        except:
            print "invalid"

def p_add(p):
    'EXP : PLUS EXP EXP'
    if (p[2],p[3]) in variables.keys():
        p[0] = variables[p[2]] + variables[p[3]]
    else:
        try:
            p[0] = int(p[2]) + int(p[3])
        except:
            print "invalid"

def p_var(p):
    'EXP : VAR'
    if p[1] in variables.keys():
        p[0] = variables[p[1]]
    else:
        print "undefined" + str(p[1])

def p_parens(p):
    'EXP : LPAREN EXP RPAREN'
    p[0] = p[2]

def p_let(p):
    'EXP : LPAREN LET LPAREN VAR EXP RPAREN EXP RPAREN'
    variables[p[4]] = p[5]
    p[0] = p[7]


def p_print(p):
    'EXP : PRINT EXP'
    print p[2]





# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")


# Build the parser
parser = yacc.yacc()

while True:
   try:
       s = raw_input('R1> ')
   except EOFError:
       break
   result = parser.parse(s)
   #print(result)
