#import ply.yacc as yacc
import plyplus.grammar_parser as plyplus
import re
from analisador_lexico import tokens

codigo_valido = True

precedence=(
    ('left', 'ID', 'INT', 'BOOLEAN'),
)


#Funcao da Gramatica
def p_prog(p):
    '''
    prog : main prog2
    '''

#Funcao extendida de prog
def p_prog2(p):
    '''
    prog2 : class prog2
          | empty
    '''

#Funcao da Gramatica
def p_main(p):
    '''
    main : CLASS id CE PUBLIC STATIC VOID MAIN PE STRING COLCE COLCD id PD CE cmd CD CD
    '''

#Funcao da Gramatica
def p_class(p):
    '''
    class : CLASS id class2 CE class3 class4 CD
    '''

#Funcao extendida de class
def p_class2(p):
    '''
    class2 : EXTENDS id
           | empty
    '''

#Funcao extendida de class
def p_class3(p):
    '''
    class3 : var class3
            | empty
    '''
#Funcao extendida de class
def p_class4(p):
    '''
    class4 : method class4
            | empty
    '''

#Funcao da Gramatica
def p_var(p):
    '''
    var : type id PONTOVIRGULA
    '''

#Funcao da Gramatica
def p_method(p):
    '''
    method : PUBLIC type id PE method2 PD CE method3 method4 RETURN exp PONTOVIRGULA CD
    '''

#Funcao extendida de method
def p_method2(p):
    '''
    method2 : params
            | empty
    '''

#Funcao extendida de method
def p_method3(p):
    '''
    method3 : var method3
            | empty
    '''

#Funcao extendida de method
def p_method4(p):
    '''
    method4 : cmd method4
            | empty
    '''

#Funcao da Gramatica
def p_params(p):
    '''
    params : type id params2
    '''

#Funcao extendida de params
def p_params2(p):
    '''
    params2 : VIRGULA type id params2
            | empty
    '''

#Funcao da Gramatica
#Retirei o ID
def p_type(p):
    '''
    type : INT COLCE COLCD
         | BOOLEAN
         | INT
         | id
    '''

#Funcao da Gramatica
def p_cmd(p):
    '''
    cmd : CE cmd2 CD
        | IF PE exp PD cmd
        | IF PE exp PD cmd ELSE cmd
        | WHILE PE exp PD cmd
        | SYSTEMOUTPRINTLN PE exp PD PONTOVIRGULA
        | id IGUAL exp PONTOVIRGULA
        | id COLCE exp COLCD IGUAL exp PONTOVIRGULA
    '''

#Funcao extendida de cmd
def p_cmd2(p):
    '''
    cmd2 : cmd cmd2
         | empty
    '''

#Funcao da Gramatica
#Conflito de exp && exp => exp && rexp
def p_exp(p):
    '''
    exp : exp ECOMERCIAL rexp
        | rexp
    '''

#Funcao da Gramatica
def p_rexp(p):
    '''
    rexp : rexp MENOR aexp
         | rexp COMPARACAO aexp
         | rexp DIFERENTE aexp
         | aexp
    '''

#Funcao da Gramatica
def p_aexp(p):
    '''
    aexp : aexp MAIS mexp
         | aexp MENOS mexp
         | mexp
    '''

#Funcao da Gramatica
def p_mexp(p):
    '''
    mexp : mexp MULTIPLICA sexp
         | mexp DIVIDE sexp
         | sexp
    '''

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

#Funcao da Gramatica
def p_pexp(p):
    '''
    pexp : id
         | THIS
         | NEW id PE PD
         | PE exp PD
         | pexp PONTO id
         | pexp PONTO id PE pexp2 PD
    '''
#Funcao extendida de pexp
def p_pexp2(p):
    '''
    pexp2 : exps
          | empty
    '''

#Funcao da Gramatica
def p_exps(p):
    '''
    exps : exp exps2
    '''
#Funcao extendida de exps
def p_exps2(p):
    '''
    exps2 : VIRGULA exp exps2
          | empty
    '''

#Funcao da Gramatica
def p_id(p):
    '''
    id : ID
    '''

#Funcao para gerar o log de erro!
def p_error(p):
    global codigo_valido
    codigo_valido = False
    print("Erro Sintatico encontrado: ", p)


#Funcao para gerar vazio
def p_empty(p):
    ''' empty : '''

'''
DEBUG
'''
#path_programa = input("Digite o caminho do arquivo:")
path_programa = 'Programas_MiniJava/programa5.java'
fp = open(path_programa, 'r')
cadeia = fp.read()
fp.close()

#parser = yacc.yacc('LALR(1)')
parser = plyplus.yacc.yacc('')
#result = parser.parse(cadeia)
result = parser
if codigo_valido:
    print('Codigo valido para a linguagem Mini Java!')
else:
    print('Codigo com erro sintatico!')