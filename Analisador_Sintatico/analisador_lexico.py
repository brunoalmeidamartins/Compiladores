import ply.lex as lex
import re
import codecs
import os
import sys

#(, ), [, ], {, }, ;, ., ,, =, ¡, ==, !=, +, -, *, /, && e !;

tokens = ['ID', 'NUMERO' , 'MAIS', 'MENOS', 'DIVIDE', 'MULTIPLICA', 'IGUAL', 'COMPARACAO', 'PE', 'PD', 'CE', 'CD',
          'COLCE', 'COLCD', 'MENOR', 'MAIOR', 'MENORIGUAL', 'MAIORIGUAL', 'NEGACAO', 'DIFERENTE', 'ECOMERCIAL', 'VIRGULA', 'PONTO',
          'PONTOVIRGULA', 'PONTOPONTO']




palavras_reservadas = ['ABSTRACT', 'ASSERT', 'BOOLEAN', 'BREAK', 'BYTE', 'CASE', 'CATCH',
          'CHAR', 'CLASS', 'CONST', 'CONTINUE', 'DEFAULT', 'DO', 'DOUBLE', 'ELSE',
          'ENUM', 'EXTENDS', 'FINAL', 'FINALLY', 'FLOAT', 'FOR', 'IF', 'GOTO',
          'IMPLEMENTS', 'IMPORT', 'INSTANCEOF', 'INT', 'INTERFACE', 'LONG', 'NATIVE',
          'NEW', 'PACKAGE', 'PRIVATE', 'PROTECTED', 'PUBLIC', 'RETURN', 'SHORT', 'STATIC',
          'STRICTFP', 'SUPER', 'SWITCH', 'SYNCHRONIZED', 'THIS', 'THROW', 'THROWS', 'TRANSIENT',
          'TRY', 'VOID', 'VOLATILE', 'WHILE', 'MAIN', 'STRING', 'LENGTH','SYSTEMOUTPRINTLN', 'SYSTEM', 'OUT',
          'PRINTLN', 'TRUE', 'FALSE', 'NULL']

tokens = tokens + palavras_reservadas

#Lista de tokens para checagem da gramatica
def t_SYSTEM_OUT_PRINTLN(t):
    r'System.out.println'
    t.value = 'SYSTEMOUTPRINTLN'
    t.type = t.value
    return t

t_ignore = ' \t' # Ignora espaco e tabulacoes
t_MAIS = r'\+'
t_MENOS = r'-'
t_MULTIPLICA = r'\*'
t_DIVIDE = r'/'
t_IGUAL = r'='
t_COMPARACAO = r'=='
t_PE = r'\('
t_PD = r'\)'
t_CE = r'\{'
t_CD = r'\}'
t_COLCE = r'\['
t_COLCD = r'\]'
t_MENOR = r'<'
t_MAIOR = r'>'
t_MENORIGUAL = r'<='
t_MAIORIGUAL = r'>='
t_NEGACAO = r'!'
t_DIFERENTE = r'\!='
t_ECOMERCIAL = r'\&&'
t_VIRGULA = r','
t_PONTO = r'\.'
t_PONTOVIRGULA = r';'
t_PONTOPONTO = r':'

#Comentarios multiplas linhas /*...*/
def t_COMMENT_MULTIPLAS_LINHAS(t):
    r'/\*((.|\n)*?)\*/'
    pass

#Nova linha
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

#Captura ID e verifica se eh uma palavra reservada
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*' #star means 0 or more, first char is a-zA-z , second character is a-zA-z0-9
    if t.value.upper() in palavras_reservadas:
        t.value = t.value.upper()
        t.type = t.value
    return t

#Captura os comentarios de uma linha
def t_COMMENT(t):
    r'\/\/.*'
    pass

#Captura o numeros inteiros
def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t # t is our token object

#Captura erro de caracter ilegal
def t_error(t):
    print('Illegal caracters %s' % t.value[0])
    t.lexer.skip(1) # skips 1 token onwards

#Usado para retornar a coluna do erro
def find_column(input, token):
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1


'''
DEBUG
'''

lexer = lex.lex()
