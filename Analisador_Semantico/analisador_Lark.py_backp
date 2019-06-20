import sys
from lark import Lark, tree, Token
import logging
#import analisador_lexico
logging.basicConfig(level=logging.DEBUG)
import Analisador_Lexico as AL

#Caminho Programa a ser executado
path = '../Programas_MiniJava/programa1.java'

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
    elif token == '[':
        return 'COLCE'
    elif token == ']':
        return 'COLCD'
    elif token == ',':
        return 'VIRGULA'
    elif token == '.':
        return 'PONTO'
    elif token[0] == '0' or token[0] == '1' or token[0] == '2' or token[0] == '3' or token[0] == '4' or token[0] == '5' \
        or token[0] == '6' or token[0] == '7' or token[0] == '8' or token[0] == '9':
        return token
    elif token == 'System.out.println':
        return 'SYSTEMOUTPRINTLN'
    else:
        if token.lower() in palavras_reservadas:
            return token
        else:
            return token
    """
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
        elif token == ',':
            return 'VIRGULA'
        elif token == '.':
            return 'PONTO'
        elif token == ';':
            return 'PONTOVIRGULA'
        elif token == ':':
            return 'PONTOPONTO'

        if token == '<':
            return 'MENOR'
        """

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

def make_png(sentence, filename):
    tree.pydot__tree_to_png(sentence, filename)

#DEBUG

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
    ?prog: mainclass ( classdeclaration )* 
    ?mainclass: class id "{" public static void main "(" string colce colcd id ")" "{" cmd "}" "}" 
    ?classdeclaration: class id (extends id)? "{" ( var )* ( method )* "}"
    ?var: type id ";"
    ?method: public type id "(" (type id ( virgula type id )* )? ")" "{" ( var )* ( cmd )* return exp ";" "}" 
    ?type: int colce colcd 
        |	boolean 
        |	int
        |	id 
        
    ?cmd: "{" ( cmd )* "}"
             | if "(" exp ")" cmd
             |	if "(" exp ")" cmd else cmd
             |	while "(" exp ")" cmd
             |	systemoutprintln "(" exp ")" ";"
             |	id igual exp ";"
             |	id colce exp colcd igual exp ";"
             
    exp: exp ecomercial _rexp
              | _rexp
              
    _rexp: _rexp menor _aexp
         | _rexp comparacao _aexp
         | _rexp diferente _aexp
         | _aexp
    _aexp: _aexp mais _mexp 
         | _aexp menos _mexp 
         | _mexp
    _mexp: _mexp multiplica _sexp 
         | _mexp divide _sexp 
         | _sexp
    _sexp: negacao _sexp 
         | menos _sexp 
         | true
         | false
         | numero
         | null
         | new int colce exp colcd
         | _pexp ponto length
         | _pexp colce exp colcd
         | _pexp
    _pexp: id
         | this
         | new id "(" ")"
         | "(" exp ")"
         | _pexp ponto id
         | _pexp ponto id "(" ( exp ( virgula exp )* )? ")"               
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
    //pe: "PE"
    //pd: "PD"
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
    //pontovirgula: "PONTOVIRGULA"
    //pontoponto: "PONTOPONTO" 
    numero: /[0-9]+/
    //numero: "NUMERO"
    //ID: "[a-zA-Z_][a-zA-Z_0-9]*"
    //id: "ID"
    id: /[a-zA-Z_][a-zA-Z_0-9]*/
    //WS: "[ \t]+" (%ignore)
    //%import commom.WS
    %ignore " "

'''
def tok_to_int(tok):
    "Converte o valor de 'tok'=string em numero inteiro"
    return Token.new_borrow_pos(tok.type, int(tok), tok)

'''
lexer_callbacks: funcao para conversao de tipos. Ex: string em numero
'''
#print(texto)
vet_ids = []
p = Lark(collision_gramar, parser='lalr', start='prog', lexer_callbacks= {'numero': tok_to_int, 'numero': vet_ids.append,})
#p = Lark(collision_gramar, parser='lalr', start='prog')
sentence = p.parse(texto)
tree = p.parse(texto).pretty()
#tree = p.parse(texto)
print(tree)
make_png(sentence, "teste.png")

