import ply.yacc as yacc
import re
from analisador_lexico import tokens
from analisador_semantico import *

codigo_valido = True

#Funcao da Gramatica
def p_prog(p):
    '''
    prog : main prog2
    '''
    p[0] = prog(p[1],p[2], "prog")

#Funcao extendida de prog
def p_prog2(p):
    '''
    prog2 : class1 prog2
          | empty
    '''
    if len(p) == 3:
        p[0] = prog2(p[1], p[2], "prog2")
    else:
        p[0] = prog2(p[1], "prog2")


#Funcao da Gramatica
def p_main(p):
    '''
    main : CLASS ID CE PUBLIC STATIC VOID MAIN PE STRING COLCE COLCD ID PD CE cmd CD CD
    '''
    p[0] = main(p[15], "main")

#Funcao da Gramatica
def p_class1(p):
    '''
    class1 : CLASS ID class2 CE class3 class4 CD
    '''
    p[0] = class1(p[3], p[5], p[6], "class1")

#Funcao extendida de class
def p_class2(p):
    '''
    class2 : EXTENDS ID
           | empty
    '''
    if len(p) == 2:
        p[0] = class2(p[1],"class2")

#Funcao extendida de class
def p_class3(p):
    '''
    class3 : var class3
            | empty
    '''
    if len(p) == 2:
        p[0] = class3(p[1], "class3")
    else:
        p[0] = class3(p[1], p[2], "class3")
#Funcao extendida de class
def p_class4(p):
    '''
    class4 : method class4
            | empty
    '''
    if len(p) == 2:
        p[0] = class3(p[1], "class4")
    else:
        p[0] = class3(p[1], p[2], "class4")

#Funcao da Gramatica
def p_var(p):
    '''
    var : type ID PONTOVIRGULA
    '''
    p[0] = var(p[0], "var")

#Funcao da Gramatica
def p_method(p):
    '''
    method : PUBLIC type ID PE method2 PD CE method3 method4 RETURN exp PONTOVIRGULA CD
    '''
    p[0] = method(p[2], p[5], p[8], p[9], p[11], "method")

#Funcao extendida de method
def p_method2(p):
    '''
    method2 : params
            | empty
    '''
    p[0] = method2(p[1], "method2")

#Funcao extendida de method
def p_method3(p):
    '''
    method3 : var method3
            | empty
    '''
    if len(p) == 2:
        p[0] = method3(p[1], "method3")
    else:
        p[0] = method3(p[1], p[2], "method3")

#Funcao extendida de method
def p_method4(p):
    '''
    method4 : cmd method4
            | empty
    '''
    if len(p) == 2:
        p[0] = method3(p[1], "method4")
    else:
        p[0] = method3(p[1], p[2], "method4")

#Funcao da Gramatica
def p_params(p):
    '''
    params : type ID params2
    '''
    p[0] = params(p[1], p[3], "params")

#Funcao extendida de params
def p_params2(p):
    '''
    params2 : VIRGULA type ID params2
            | empty
    '''
    if len(p) == 2:
        p[0] = params2(p[1],"params2")
    else:
        p[0] = params2(p[2], p[4], "params2")

#Funcao da Gramatica
def p_type(p):
    '''
    type : INT COLCE COLCD
         | BOOLEAN
         | INT
         | ID
    '''
    if len(p) ==  2:
        p[0] = type(p[1], "type")
    else:
        p[0] = type(p[1],p[2],p[3], "type")

#Funcao da Gramatica
def p_cmd(p):
    '''
    cmd : CE cmd2 CD
        | IF PE exp PD cmd
        | IF PE exp PD cmd ELSE cmd
        | WHILE PE exp PD cmd
        | SYSTEMOUTPRINTLN PE exp PD PONTOVIRGULA
        | ID IGUAL exp PONTOVIRGULA
        | ID COLCE exp COLCD IGUAL exp PONTOVIRGULA
    '''
    if len(p) == 4:
        p[0] = cmd(p[2], "cmd")
    elif len(p) == 5:
        p[0] = cmd(p[3], "cmd")
    elif len(p) == 6:
        if p[1] == 'IF':
            p[0] = cmd(p[3], p[5], "cmd")
        elif p[1] == 'WHILE':
            p[0] = cmd(p[3], p[5], "cmd")
        elif p[1] == "SYSTEMOUTPRINTLN":
            p[0] = cmd(p[3], "cmd")
        else
            pass
    else:
        if p[1] == 'IF':
            p[0] = cmd(p[3], p[5], p[7], "cmd")
        else:
            p[0] = cmd(p[3], p[6], "cmd")



#Funcao extendida de cmd
def p_cmd2(p):
    '''
    cmd2 : cmd cmd2
         | empty
    '''
    if len(p) == 2:
        p[0] = cmd2(p[1],"cmd2")
    else:
        p[0] = cmd2(p[1], p[2], "cmd2")

#Funcao da Gramatica
#Conflito de exp && exp => exp && rexp
def p_exp(p):
    '''
    exp : exp ECOMERCIAL rexp
        | rexp
    '''
    if len(p) == 2:
        p[0] = exp(p[1],"exp")
    else:
        p[0] = exp(p[1], p[3], "exp")

#Funcao da Gramatica
def p_rexp(p):
    '''
    rexp : rexp MENOR aexp
         | rexp COMPARACAO aexp
         | rexp DIFERENTE aexp
         | aexp
    '''
    if len(p) == 2:
        p[0] = rexp(p[1],"rexp")
    else:
        p[0] = rexp(p[1], p[3], "rexp")

#Funcao da Gramatica
def p_aexp(p):
    '''
    aexp : aexp MAIS mexp
         | aexp MENOS mexp
         | mexp
    '''
    if len(p) == 2:
        p[0] = aexp(p[1],"aexp")
    else:
        p[0] = aexp(p[1], p[3], "aexp")

#Funcao da Gramatica
def p_mexp(p):
    '''
    mexp : mexp MULTIPLICA sexp
         | mexp DIVIDE sexp
         | sexp
    '''
    if len(p) == 2:
        p[0] = mexp(p[1],"mexp")
    else:
        p[0] = mexp(p[1], p[3], "mexp")

#Funcao da Gramatica
def p_sexp(p):
    '''
    sexp : NEGACAO sexp
         | MENOS sexp
         | TRUE
         | FALSE
         | NUMERO
         | NULL
         | NEW INT COLCE exp COLCD
         | pexp PONTO LENGTH
         | pexp COLCE exp COLCD
         | pexp
    '''
    if len(p) == 2:
        p[0] = sexp(p[1],"sexp")
    elif len(p) == 3:
        p[0] = sexp(p[2], "sexp")
    elif len(p) == 4:
        p[0] = sexp(p[1], "sexp")
    elif len(p) == 5:
        p[0] = sexp(p[1], p[3], "sexp")
    else:
        p[0] = sexp(p[4], "sexp")

#Funcao da Gramatica
def p_pexp(p):
    '''
    pexp : ID
         | THIS
         | NEW ID PE PD
         | PE exp PD
         | pexp PONTO ID
         | pexp PONTO ID PE pexp2 PD
    '''
    if len(p) == 4:
        if p[1] == PE:
            p[0] = pexp(p[2], "pexp")
        else:
            p[0] = pexp(p[1], "pexp")
    else:
        p[0] = pexp(p[1], p[5], "pexp")
#Funcao extendida de pexp
def p_pexp2(p):
    '''
    pexp2 : exps
          | empty
    '''
    p[0] = pexp2(p[1], "pexp2")

#Funcao da Gramatica
def p_exps(p):
    '''
    exps : exp exps2
    '''
    p[0] = exps(p[1], p[2], "exps")
#Funcao extendida de exps
def p_exps2(p):
    '''
    exps2 : VIRGULA exp exps2
          | empty
    '''
    if len(p) == 2:
        p[0] = exps2(p[1], "exps2")
    else:
        p[0] = exps2(p[2], p[3], "exps2")

#Funcao para gerar o log de erro!
def p_error(p):
    global codigo_valido
    codigo_valido = False
    print("Erro Sintatico encontrado: ", p)


#Funcao para gerar vazio
def p_empty(p):
    ''' empty : '''
    p[0] = Null()

'''
DEBUG
'''
path_programa = input("Digite o caminho do arquivo:")
fp = open(path_programa, 'r')
cadeia = fp.read()
fp.close()

parser = yacc.yacc(debug=False)
result = parser.parse(cadeia)
if codigo_valido:
    print('Codigo valido para a linguagem Mini Java!')
else:
    print('Codigo com erro sintatico!')