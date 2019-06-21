import sys
from lark import Lark, tree, Token, Transformer, Visitor
import logging
logging.basicConfig(level=logging.DEBUG)
import Analisador_Lexico as AL

import PrettyPrintVisitor as ppv
import Syntaxtree as syntax

class AnalisadorLark():

    palavras_reservadas = ['abstract', 'assert', 'boolean', 'break', 'byte', 'case', 'catch', 'char', 'class', 'const',
                               'continue', 'default', 'do', 'double', 'else', 'enum', 'extends', 'final', 'finally',
                               'float',
                               'for', 'if', 'goto', 'implements', 'import', 'instanceof', 'int', 'interface', 'long',
                               'native',
                               'new', 'package', 'private', 'protected', 'public', 'return', 'short', 'static', 'strictfp',
                               'super', 'switch', 'synchronized', 'this', 'throw', 'throws', 'transient', 'try', 'void',
                               'volatile', 'while', 'main', 'string', 'length', 'System', 'out',
                               'println','System.out.println']

    def trocaOperadoresPorPalavras(self, token):
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
            if token.lower() in self.palavras_reservadas:
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

    def retornaTokensArquivo(self, caminho_arquivo):
        path_arquivo = caminho_arquivo
        analisador_lexico = AL.analisador_lexico()
        vetor_tokens = analisador_lexico.funcaoPrincipalAnalisadorLexico(path_arquivo)

        #Arrumando o vetor de tokens
        cont = 0
        tokens = ''
        for token in vetor_tokens:
            if cont == 0:
                tokens = (self.trocaOperadoresPorPalavras(token[2])).upper()
            else:
                tokens = tokens +' '+ (self.trocaOperadoresPorPalavras(token[2])).upper()
            cont +=1
            #tokens = tokens +' '+token[2].lower()

        return tokens

    def make_png(self, sentence, filename):
        tree.pydot__tree_to_png(sentence, filename)

    #DEBUG

    def tok_to_int(tok):
        "Converte o valor de 'tok'=string em numero inteiro"
        return Token.new_borrow_pos(tok.type, int(tok), tok)

    '''
    lexer_callbacks: funcao para conversao de tipos. Ex: string em numero
    '''
    def funcaoPrincipal(self, caminho):
        # Caminho Programa a ser executado
        path = caminho
        with open(path) as f:
            texto_arq = f.readlines()

        # print(texto)
        texto = ''
        for i in texto_arq:
            texto = texto + i

        texto = self.retornaTokensArquivo(path)
        cont = 1
        text = ''
        for i in texto:
            text = text + i
            if i == ' ':
                # print(text, cont)
                cont += 1
                text = ''
        collision_gramar = '''
                    ?program: mainclass classdecl* -> program
                    ?mainclass: class id "{" public static void main "(" string colce colcd id ")" "{" statement "}" "}" -> mainclass
                    ?classdecl: class id "{" vardecl* methoddecl* "}" -> classceclcimple
                             | class id extends id "{" vardecl* methoddecl* "}" -> classdeclextends
                    ?vardecl: type id ";" -> vardecl
                    ?methoddecl: public type id "(" formallist ")" "{" vardecl* statement* return exp ";" "}" -> methoddecl
                    ?formallist: type id formalrest* -> formal
                               | 
                    ?formalrest: virgula type id
                    ?type: int colce colcd -> intarraytype
                        | boolean -> booleantype
                        | int -> integertype
                        | id -> identifiertype
                    ?statement: "{" statement* "}" -> block
                             | if "(" exp ")" statement else statement -> ifjava
                             | while "(" exp ")" statement -> whilejava
                             | systemoutprintln "(" exp ")" ";" -> printjava
                             | id igual exp ";" -> assign
                             | id colce exp colcd igual exp ";" -> arrayassign
                    ?exp: exp ecomercial exp -> andjava
                       | exp menor exp -> lessthan
                       | exp mais exp -> plus
                       | exp menos exp -> minus
                       | exp multiplica exp -> times
                       | exp colce exp colcd -> arraylooup
                       | exp ponto length -> arraylength
                       | exp ponto id "(" explist ")" -> call
                       | numero -> integerliteral
                       | true -> true
                       | false -> false
                       | id -> identifierexp
                       | this -> this
                       | new int colce exp colcd -> newarray
                       | new id "(" ")" -> newobject
                       | negacao exp -> notjava
                       | "(" exp ")"
                    ?explist: exp exprest* -> explist
                           | 
                    ?exprest: virgula exp

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
                    id: /[a-zA-Z_][a-zA-Z_0-9]*/ -> identifier
                    //WS: "[ \t]+" (%ignore)
                    //%import commom.WS
                    %ignore " "
                '''
        #print(texto)
        vet_ids = []
        #p = Lark(collision_gramar, parser='lalr', start='prog', lexer_callbacks= {'numero': tok_to_int, 'numero': vet_ids.append,})
        p = Lark(collision_gramar, parser='lalr', start='program')
        #sentence = p.parse(texto)
        tree = p.parse(texto)
        tree1 = p.parse(texto).pretty()
        #tree = p.parse(texto)
        #print(tree)
        #self.make_png(tree, "teste2.png")
        #print(texto)
        return tree
#######Visitor#####

#######FIM Visitor#####
class ImplementaVisitor(Visitor):

    def goal(self, tree):
        assert tree.data == "goal"

    def mainclass(self, tree):
        assert tree.data == "mainclass"

    def classdeclaration(self, tree):
        assert tree.data == "classdeclaration"

    def vardeclaration(self, tree):
        assert tree.data == "vardeclaration"

    def methoddeclartion(self, tree):
        assert tree.data == "methoddeclaration"

    def type(self, tree):
        assert tree.data == "type"
        #print(tree)

    def statement(self, tree):
        assert tree.data == "statement"

    def expression(self, tree):
        assert tree.data == "expression"
        print(tree.children[0])

    def string(self, tree):
        assert tree.data == "string"

    def systemoutprintln(self, tree):
        assert tree.data == "systemoutprintln"
        #print(tree)

    def numero(self, tree):
        assert tree.data == "numero"
        #print(tree.children[0])

    def ecomercial(self, tree):
        assert tree.data == "ecomercial"
        i = tree.children[0]
        e1 = tree.children[1]
        e2 = tree.children[2]

    def ArrayAssign(self, tree):
        assert  tree.data == "ArrayAssign"
        i = tree.children[0]
        e1 = tree.children[1]
        e2 = tree.children[2]

    def ArrayLength(self, tree):
        assert  tree.data == "ArrayAssign"
        e = tree.children[0]

    def ArrayLookup(self, tree):
        assert tree.data == "ArrayLookup"
        e1 = tree.children[0]
        e2 = tree.children[1]

    def Assign(self, tree):
        assert tree.data == "Assign"
        i = tree.children[0]
        e = tree.children[1]
    def Block(self, tree):
        assert  tree.data == "Block"
        sl = tree.children[0]

    def BooleanType(self, tree):
        assert tree.data == "BooleanType"

    def Call(self, tree):
        assert tree.data == "Call"
        e = tree.children[0]
        i = tree.children[1]
        el = tree.children[2]

    def ClassDecl(self, tree):
        pass
    def ClassDeclExtends(self, tree):
        assert tree.data == "CallDeclExtends"
        i = tree.children[0]
        j = tree.children[1]
        vl = tree.children[2]
        ml = tree.children[3]
    def ClassDeclList(self, tree):
        lista = []

    def accept(self, v):
        v.visit(self)

    def type_accept(self, v):
        return v.visit(self)

    def minus(self, tree):
        assert tree.data == "minus"
        e1 = tree.children[0]
        e2 = tree.children[2]
        print(e2)
class minus():
    pass



class ImplementaTransformer(Transformer):
    def exp(self, args):
        print(args)
        #return eval(args[0])



#Main

analisador = AnalisadorLark()
tree = analisador.funcaoPrincipal('../Programas_MiniJava/programa1.java')
#print(tree.pretty())
#print(ImplementaTransformer().transform(tree))
#print(tree)
#ImplementaVisitor().visit(tree)
#a = ppv.PrettyPrintVisitor()
#a.program_visit(tree)
#a = syntax
#b = a.program(ppv.PrettyPrintVisitor())
#print(dir(a))
ç