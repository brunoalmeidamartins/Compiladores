import ply.lex as lex
import ply.yacc as yacc
import sys

tokens1 = ['INT', 'NAME' , 'PLUS' , 'MINUS' , 'DIVIDE' , 'MULTIPLY' , 'EQUALS']

palavras_reservadas = ['ABSTRACT', 'ASSERT', 'BOOLEAN', 'BREAK', 'BYTE', 'CASE', 'CATCH',
          'CHAR', 'CLASS', 'CONST', 'CONTINUE', 'DEFAULT', 'DO', 'DOUBLE', 'ELSE',
          'ENUM', 'EXTENDS', 'FINAL', 'FINALLY', 'FLOAT', 'FOR', 'IF', 'GOTO',
          'IMPLEMENTS', 'IMPORT', 'INSTANCEOF', 'INT', 'INTERFACE', 'LONG', 'NATIVE',
          'NEW', 'PACKAGE', 'PRIVATE', 'PROTECTED', 'PUBLIC', 'RETURN', 'SHORT', 'STATIC',
          'STRICTFP', 'SUPER', 'SWITCH', 'SYNCHRONIZED', 'THIS', 'THROW', 'THROWS', 'TRANSIENT',
          'TRY', 'VOID', 'VOLATILE', 'WHILE', 'MAIN', 'STRING', 'LENGTH', 'SYSTEM', 'OUT',
          'PRINTLN', 'SYSTEM.OUT.PRINTLN']
tokens = tokens1 + palavras_reservadas


#list of tokens , for grammar checking

t_PLUS = r'\+'
t_MINUS = r'\-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'\/'
t_EQUALS = r'\='

t_ignore = r' ' # used for ignoring spaces between numbers and operators


#Palavras Reservadas
t_ABSTRACT = r'\abstract'
t_ASSERT = r'\assert'
t_BOOLEAN = r'\boolean'
t_BREAK = r'\break'
t_BYTE = r'\byte'
t_CASE = r'\case'
t_CATCH = r'\catch'
t_CHAR = r'\char'
t_CLASS = r'\class'
t_CONST = r'\const'
t_CONTINUE = r'\continue'
t_DEFAULT = r'\default'
t_DO = r'\do'
t_DOUBLE = r'\double'
t_ELSE = r'\else'
t_ENUM = r'\enum'
t_EXTENDS = r'\extends'
t_FINAL = r'\final'
t_FINALLY = r'\finally'
t_FLOAT = r'\float'
t_FOR = r'\for'
t_IF = r'\if'
t_GOTO = r'\goto'
t_IMPLEMENTS = r'\implements'
t_IMPORT = r'\import'
t_INSTANCEOF = r'\instanceof'
t_INT = r'\int'
t_INTERFACE = r'\interface'
t_LONG = r'\long'
t_NATIVE = r'\native'
t_NEW = r'\new'
t_PACKAGE = r'\package'
t_PRIVATE = r'\private'
t_PROTECTED = r'\protected'
t_PUBLIC = r'\public'
t_RETURN = r'\return'
t_SHORT = r'\short'
t_STATIC = r'\static'
t_STRICTFP = r'\strictfp'
t_SUPER = r'\super'
t_SWITCH = r'\switch'
t_SYNCHRONIZED = r'\synchronized'
t_THIS = r'\this'
t_THROW = r'\throw'
t_THROWS = r'\throws'
t_TRANSIENT = r'\transient'
t_TRY = r'\try'
t_VOID = r'\void'
t_VOLATILE = r'\volatile'
t_WHILE = r'\while'
t_MAIN = r'\main'
t_STRING = r'\string'
t_LENGTH = r'\length'
t_SYSTEM = r'\system'
t_OUT = r'\out'
t_PRINTLN = r'\println'
t_SYSTEM_OUT_PRINTLN = r'\system.out.println'


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

#lexer = lex.lex()




for i in tokens:
    print("t_" + i +" = r'\\"+i.lower()+"'")











'''
def p_expreg_soma(p):
    'expreg : expreg SOMA term'

def p_expreg_subtracao(p):
    'expreg : expreg SUBTRACAO term'

def p_expreg_term(p):
    'expreg : term'

def p_term_multiplicacao(p):
    'term : term MULTIPLICACAO factor'

def p_term_divisao(p):
    'term : term DIVISAO factor'

def p_term_factor(p):
    'term : factor'

def p_factor_num(p):
    'factor : NUMERO'

def p_error(p):
    print("Syntax error in input!")

parser = yacc.yacc()

sCaminhoImg = 'teste.txt'
oArquivo = open(sCaminhoImg)

sData = ''
with oArquivo as oInfo:
    for sLine in oInfo.readlines():
        if not sLine:
            continue
        parser.parse(sLine)

'''