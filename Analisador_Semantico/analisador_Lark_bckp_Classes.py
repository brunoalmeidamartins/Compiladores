import sys
from lark import Lark, tree, Token, Transformer, Visitor
import logging

logging.basicConfig(level=logging.DEBUG)
import Analisador_Lexico as AL


class AnalisadorLark():
    palavras_reservadas = ['abstract', 'assert', 'boolean', 'break', 'byte', 'case', 'catch', 'char', 'class', 'const',
                           'continue', 'default', 'do', 'double', 'else', 'enum', 'extends', 'final', 'finally',
                           'float',
                           'for', 'if', 'goto', 'implements', 'import', 'instanceof', 'int', 'interface', 'long',
                           'native',
                           'new', 'package', 'private', 'protected', 'public', 'return', 'short', 'static', 'strictfp',
                           'super', 'switch', 'synchronized', 'this', 'throw', 'throws', 'transient', 'try', 'void',
                           'volatile', 'while', 'main', 'string', 'length', 'System', 'out',
                           'println', 'System.out.println']

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
        elif token[0] == '0' or token[0] == '1' or token[0] == '2' or token[0] == '3' or token[0] == '4' or token[
            0] == '5' \
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

        # Arrumando o vetor de tokens
        cont = 0
        tokens = ''
        for token in vetor_tokens:
            if cont == 0:
                tokens = (self.trocaOperadoresPorPalavras(token[2])).upper()
            else:
                tokens = tokens + ' ' + (self.trocaOperadoresPorPalavras(token[2])).upper()
            cont += 1
            # tokens = tokens +' '+token[2].lower()

        return tokens

    def make_png(self, sentence, filename):
        tree.pydot__tree_to_png(sentence, filename)

    # DEBUG

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
        # print(texto)
        # texto = retornaTokensArquivo(path)
        collision_gramar = '''
            ?goal: mainclass ( classdeclaration )* 
            ?mainclass: class id "{" public static void main "(" string colce colcd id ")" "{" statement "}" "}" 
            ?classdeclaration: class id (extends id)? "{" ( vardeclaration )* ( methoddeclaration )* "}"
            ?vardeclaration: type id ";"
            ?methoddeclaration: public type id "(" (type id ( virgula type id )* )? ")" "{" ( vardeclaration )* ( statement )* return expression ";" "}" 
            ?type: int colce colcd 
                |	boolean 
                |	int
                |	id
            ?statement: "{" ( statement )* "}"
                         | if "(" expression ")" statement else statement
                         |	while "(" expression ")" statement
                         |	systemoutprintln "(" expression ")" ";"
                         |	id igual expression ";"
                         |	id colce expression colcd igual expression ";"
            ?expression: expression ( ecomercial | menor | mais | menos | multiplica ) expression
                       | expression colce expression colcd
                       | expression ponto length
                       | expression ponto id "(" ( expression ( virgula expression)* )? ")"
                       | numero
                       | true
                       | false
                       | id
                       | this
                       | new int colce expression colcd
                       | new id "(" ")"
                       | negacao expression
                       | "(" expression ")"
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
        # print(texto)
        vet_ids = []
        # p = Lark(collision_gramar, parser='lalr', start='prog', lexer_callbacks= {'numero': tok_to_int, 'numero': vet_ids.append,})
        p = Lark(collision_gramar, parser='lalr', start='goal')
        # sentence = p.parse(texto)
        tree = p.parse(texto)
        tree1 = p.parse(texto).pretty()
        # tree = p.parse(texto)
        # print(tree)
        # self.make_png(tree, "teste1.png")
        return tree


#######Visitor#####
class And(Exp):
    def __init__(self, ae1, ae2):
        self.e1 = ae1
        self.e2 = ae2

    def accept(self, v):
        v.visit(self)

    def accept(self, v):
        return v.visit(self)


class ArrayAssign(Statement):
    def __init__(self, ai, ae1, ae2):
        self.i = ai
        self.e1 = ae1
        self.e2 = ae2

    def accept(self, v):
        v.visit(self)

    def accept(self, v):
        return v.visit(self)


class ArrayLength(Exp):
    def __init__(self, ae):
        self.e = ae

    def accept(self, v):
        v.visit(self)

    def accept(self, v):
        return v.visit(self)


class ArrayLookup(Exp):
    def __init__(self, ae1, ae2):
        self.e1 = ae1
        self.e2 = ae2

    def accept(self, v):
        v.visit(self)

    def accept(self, v):
        return v.visit(self)


class Assing(Statement):
    def __init__(self, ai, ae):
        self.i = ai
        self.e = ae

    def accept(self, v):
        v.visit(self)

    def accept(self, v):
        return v.visit(self)


class Block(Statement):
    def __init__(self, asl):
        self.sl = asl

    def accept(self, v):
        v.visit(self)

    def accept(self, v):
        return v.visit(self)


class BooleanType(Type):
    def accept(self, v):
        v.visit(self)

    def accept(self, v):
        return v.visit(self)


class Call(exp):
    def __init__(self, ae, ai, ael):
        self.e = ae
        self.i = ai
        self.el = ael

    def accept(self, v):
        v.visit(self)

    def accept(self, v):
        return v.visit(self)


class ClassDecl():
    def accept(self, v):
        pass


class ClassDeclExtends(ClassDecl):
    def __init__(self, ai, aj, avl, aml):
        self.i = ai
        self.j = aj
        self.vl = avl
        self.ml = aml

    def accept(self, v):
        v.visit(self)

    def accept(self, v):
        return v.visit(self)


class ClassDeclList():
    def __init__(self):
        self.lista = []

    def addElement(self, n):
        self.lista.append(n)

    def elementAt(self, i):
        return self.elementAt(i)

    def size(self):
        return len(self.lista)


class ClassDeclSimple(ClassDecl):
    def __init__(self, ai, avl, aml):
        self.i = ai
        self.vl = avl
        self.ml = aml

    def accept(self, v):
        v.visit(self)

    def accept(self, v):
        return v.visit(self)


class Exp():
    def accept(self, v):
        pass


class ExpList():
    def __init__(self):
        self.lista = []

    def addElement(self, n):
        self.lista.append(n)

    def elementAt(self, i):
        return self.elementAt(i)

    def size(self):
        return len(self.lista)


class false(Exp):
    def accept(self, v):
        v.visit(self)

    def accept(self, v):
        return v.visit(self)


class Formal():
    def __init__(self, at, ai):
        self.t = at
        self.i = ai

    def accept(self, v):
        v.visit(self)

    def accept(self, v):
        return v.visit(self)


class FormalList():
    def __init__(self):
        self.lista = []

    def addElement(self, n):
        self.lista.append(n)

    def elementAt(self, i):
        return self.elementAt(i)

    def size(self):
        return len(self.lista)


class Identifier():
    def __init__(self, asf):
        self.s = asf

    def accept(self, v):
        v.visit(self)

    def accept(self, v):
        return v.visit(self)

    def toString(self):
        return self.s


class IdentifierExp(Exp):
    def __init__(self, asf):
        self.s = asf

    def accept(self, v):
        v.visit(self)

    def accept(self, v):
        return v.visit(self)


class IdentifierType(Type):
    def __init__(self, asf):
        self.s = asf

    def accept(self, v):
        v.visit(self)

    def accept(self, v):
        return v.visit(self)


class If(Statement):
    def __init__(self, ae, as1, as2):
        self.e = ae
        self.s1 = as1
        self.s2 = as2

    def accept(self, v):
        v.visit(self)

    def accept(self, v):
        return v.visit(self)


class IntArrayType(Type):
    def accept(self, v):
        v.visit(self)

    def accept(self, v):
        return v.visit(self)


class IntergerLiteral(Exp):
    def __init__(self, ai):
        self.i = ai

    def accept(self, v):
        v.visit(self)

    def accept(self, v):
        return v.visit(self)


class IntegerType(Type):
    def accept(self, v):
        v.visit(self)

    def accept(self, v):
        return v.visit(self)


class LessThan(Exp):
    def __init__(self, ae1, ae2):
        self.e1 = ae1
        self.e2 = ae2

    def accept(self, v):
        v.visit(self)

    def accept(self, v):
        return v.visit(self)


class MainClass():
    def __init__(self, ai1, ai2, asf):
        self.i1 = ai1
        self.i2 = ai2
        self.s = asf

    def accept(self, v):
        v.visit(self)

    def accept(self, v):
        return v.visit(self)


class MethodDecl():
    def __init__(self, at, ai, afl, avl, asl, ae):
        self.t = at
        self.i = ai
        self.fl = afl
        self.vl = avl
        self.sl = asl
        self.e = ae

    def accept(self, v):
        v.visit(self)

    def accept(self, v):
        return v.visit(self)


class MethodDeclList():
    def __init__(self):
        self.lista = []

    def addElement(self, n):
        self.lista.append(n)

    def elementAt(self, i):
        return self.elementAt(i)

    def size(self):
        return len(self.lista)


class Minus(Exp):
    def __init__(self, ae1, ae2):
        self.e1 = ae1
        self.e2 = ae2

    def accept(self, v):
        v.visit(self)

    def accept(self, v):
        return v.visit(self)


class NewArray(Exp):
    def __init__(self, ae):
        self.e = ae

    def accept(self, v):
        v.visit(self)

    def accept(self, v):
        return v.visit(self)


class NewObject(Exp):
    def __init__(self, ai):
        self.i = ai

    def accept(self, v):
        v.visit(self)

    def accept(self, v):
        return v.visit(self)


class Not(Exp):
    def __init__(self, ae):
        self.e = ae

    def accept(self, v):
        v.visit(self)

    def accept(self, v):
        return v.visit(self)


class Plus(Exp):
    def __init__(self, ae1, ae2):
        self.e1 = ae1
        self.e2 = ae2

    def accept(self, v):
        v.visit(self)

    def accept(self, v):
        return v.visit(self)


class Print(Statement):
    def __init__(self, ae):
        self.e = ae

    def accept(self, v):
        v.visit(self)

    def accept(self, v):
        return v.visit(self)


class Program():
    def __init__(self, am, acl):
        self.m = am
        self.cl = acl

    def accept(self, v):
        v.visit(self)

    def accept(self, v):
        return v.visit(self)


class Statement():
    def accept(self):
        pass


class StatementList():
    def __init__(self):
        self.lista = []

    def addElement(self, n):
        self.lista.append(n)

    def elementAt(self, i):
        return self.elementAt(i)

    def size(self):
        return len(self.lista)


class This(Exp):
    def accept(self, v):
        v.visit(self)

    def accept(self, v):
        return v.visit(self)


class Times(Exp):
    def __init__(self, ae1, ae2):
        self.e1 = ae1
        self.e2 = ae2

    def accept(self, v):
        v.visit(self)

    def accept(self, v):
        return v.visit(self)


class true(Exp):
    def accept(self, v):
        v.visit(self)

    def accept(self, v):
        return v.visit(self)


class Type():
    def accept(self, v):
        pass


class VarDecl():
    def __init__(self, at, ai):
        self.t = at
        self.i = ai

    def accept(self, v):
        v.visit(self)

    def accept(self, v):
        return v.visit(self)


class VarDeclList():
    def __init__(self):
        self.lista = []

    def addElement(self, n):
        self.lista.append(n)

    def elementAt(self, i):
        return self.elementAt(i)

    def size(self):
        return len(self.lista)


class While(Statement):
    def __init__(self, ae, asf):
        self.e = ae
        self.s = asf

    def accept(self, v):
        v.visit(self)

    def accept(self, v):
        return v.visit(self)


# Outras DepthFirstVisitor


class DepthFirstVisitor(Visitor):
    # MainClass m;
    # ClassDeclList cl;
    def visit(self, Program):
        n = Program
        n.m.accept(self)
        for i in n.cl.elementAt:
            i.accept(self)

    # Identifier    i1, i2;
    # Statement    s;
    def visit(self, MainClass):
        n = MainClass
        n.i1.accept(self)
        n.i2.accept(self)
        n.s.accept(self)

    # Identifier i
    # VarDeclList vl
    # MethodDeclList ml
    def visit(self, ClassDeclSimple):
        n = ClassDeclSimple
        n.i.accept(self)
        for i in n.vl.elementAt:
            i.accept(self)
        for i in n.ml.elementAt:
            i.accept(self)

    # Identifier i
    # Identifier j
    # VarDeclList vl
    # MethodDeclList
    def visit(self, ClassDeclExtends):
        n = ClassDeclExtends
        n.i.accept(self)
        n.j.accept(self)
        for i in n.vl.elementAt:
            i.accept(self)
        for i in n.ml.elementAt:
            i.accept(self)

    # Type t
    # Identifier i
    def visit(self, VarDecl):
        n = VarDecl
        n.t.accept(self)
        n.i.accept(self)

    # Type    t;
    # Identifier    i;
    # FormalList    fl;
    # VarDeclList    vl;
    # StatementList    sl;
    # Exp    e;
    def visit(self, MethodDecl):
        n = MethodDecl
        n.t.accept(self)
        n.i.accept(self)
        for i in n.fl.elementAt:
            i.accept(self)

    # Type t
    # Identifier i
    def visit(self, Formal):
        n = Formal
        n.t.accept(self)
        n.i.accept(self)

    def visit(self, IntArrayType):
        pass

    def visit(self, BooleanType):
        pass

    def visit(self, IntergerType):
        pass

    def visit(self, Identifier):
        pass

    # String s;
    def visit(self, IdentifierType):
        pass

    # StatementList sl
    def visit(self, Block):
        n = Block
        for i in n.sl.elementAt:
            i.accept(self)

    # Exp e
    # Statement s1, s2
    def visit(self, If):
        n = If
        n.e.accept(self)
        n.s1.accept(self)
        n.s2.accept(self)

    # Exp e
    # Statement s
    def visit(self, While):
        n = While
        n.e.accept(self)
        n.s.accept(self)

    # Exp e
    def visit(self, Print):
        n = Print
        n.e.accept(self)

    # Identifier i
    # Exp e
    def visit(self, Assign):
        n = Assign
        n.i.accept(self)
        n.e.accept(self)

    # Identifier i
    # Exp e1, e2
    def visit(self, ArrayAssign):
        n = ArrayAssign
        n.i.accept(self)
        n.e1.accept(self)
        n.e2.accept(self)

    # Exp e1, e2
    def visit(self, And):
        n = And
        n.e1.accept(self)
        n.e2.accept(self)

    # Exp e1, e2
    def visit(self, LessThan):
        n = LessThan
        n.e1.accept(self)
        n.e2.accept(self)

    # Exp e1, e2
    def visit(self, Plus):
        n = Plus
        n.e1.accept(self)
        n.e2.accept(self)

    # Exp e1, e2
    def visit(self, Minus):
        n = Minus
        n.e1.accept(self)
        n.e2.accept(self)

    # Exp e1, e2
    def visit(self, Times):
        n = Times
        n.e1.accept(self)
        n.e2.accept(self)

    # Exp e1, e2
    def visit(self, ArrayLookup):
        n = ArrayLookup
        n.e1.accept(self)
        n.e2.accept(self)

    # Exp e
    def visit(self, ArrayLength):
        n = ArrayLength
        n.e.accept(self)

    # Exp e
    # Identifier i
    # ExpList el
    def visit(self, Call):
        n = Call
        n.e.accept(self)
        n.i.accept(self)
        for i in n.el.elementAt:
            i.accept(self)

    # int i
    def visit(self, IntergerLiteral):
        pass

    def visit(self, true):
        pass

    def visit(self, false):
        pass

    # String s
    def visit(self, IdentifierExp):
        pass

    def visit(self, This):
        pass

    # Exp e
    def visit(self, NewArray):
        n = NewArray
        n.e.accept(self)

    # Identifier i
    def visit(self, NewObject):
        pass

    # Exp e
    def visit(self, Not):
        n = Not
        n.e.accept(self)

    # String s
    def visit(self, Identifier):
        pass


#######FIM Visitor#####
class ImplementaVisitor(Visitor):
    def visitprog(self, tree):
        assert tree.data == "prog"


class ImplementaTransformer(Transformer):
    def exp(self, args):
        print(args)
        # return eval(args[0])


# Main

analisador = AnalisadorLark()
tree = analisador.funcaoPrincipal('../Programas_MiniJava/programa1.java')
# print(tree.pretty())
print(ImplementaTransformer().transform(tree))