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
    Program : MainClass Program2
    '''
    print('Program')
def p_Program2(p):
    '''
    Program2 : ClassDeclaration Program2
             | empty
    '''
def p_MainClass(p):
    '''
    MainClass : CLASS Identifier CE PUBLIC STATIC VOID MAIN PE STRING COLCE COLCD Identifier PD CE Statement CD CD
    '''
    print('Main Class')
def p_ClassDeclaration(p):
    '''
    ClassDeclaration : CLASS Identifier ClassDeclaration2 CE ClassDeclaration3 ClassDeclaration4 CD
    '''
    print('Class Declaration')

def p_ClassDeclaration2(p):
    '''
    ClassDeclaration2 : EXTENDS Identifier
                      | empty
    '''
def p_ClassDeclaration3(p):
    '''
    ClassDeclaration3 : VarDeclaration ClassDeclaration3
                      | empty
    '''
def p_ClassDeclaration4(p):
    '''
    ClassDeclaration4 : MethodDeclaration ClassDeclaration4
                      | empty
    '''
def p_VarDeclaration(p):
    '''
    VarDeclaration : Type Identifier PONTOVIRGULA
    '''
    print('Var Declaration')
def p_MethodDeclaration(p):
    '''
    MethodDeclaration : PUBLIC Type Identifier PE MethodDeclaration2 PD CE MethodDeclaration4 MethodDeclaration5 RETURN Expression PONTOVIRGULA CD
    '''
    print('Method Declaration')
def p_MethodDeclaration2(p):
    '''
    MethodDeclaration2 : MethodDeclaration3
                       | empty
    '''
def p_MethodDeclaration3(p):
    '''
    MethodDeclaration3 : Type Identifier MethodDeclaration6
                       | empty
    '''
def p_MethodDeclaration6(p):
    '''
    MethodDeclaration6 : VIRGULA Type Identifier MethodDeclaration6
                       | empty
    '''
def p_MethodDeclaration4(p):
    '''
    MethodDeclaration4 : VarDeclaration MethodDeclaration4
                       | empty
    '''

def p_MethodDeclaration5(p):
    '''
    MethodDeclaration5 : Statement MethodDeclaration5
                       | empty
    '''

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
    Statement : CE Statement2 CD
              | IF PE Expression PD Statement ELSE Statement
              | WHILE PE Expression PD Statement
              | SYSTEMOUTPRINTLN PE Expression PD PONTOVIRGULA
              | Identifier IGUAL Expression PONTOVIRGULA
              | Identifier COLCE Expression COLCD IGUAL Expression PONTOVIRGULA
    '''
    print('Statement')
def p_Statement2(p):
    '''
    Statement2 : Statement Statement2
               | empty
    '''
def p_Expression(p):
    '''
    Expression : Expression ECOMERCIAL Expression
               | Expression MENOR Expression
               | Expression MAIS Expression
               | Expression MENOS Expression
               | Expression MULTIPLICA Expression
               | Expression COLCE Expression COLCD
               | Expression PONTO LENGTH
               | Expression PONTO Identifier PE Expression2 PD
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
def p_Expression2(p):
    '''
    Expression2 : Expression Expression3
                | empty
    '''
def p_Expression3(p):
    '''
    Expression3 : VIRGULA Expression Expression3
                | empty
    '''

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
    print("Syntax error found!!", p)


'''
DEBUG
'''
fp = codecs.open('programa1.txt', 'r', 'utf-8')
cadeia = fp.read()
fp.close()

parser = yacc.yacc()
result = parser.parse(cadeia)

print(result)