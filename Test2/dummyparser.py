import ply.yacc as yacc
import array, sys

from dummylexer import tokens
#from datas import ic, ddata
global ic
global ddata
global pstr

ic = 0
ddata = [0 for x in range(30000)]

def p_GETIC(p):
    'exp : GETIC'
    global ic
    print ic

# def p_loop(p):
#     'exp : JUMPBACK exp JUMPFWD'
#     print s[::-1]
#     ss = s[::-1][1:len(s)-1]
#     print ss
#     # for i in range(ddata[ic]):
#     #     for j in ss:
#     #         print ss
#     #         parser.parse(ss)
#
# def p_comp(p):
#     '''exp  : NEXTBIT exp
#             | PREVBIT exp
#             | PLUS exp
#             | MINUS exp
#             | DOT exp
#             | COMMA exp
#             | NEXTBIT
#             | PREVBIT
#             | PLUS
#             | MINUS
#             | DOT
#             | COMMA'''
#     global ic, ddata
#     #if [str(p[0]), str(p[2])] in ['[',']']:
#     #    print str(p[1])
#     #else:
#     s = str(p[1])
#     #print s
#     if s in '>':
#         #print ">"
#         if ic < 30000: ic+=1
#     elif s in '<':
#         #print "<"
#         if ic > 0: ic-=1
#     elif s in '+':
#         #print "+"
#         ddata[ic]+=1
#     elif s in '-':
#         #print "-"
#         ddata[ic]-=1
#     elif s in '.':
#         #print "."
#         print ddata[ic]
#     elif s in ',':
#         #print ","
#         ddata[ic] = (ord(raw_input()[0]) - 48)
#     else:
#         p_error(p)




def p_exit(p):
    'exp : EXIT'
    print "exit"
    sys.exit(0)



# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")


# Build the parser
parser = yacc.yacc()

while True:
   try:
       s = raw_input('BrainFu*k#:')
       if s not in 'exit':
           s = s[::-1]
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)
   #print(result)
