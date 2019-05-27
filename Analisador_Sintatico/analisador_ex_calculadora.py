import ply.lex as lex
import ply.yacc as yacc
import sys

tokens = ['INT','FLOAT' , 'NAME' , 'PLUS' , 'MINUS' , 'DIVIDE' , 'MULTIPLY' ,
'EQUALS']

#list of tokens , for grammar checking

t_PLUS = r'\+'
t_MINUS = r'\-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'\/'
t_EQUALS = r'\='

t_ignore = r' ' # used for ignoring spaces between numbers and operators

#has to match name of token,

def t_FLOAT(t):
    r'\d+\.\d+' # 1.2 is a float , 1.any number is a float
    t.value = float(t.value)
    return t

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t # t is our token object

def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*' #star means 0 or more, first char is a-zA-z , second character is a-zA-z0-9
    t.type = 'NAME'
    return t

def t_error(t):
    print("Illegal characters!")
    t.lexer.skip(1) # skips 1 token onwards

lexer = lex.lex()

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULTIPLY', 'DIVIDE')
)

def p_calc(p):
    '''
    calc : expression
         | var_assign
         | empty
    '''
    print(run(p[1]))

def p_var_assign(p):
    '''
    var_assign : NAME EQUALS NAME
    '''
    p[0] = (p[2], p[1], p[3])
def p_expression(p):
    '''
    expression : expression MULTIPLY expression
               | expression DIVIDE expression
               | expression PLUS expression
               | expression MINUS expression
    '''

    p[0] = (p[2], p[1], p[3])

def p_expression_int_float(p):
    '''
    expression : INT
               | FLOAT
    '''
    p[0] = p[1]

def p_expression_var(p):
    '''
    expression : NAME
    '''
    p[0] = ('var', p[1])

def p_empty(p):
    ''' empty : '''
    p[0] = None

def p_error(p):
    print("Syntax error found!!")

def run(p):
    if type(p) == tuple:
        if p[0] == '+':
            return run(p[1]) + run(p[2])
        elif p[0] == '-':
            return run(p[1]) - run(p[2])
        elif p[0] == '*':
            return run(p[1]) * run(p[2])
        elif p[0] == '/':
            return run(p[1]) / run(p[2])
    else:
        return p

parser = yacc.yacc()

print('Digite as expressoes: ')
while True:
   try:
       s = input('>>')
   except EOFError:
       break
   parser.parse(s)
