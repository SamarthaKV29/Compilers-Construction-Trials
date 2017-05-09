import ply.yacc as yacc
import array, sys

from c0lexer import tokens

variables = {}
var_types = {}

class Expr: pass




def p_program(p):
    'EXP : LPAREN PROGRAM EXP MORE RPAREN'
    if (len(p) == 5):
        p[0] = p[3]
    elif (len(p) > 5):
        pass


def p_brackets(p):
    'EXP : LPAREN EXP RPAREN'
    p[0] = p[2]

def p_more(p):
    '''MORE : EXP MORE
            | '''
    if len(p) is 0:
        return


def p_neg(p):
    'EXP : NEGATE EXP'
    if p[2] in variables.keys():
        if var_types[p[2]] in 'INTEGER':
            variables[p[2]] = 0 - int(variables[p[2]])
            p[0] = variables[p[2]]
        elif var_types[p[2]] in 'BOOL':
            print "error: Invalid operation on Non BOOL"
    else:
        try:
            p[0] = 0 - int(p[2])
        except:
            print "invalid add op"

def p_add(p):
    'EXP : PLUS EXP EXP'
    if (p[2],p[3]) in variables.keys():
        if (var_types[p[2]], var_types[p[3]]) in 'INTEGER':
            p[0] = int(variables[p[2]]) + int(variables[p[3]])
        elif (var_types[p[2]], var_types[p[3]]) in 'BOOL':
            print "error: Invalid operation on Non BOOL"
    else:
        try:
            p[0] = int(p[2]) + int(p[3])
        except:
            print "invalid add op"



def p_int_exp(p):
    'EXP : INTEGER'
    p[0] = int(p[1])

def p_bool_exp(p):
    'EXP : BOOL'
    p[0] = p[1]

def p_scan(p):
    'EXP : SCAN'
    p[0] = raw_input('>')




def p_var(p):
    'EXP : VAR EXP'
    print "creating"
    variables[p[1]] = p[2]


def p_print(p):
    'EXP : PRINT VAR'
    if p[2] in variables.keys():
        print variables[p[2]]
    else:
        print "invalid"

def p_prr(p):
    'EXP : PRINT INTEGER'
    print p[2]

# Error rule for syntax errors
def p_error(p):
    if p:
         print("Syntax error at token", p.type)
         # Just discard the token and tell the parser it's okay.
         parser.errok()
    else:
         print("Syntax error at EOF")


# Build the parser
parser = yacc.yacc()

while True:
   try:
       s = raw_input('R1> ')
   except EOFError:
       break
   result = parser.parse(s)
   #print(result)
