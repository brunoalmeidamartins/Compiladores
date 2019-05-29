import ply.yacc as yacc
import re
import codecs
import os
import sys
from analisador_lexico import tokens
from sys import stdin

precedence = (
    ('left', 'MAIS', 'MENOS'),
    ('left', 'MULTIPLICA', 'DIVIDE')
)

#lexer.input(cadeia)

def p_Program(p):
    '''
    Program : MainClass ClassDeclaration
    '''
    print('Program')
def p_MainClass(p):
    '''
    MainClass : CLASS Identifier CE PUBLIC STATIC VOID MAIN PE STRING COLCE COLCD Identifier PD CE Statement CD CD
    '''
    print('Main Class')
def p_ClassDeclaration(p):
    '''
    ClassDeclaration : empty
                     | CLASS Identifier EXTENDS Identifier CE VarDeclaration MethodDeclaration CD
                     | CLASS Identifier CE VarDeclaration MethodDeclaration CD
    '''
    print('Class Declaration')
def p_VarDeclaration(p):
    '''
    VarDeclaration : empty
                   | Type Identifier PONTOVIRGULA
                   | Type Identifier PONTOVIRGULA VarDeclaration
    '''
    print('Var Declaration')
def p_MethodDeclaration(p):
    '''
    MethodDeclaration : empty
                      | PUBLIC Type Identifier PE MethodDeclaration_2 PD CE VarDeclaration Statement RETURN Expression PONTOVIRGULA CD MethodDeclaration
    '''
    print('Method Declaration')
def p_MethodDeclaration_2(p):
    '''
    MethodDeclaration_2 : empty
                        | Type Identifier
                        | Type Identifier VIRGULA MethodDeclaration_2
    '''
    print('Method Declaration 2')
def p_Type(p):
    '''
    Type : INT COLCE COLCD
         | BOOLEAN
         | INT
         | Identifier
    '''
    print('Type')
def p_Statement(p):
    '''
    Statement : empty
              | CE Statement CD
              | IF PE Expression PD Statement ELSE Statement
              | WHILE PE Expression PD Statement
              | SYSTEM PONTO OUT PONTO PRINTLN PE Expression PD PONTOVIRGULA
              | Identifier IGUAL Expression PONTOVIRGULA
              | Identifier COLCE Expression COLCD IGUAL Expression PONTOVIRGULA
    '''
    print('Statement')
def p_Expression(p):
    '''
    Expression : Expression ECOMERCIAL Expression
               | Expression MENOR Expression
               | Expression MENORIGUAL Expression
               | Expression MAIOR Expression
               | Expression MAIORIGUAL Expression
               | Expression DIFERENTE Expression
               | Expression COMPARACAO Expression
               | Expression MAIS Expression
               | Expression MENOS Expression
               | Expression MULTIPLICA Expression
               | Expression DIVIDE Expression
               | Expression COLCE Expression COLCD
               | Expression PONTO LENGTH
               | Expression PONTO Identifier PE  Expression_2 PD
               | NUMERO
               | TRUE
               | FALSE
               | Identifier
               | THIS
               | NEW INT COLCE Expression COLCD
               | NEW Identifier PE PD
               | NEGACAO Expression
               | PE Expression PD
    '''
    print('Expression')
def p_Expression_2(p):
    '''
    Expression_2 : empty
                 | Expression
                 | Expression VIRGULA Expression_2
    '''
    print('Expression 2')
def p_Identifier(p):
    '''
    Identifier : ID
    '''
    print('Identifier')
def p_empty(p):
    ''' empty : '''
    p[0] = None
    print('Vazio')

def p_error(p):
    print("Syntax error found!!")
    print(p.type, p.value, p.lineno, p.lexpos)


'''
DEBUG
'''
fp = codecs.open('teste.txt', 'r', 'utf-8')
cadeia = fp.read()
fp.close()

parser = yacc.yacc('LR(1)')
result = parser.parse(cadeia)

print(result)