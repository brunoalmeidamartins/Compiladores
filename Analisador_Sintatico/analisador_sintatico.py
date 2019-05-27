import ply.lex as lex
import ply.yacc as yacc
import sys

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

