from lark import Lark
import logging
#import analisador_lexico
logging.basicConfig(level=logging.DEBUG)

import Analisador_Lexico as AL
from analisador_lexico import tokens

palavras_reservadas = ['abstract', 'assert', 'boolean', 'break', 'byte', 'case', 'catch', 'char', 'class', 'const',
                           'continue', 'default', 'do', 'double', 'else', 'enum', 'extends', 'final', 'finally',
                           'float',
                           'for', 'if', 'goto', 'implements', 'import', 'instanceof', 'int', 'interface', 'long',
                           'native',
                           'new', 'package', 'private', 'protected', 'public', 'return', 'short', 'static', 'strictfp',
                           'super', 'switch', 'synchronized', 'this', 'throw', 'throws', 'transient', 'try', 'void',
                           'volatile', 'while', 'main', 'string', 'length', 'System', 'out',
                           'println','System.out.println']

def trocaOperadoresPorPalavras(token):
    # print(token)
    if token == '+':
        return 'MAIS'
    elif token == '-':
        return 'MENOS'
    elif token == '*':
        return 'MULTIPLICA'
    elif token == '/':
        return 'DIVIDE'
    elif token == '=':
        return 'IGUAL'
    elif token == '==':
        return 'COMPARACAO'
    elif token == '(':
        return 'PE'
    elif token == ')':
        return 'PD'
    elif token == '{':
        return 'CE'
    elif token == '}':
        return 'CD'
    elif token == '[':
        return 'COLCE'
    elif token == ']':
        return 'COLCD'
    elif token == '<':
        return 'MENOR'
    elif token == '>':
        return 'MAIOR'
    elif token == '<=':
        return 'MENORIGUAL'
    elif token == '>=':
        return 'MAIORIGUAL'
    elif token == '!':
        return 'NEGACAO'
    elif token == '!=':
        return 'DIFERENTE'
    elif token == '&&':
        return 'ECOMERCIAL'
    elif token == ',':
        return 'VIRGULA'
    elif token == '.':
        return 'PONTO'
    elif token == ';':
        return 'PONTOVIRGULA'
    elif token == ':':
        return 'PONTOPONTO'
    elif token[0] == '0' or token[0] == '1' or token[0] == '2' or token[0] == '3' or token[0] == '4' or token[0] == '5' \
        or token[0] == '6' or token[0] == '7' or token[0] == '8' or token[0] == '9':
        return 'NUMERO'
    elif token == 'System.out.println':
        return 'SYSTEMOUTPRINTLN'
    else:
        if token.lower() in palavras_reservadas:
            return token
        else:
            return 'ID'

def retornaTokensArquivo(caminho_arquivo):
    path_arquivo = caminho_arquivo
    analisador_lexico = AL.analisador_lexico()
    vetor_tokens = analisador_lexico.funcaoPrincipalAnalisadorLexico(path_arquivo)

    #Arrumando o vetor de tokens
    cont = 0
    tokens = ''
    for token in vetor_tokens:
        if cont == 0:
            tokens = (trocaOperadoresPorPalavras(token[2])).upper()
        else:
            tokens = tokens +' '+ (trocaOperadoresPorPalavras(token[2])).upper()
        cont +=1
        #tokens = tokens +' '+token[2].lower()

    return tokens


path = 'Programas_MiniJava/programa1.java'


with open(path) as f:
    texto_arq = f.readlines()

#print(texto)
texto = ''
for i in texto_arq:
    texto = texto + i

texto = retornaTokensArquivo(path)
cont = 1
text = ''
for i in texto:
    text = text + i
    if i == ' ':
        #print(text, cont)
        cont +=1
        text = ''
#print(texto)
#texto = retornaTokensArquivo(path)

collision_gramar = ''' 
    start: goal
    ?goal: mainclass ( classdeclaration )*
    ?mainclass: class id ce public static void main pe string colce colcd id pd ce statement cd cd
    ?classdeclaration: class id (extends id)? ce ( vardeclaration )* ( methoddeclaration )* cd
    ?vardeclaration: type id pontovirgula
    ?methoddeclaration: public type id pe (type id ( virgula type id )* )? pd ce ( vardeclaration )* ( statement )* return expression pontovirgula cd
    ?type: int colce colcd
        |	boolean
        |	int -> int
        |	id -> id
        
    ?statement: ce ( statement )* cd
             |	if pe expression pd statement else statement
             |	while pe expression pd statement
             |	systemoutprintln pe expression pd pontovirgula
             |	id igual expression pontovirgula
             |	id colce expression colcd igual expression pontovirgula
             
    ?expression: expression ( ecomercial | menor | mais | menos | multiplica ) expression
              |	expression colce expression colcd
              |	expression ponto length
              |	expression ponto id pe ( expression ( virgula expression )* )? pd
              |	numero -> numero
              |	true
              |	false -> false
              |	id
              |	this -> this
              |	new int colce expression colcd
              |	new id pe pd
              |	negacao expression
              |	pe expression pd
              
    //Tokens
    string: "STRING"
    systemoutprintln: "SYSTEMOUTPRINTLN"
    main: "MAIN"
    static: "STATIC"
    void: "VOID"
    class: "CLASS"
    extends: "EXTENDS"
    public: "PUBLIC"
    return: "RETURN"
    boolean: "BOOLEAN"
    int: "INT"
    if: "IF"
    else: "ELSE"
    while: "WHILE"
    true: "TRUE"
    false: "FALSE"
    null: "NULL"
    new: "NEW"
    length: "LENGTH"
    this: "THIS"
    mais: "MAIS"
    menos: "MENOS"
    multiplica: "MULTIPLICA"
    divide: "DIVIDE"
    igual: "IGUAL"
    comparacao: "COMPARACAO"
    pe: "PE"
    pd: "PD"
    ce: "CE"
    cd: "CD"
    colce: "COLCE"
    colcd: "COLCD"
    menor: "MENOR"
    maior: "MAIOR"
    menorigual: "MENORIGUAL"
    maiorigual: "MAIORIGUAL"
    negacao: "NEGACAO"
    diferente: "DIFERENTE"
    ecomercial: "ECOMERCIAL"
    virgula: "VIRGULA"
    ponto: "PONTO"
    pontovirgula: "PONTOVIRGULA"
    pontoponto: "PONTOPONTO"
    //numero: "\d+"
    numero: "NUMERO"
    //ID: "[a-zA-Z_][a-zA-Z_0-9]*"
    id: "ID"
    //WS: "[ \t]+" (%ignore)
    //%import commom.WS
    %ignore " "

'''
p = Lark(collision_gramar, parser='lalr')
parser = p.parse(texto)
print(parser)
