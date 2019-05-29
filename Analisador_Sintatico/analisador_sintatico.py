import ply.yacc as yacc
import re
import codecs
import os
import sys
from analisador_lexico import tokens
from sys import stdin

precedence = (
    ('right', 'ID'),
    ('right', 'COLCE')
)

#lexer.input(cadeia)

def p_prog(p):
    '''
    prog : main class
    '''
    #print('prog')

def p_main(p):
    '''
    main : CLASS ID CE PUBLIC STATIC VOID MAIN PE STRING COLCE COLCD ID PD CE cmd CD CD
    '''
    #print('main')
def p_class(p):
    '''
    class : CLASS ID EXTENDS ID CE var method CD class
          | CLASS ID CE var method CD class
          | empty
    '''
    #print('class')
def p_var(p):
    '''
    var : type ID PONTOVIRGULA var
        | empty
    '''
    #Se puder aceitar int a = 3, eh so adicionar {type cmd}
    #print('var')
    p[0] = ('var', p[1])
def p_method(p):
    '''
    method : PUBLIC type ID PE params PD CE var cmd RETURN exp PONTOVIRGULA CD method
           | empty
    '''
    #print('method')
def p_params(p):
    '''
    params : type ID
           | type ID VIRGULA params
           | empty
    '''
    #print('params')
def p_type(p):
    '''
    type : INT COLCE COLCD
         | BOOLEAN
         | INT
         | ID
    '''
    print(p[0])


#Para retirado do conflito, foi acrescentado as chaves nos comandos do IF e ELSE. Mudando a linguagem
def p_cmd(p):
    '''
    cmd : CE cmd CD
        | IF PE exp PD CE cmd CD
        | IF PE exp PD CE cmd CD ELSE CE cmd CD
        | WHILE PE exp PD cmd
        | SYSTEM PONTO OUT PONTO PRINTLN PE exp PD PONTOVIRGULA
        | ID IGUAL exp PONTOVIRGULA
        | ID COLCE exp COLCD IGUAL exp PONTOVIRGULA
        | empty
    '''
    #print('cmd')


#Conflito de exp && exp => exp && rexp
def p_exp(p):
    '''
    exp : exp ECOMERCIAL rexp
        | rexp
    '''
    if len(p) > 2:
        p[0] = ('expressao',p[2],p[1],p[3])
        print('expressao', p[2], p[1],p[3])

def p_rexp(p):
    '''
    rexp : rexp MENOR aexp
         | rexp COMPARACAO aexp
         | rexp DIFERENTE aexp
         | aexp
    '''
    if len(p) > 2:
        p[0] = ('expressao', p[2], p[1], p[3])
        print('expressao', p[2], p[1], p[3])
def p_aexp(p):
    '''
    aexp : aexp MAIS mexp
         | aexp MENOS mexp
         | mexp
    '''
    if len(p) > 2:
        p[0] = ('expressao', p[2], p[1], p[3])
        print('expressao', p[2], p[1], p[3])

def p_mexp(p):
    '''
    mexp : mexp MULTIPLICA sexp
         | mexp DIVIDE sexp
         | sexp
    '''
    if len(p) > 2:
        p[0] = ('expressao', p[2], p[1], p[3])
        print('expressao', p[2], p[1], p[3])
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
    print(p[1])

def p_pexp(p):
    '''
    pexp : ID
         | THIS
         | NEW ID PE PD
         | PE exp PD
         | pexp PONTO ID
         | pexp PONTO ID PE exps PD
    '''
    #print('pexp')

def p_exps(p):
    '''
    exps : exp COLCE VIRGULA  exp COLCD
         | exp
         | empty
    '''
    #print('exps')

def p_error(p):
    print("Syntax error found!!", p)
    #print(p.type, p.value, p.lineno, p.lexpos)

def p_empty(p):
    ''' empty : '''
    p[0] = None
    #print('Vazio')

'''
DEBUG
'''
fp = codecs.open('teste.txt', 'r', 'utf-8')
cadeia = fp.read()
fp.close()

parser = yacc.yacc(debug=True)
result = parser.parse(cadeia)

print(result)