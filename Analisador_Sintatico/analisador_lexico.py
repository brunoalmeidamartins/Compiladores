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
          'TRY', 'VOID', 'VOLATILE', 'WHILE', 'MAIN', 'STRING', 'LENGTH', 'SYSTEM', 'OUT',
          'PRINTLN', 'TRUE', 'FALSE', 'NULL']

'''
palavras_reservadas = {
                        'abstract':'ABSTRACT',
                        'assert':'ASSERT',
                        'boolean':'BOOLEAN',
                        'break':'BREAK',
                        'byte':'BYTE',
                        'case':'CASE',
                        'catch':'CATCH',
                        'char':'CHAR',
                        'class':'CLASS',
                        'const':'CONST',
                        'continue':'CONTINUE',
                        'default':'DEFAULT',
                        'do':'DO',
                        'double':'DOUBLE',
                        'else':'ELSE',
                        'enum':'ENUM',
                        'extends':'EXTENDS',
                        'final':'FINAL',
                        'finally':'FINALLY',
                        'float':'FLOAT',
                        'for':'FOR',
                        'if':'IF',
                        'goto':'GOTO',
                        'implements':'IMPLEMENTS',
                        'import':'IMPORT',
                        'instanceof':'INSTANCEOF',
                        'int':'INT',
                        'interface':'INTERFACE',
                        'long':'LONG',
                        'native':'NATIVE',
                        'new':'NEW',
                        'package':'PACKAGE',
                        'private':'PRIVATE',
                        'protected':'PROTECTED',
                        'public':'PUBLIC',
                        'return':'RETURN',
                        'short':'SHORT',
                        'static':'STATIC',
                        'strictfp':'STRICTFP',
                        'super':'SUPER',
                        'switch':'SWITCH',
                        'synchronized':'SYNCHRONIZED',
                        'this':'THIS',
                        'throw':'THROW',
                        'throws':'THROWS',
                        'transient':'TRANSIENT',
                        'try':'TRY',
                        'void':'VOID',
                        'volatile':'VOLATILE',
                        'while':'WHILE',
                        'main':'MAIN',
                        'string':'STRING',
                        'length':'LENGTH',
                        'system':'SYSTEM',
                        'out':'OUT',
                        'println':'PRINTLN',
                        #'system_out_println':'SYSTEM.OUT.PRINTLN',
}
'''
tokens = tokens + palavras_reservadas


#list of tokens , for grammar checking
t_ignore = ' \t' # used for ignoring spaces between numbers and operators
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

#def t_TABULACOES(t):
#    r'\s'
#    pass
def t_COMMENT_MULTIPLAS_LINHAS(t):
    r'\/\*(?s).\*\/'
    pass

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*' #star means 0 or more, first char is a-zA-z , second character is a-zA-z0-9
    if t.value.upper() in palavras_reservadas:
        t.value = t.value.upper()
        t.type = t.value
    return t

def t_COMMENT(t):
    r'\/\/.*'
    pass

def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t # t is our token object

def t_error(t):
    print('Illegal caracters %s' % t.value[0])
    t.lexer.skip(1) # skips 1 token onwards

def find_column(input, token):
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1


'''
DEBUG
'''

#fp = codecs.open('teste.txt','r','utf-8')
#cadeia = fp.read()
#fp.close()

#print(tokens)
lexer = lex.lex()

#lexer.input(cadeia)


#while True:
#    tok = lexer.token()
#    if not tok : break
#    print(tok)
