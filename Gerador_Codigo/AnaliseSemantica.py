import os, sys, re
from antlr4 import *
from antlr4.error import ErrorListener
import argparse

if __name__ is not None and "." in __name__:
	from .MiniJavaVisitor import MiniJavaVisitor
	from .MiniJavaListener import MiniJavaListener
else:
    from MiniJavaVisitor import MiniJavaVisitor
    from MiniJavaListener import MiniJavaListener

#Variaveis Globais
classe_atual = ''
regiao = 0


class ClassInfo(object):
    def __init__(self):
        self.name = ''
        self.extendName = ''

        self.fields = {}
        self.methods = {}

    def print(self):
        print("Classe: ", self.name)
        print(" extends", self.extendName)
        print(" FIELDS:")
        valores = self.fields.keys()
        for i in valores:
            print(" ",i, '->', self.fields.get(i).toString())
        print(" Metodos:")
        valores = self.methods.keys()
        for i in valores:
            print(" ", i, '->', self.methods.get(i).toString())

class FieldInfo(object):
    def __init__(self, name=None, type=None):
        self.typeName = name
        self.type = type

    def toString(self):
        if self.typeName != None:
            return self.typeName
        else:
            #return self.type.toString()
            return self.type

class MethodoInfo(object):
    def __init__(self):
        self.name = None
        self.returnType = None
        self.parameters = []

    def toString(self):
        ret = self.returnType + " " + self.name + "("
        for i in self.parameters:
            ret+= i.toString() + ", "
        tamanho = len(self.parameters)
        if tamanho != 0:
            ret = ret[0, len(ret) -2]
        return ret + ")"

class VariableType():

    def toString(self, name):
        nome = name.upper()
        res = ''
        if nome == 'INT':
            res = 'INT'
        elif nome == 'BOOLEAN':
            res = 'BOOLEAN'
        elif nome == 'INT_ARRAY':
            res = 'INT_ARRAY'
        elif nome == 'USER_DEFINED':
            res = 'USER_DEFINED'
        else:
            res = 'UNKKNOW'
        return res

class Scope(object):

    def __init__(self, parent):
        self.parent = parent
        self.currentClassName = None
        if parent != None:
            self.currentClassName = parent.currentClassName
        self.entries = {}

    def insert(self, toInsert):
        self.entries[toInsert.name] = toInsert


    def lookup(self, name):
        ret = ''
        if name in self.entries:
            ret = self.entries.get(name).type
        else:
            if self.parent == None:
                ret = None
            else:
                ret = self.parent.lookup(name)
        return ret

    def clear(self):
        return self.entries.clear()

    def print(self, ident):
        if self.parent != None:
            self.parent.print(ident)
        valores = self.entries.keys()
        for i in valores:
            print(self.entries.get(i).name +" -> " + self.entries.get(i).type)

class VariableEntry(object):
    def __init__(self, type, name):
        self.name = name
        self.type = type

    #def VariableEntry(self, type, name):
        #self.name = name
        #self.type = type
    def obtemNomeTipo(self):
        return self.type + ":"+self.name

    def toString(self):
        return self.type.toString() + ": " + self.name

class ReturnItem(object):
    def __init__(self, type, register):
        self.type = type
        self.register = register

class Generator(object):

    def __init__(self, prefix):
        self.count = 0
        self.prefix = prefix
        self.toReuse = []

    def next(self):
        num = 0
        if len(self.toReuse) == 0:
            self.cont += 1
        else:
            self.toReuse.remove()
        #return self.prefix + int(self.toString(num))
        return self.prefix + str(num)

    def reset(self, count):
        self.count = count

    def reuse(self, num):
        self.toReuse.append(num)

"""
Primeira Passagem do Visitor
Verificacao de erros:
*- Estende classe nao declarada anteriormente
*- Exclusivadade da variavel global da classe
*- Exclusividade do metodo
*- Exclusividade da classe
"""

class Visitor1(MiniJavaVisitor):

    def __init__(self):
        self.classes = {}

    def retornaClassePronta(self):
        return self.classes


    def print_erro(self, msg, token):
        linha = token.line  # Numero da linha do erro
        coluna = token.column  # Numero da coluna do erro
        print('Linha ' + str(linha) + ':' + str(coluna) + '\t' + 'Erro: ' + msg)

    def erro_generico_detectado(self, msg, ctx):
        # Identificador nao definido
        self.print_erro(msg, ctx)

    # Visit a parse tree produced by MiniJavaParser#goal.
    def visitGoal(self, ctx):
        ctx.mainClass().accept(self)
        for i in ctx.classDeclaration():
            i.accept(self)
        return None


    # Visit a parse tree produced by MiniJavaParser#mainclass.
    def visitMainclass(self, ctx):
        global classe_atual
        global regiao
        name = ctx.Identifier(0).getText()
        classe_atual = name
        main = ClassInfo()
        main.name = name
        main.extendName = None

        regiao += 1
        self.classes[name] = main
        return None


    # Visit a parse tree produced by MiniJavaParser#dec_class.
    def visitDec_class(self, ctx):
        global classe_atual
        global regiao
        className = ctx.Identifier(0).getText()
        classe_atual = className
        classInfo = ClassInfo()
        classInfo.name = className
        classInfo.extendName = None
        try:
            classInfo.extendName = ctx.Identifier(1).getText()
        except:
            pass
        #Checa classe Inexistente
        if className in self.classes:
            self.erro_generico_detectado("Classe " + className +' ja foi declarada anteriormente!',
                                         ctx.Identifier(0).getSymbol())
            sys.exit()
        #Verificar se a classe a qual herda foi declarada
        if classInfo.extendName != None and classInfo.extendName not in self.classes:
            self.erro_generico_detectado("Classe " + classInfo.extendName + ' nao foi declarada anteriormente!',
                                         ctx.Identifier(1).getSymbol())
            sys.exit()

        self.classes[className] = classInfo
        regiao += 1

        for i in ctx.varDeclaration():
            i.accept(self)

        for i in ctx.methodDeclaration():
            i.accept(self)

        return None


    # Visit a parse tree produced by MiniJavaParser#dec_var.
    def visitDec_var(self, ctx):
        #Pega o tipo do campo
        typeName = ctx.mtype().getText()
        type = FieldInfo()
        if typeName == 'INT':
            type.typeName = None
            type.type = VariableType().toString(typeName)
        elif typeName == 'INT[]':
            type.typeName = None
            type.type = VariableType().toString(typeName)
        elif typeName == 'BOOLEAN':
            type.typeName = None
            type.type = VariableType().toString(typeName)
        else:
            type.typeName = typeName
            type.type = VariableType().toString('USER_DEFINED')

        # Checar a exclusividade da variavel
        classInfo = self.classes.get(classe_atual)

        name = ctx.Identifier().getText()
        if name in classInfo.fields:
            self.erro_generico_detectado("Dec_Var: Variavel " + name + ' ja foi declarada anteriormente!',
                                         ctx.Identifier().getSymbol())
            sys.exit()
        classInfo.fields[name] = type
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#dec_method.
    def visitDec_method(self, ctx):
        global classe_atual
        typeName = ctx.mtype(0).getText()
        type = FieldInfo()
        if typeName == 'INT':
            type.typeName = None
            type.type = VariableType().toString(typeName)
        elif typeName == 'INT[]':
            type.typeName = None
            type.type = VariableType().toString(typeName)
        elif typeName == 'BOOLEAN':
            type.typeName = None
            type.type = VariableType().toString(typeName)
        else:
            type.typeName = typeName
            type.type = VariableType().toString('USER_DEFINED')

        newMethod = MethodoInfo()
        newMethod.returnType = type

        #Nome do metodo
        newMethod.name = ctx.Identifier(0).getText()

        #Exclusividade do metodo
        classInfo = self.classes.get(classe_atual)
        if newMethod.name in classInfo.methods:
            self.erro_generico_detectado("Dec_Method: Metodo " + newMethod.name + ' ja foi declarada anteriormente!',
                                         ctx.Identifier(0).getSymbol())
            sys.exit()

        #Obter parametros
        lista_parametros = []
        for i in range(1, len(ctx.mtype())):
            lista_parametros.append(ctx.mtype(i).accept(self))
        if len(lista_parametros) != 0:
            for i in lista_parametros:
                if i.upper() == 'INT':
                    parType = FieldInfo(None, 'INT')
                elif i.upper() == 'BOOLEAN':
                    parType = FieldInfo(None, 'BOOLEAN')
                elif i.upper() == 'INT_ARRAY':
                    parType = FieldInfo(None, 'INT_ARRAY')
                else:
                    parType = FieldInfo(i.upper(), 'USER_DEFINED')
                newMethod.parameters.append(parType)

        #Verifica se metodo substitui o metodo da superclasse
        if classInfo.extendName == '':
            currentClassName = None
        else:
            currentClassName = classInfo.extendName
        while(currentClassName != None):
            currentClass = self.classes.get(currentClassName)
            if newMethod.name in currentClass.methods:
                superMethod = currentClass.methods.get(newMethod.name)
                correctOverride = True
                if newMethod.returnType.type != superMethod.returnType.type or \
                        len(newMethod.parameters) != len(superMethod.parameters):
                    correctOverride = False

                if correctOverride:
                    for i in range(0, len(newMethod.parameters)):
                        if newMethod.parameters[i].type != superMethod.parameters[i].type:
                            correctOverride = False
                if not correctOverride:
                    self.erro_generico_detectado("Override de funcao diferente da super classe",
                                                 ctx.Identifier(0).getSymbol())
                    sys.exit()

            currentClassName = currentClass.extendName
        classInfo.methods[newMethod.name] = newMethod
        return None


    # Visit a parse tree produced by MiniJavaParser#mtype.
    def visitMtype(self, ctx):
        type = ctx.getText().upper()
        return type

    # Visit a parse tree produced by MiniJavaParser#expr_id.
    def visitExpr_id(self, ctx):
        id = ctx.getText()
        return id

    # Visit a parse tree produced by MiniJavaParser#err_miss_RHS.
    def visitErr_miss_RHS(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MiniJavaParser#err_many_lparents.
    def visitErr_many_lparents(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#err_many_rparents.
    def visitErr_many_rparents(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#expr_array.
    def visitExpr_array(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#err_miss_LHS.
    def visitErr_miss_LHS(self, ctx):
        return self.visitChildren(ctx)


class Visitor2(MiniJavaVisitor):

    def __init__(self, classes):
        self.classes = classes
        self.tempParameters = []
        self.scopoGlobal = None
        self.scopoLocal = None

    def print_erro(self, msg, token):
        linha = token.line  # Numero da linha do erro
        coluna = token.column  # Numero da coluna do erro
        print('Linha ' + str(linha) + ':' + str(coluna) + '\t' + 'Erro: ' + msg)

    def erro_generico_detectado(self, msg, ctx):
        # Identificador nao definido
        self.print_erro(msg, ctx)

    #Checa se a class2 eh subclass da class1
    def isCompatible(self, class1, class2):
        if class1.upper() == 'INT[]':
            class1 = 'INT_ARRAY'
        if class2.upper() == 'INT[]':
            class2 = 'INT_ARRAY'
        if class1 == class2:
            return True
        alternativa1 = False
        alternativa2 = False
        valores_classes = self.classes.keys()
        for i in valores_classes:
            if class1 == i.upper():
                alternativa1 = True
            if class2 == i.upper():
                alternativa2 = True
        if not (alternativa1 and alternativa2):
            return False

        nomeClasse = ''
        for i in valores_classes:
            if class2 == i.upper():
                nomeClasse = i
                break
        class2 = self.classes.get(nomeClasse).extendName

        while class2 != None:
            if class1.upper() == class2.upper():
                return True
            for i in valores_classes:
                if class2 == i.upper():
                    nomeClasse = i
                    break
            class2 = self.classes.get(nomeClasse).extendName
        return False

    def lookupField(self, scope, fieldName):
        #Checa o escopo
        ret = scope.lookup(fieldName)
        if ret != None:
            return ret

        #Checa as super classses
        className1 = scope.currentClassName
        className = self.classes.get(className1).extendName
        while className != None:
            superClass = self.classes.get(className)
            if fieldName in superClass.fields:
                return superClass.fields.get(fieldName).toString()

            className = self.classes.get(className).extendName

        return None

    def lookupMethod(self, className, methodName):
        classInfo = self.classes.get(className)

        #Checa a classe
        if methodName in classInfo.methods:
            return classInfo.methods.get(methodName)

        #Checa super classes
        extendName = classInfo.extendName
        while extendName != None:
            classInfo = self.classes.get(extendName)
            if methodName in classInfo.methods:
                return classInfo.methods.get(methodName)
            extendName = classInfo.extendName
        return None

    # Visit a parse tree produced by MiniJavaParser#goal.
    def visitGoal(self, ctx):
        ctx.main_class.accept(self)
        for i in ctx.classDeclaration():
            i.accept(self)
        self.classes.clear()
        #return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#mainclass.
    def visitMainclass(self, ctx):
        global classe_atual
        global regiao
        classe_atual = ctx.Identifier(0).getText()
        self.scopoGlobal = Scope(None)
        self.scopoGlobal.currentClasseName = ctx.Identifier(0).getText()
        ctx.main_class_stmt.accept(self) #Visita os filhos

        self.scopoGlobal.clear()
        return None

    # Visit a parse tree produced by MiniJavaParser#dec_class.
    def visitDec_class(self, ctx):
        global classe_atual
        global regiao
        classe_atual = ctx.Identifier(0).getText()
        self.scopoGlobal = Scope(None)
        self.scopoGlobal.currentClassName = ctx.Identifier(0).getText()

        self.scopoLocal = self.scopoGlobal #Primeira Passada
        # Variaveis
        for i in ctx.varDeclaration():
            i.accept(self)

        regiao = 1

        # Checa os metodos
        for i in ctx.methodDeclaration():
            i.accept(self)
        self.scopoGlobal.clear()
        regiao = 0
        return None


    # Visit a parse tree produced by MiniJavaParser#dec_var.
    def visitDec_var(self, ctx):
        type = ctx.mtype().accept(self)
        if type != 'INT' and type != 'INT[]' and type != 'BOOLEAN' and (not type in self.classes):
            self.erro_generico_detectado("Dec_Var: Classe nao encontrada "+ type, \
                                         ctx.Identifier().getSymbol())
            sys.exit()

        #Variavel desconhecida
        varName = ctx.Identifier().getText()
        scope = self.scopoGlobal
        scope1 = self.scopoLocal

        if regiao == 0:
            if varName in scope.entries:
                self.erro_generico_detectado("Dec-Var: Variavel " + varName +' ja declarada' , \
                                             ctx.Identifier().getSymbol())
                sys.exit()
            scope.insert(VariableEntry(type,varName))
        else:
            if regiao != 0:
                if varName in scope.entries or varName in scope1.entries:
                    self.erro_generico_detectado("Dec-Var: Variavel " + varName +' ja declarada' , \
                                                 ctx.Identifier().getSymbol())
                    sys.exit()
                scope1.insert(VariableEntry(type,varName))
        return None



    # Visit a parse tree produced by MiniJavaParser#dec_method.
    def visitDec_method(self, ctx):
        self.scopoLocal = Scope(self.scopoGlobal)
        method = self.scopoLocal
        retType_bkcp = ctx.mtype(0).getText()
        retType = ctx.mtype(0).getText()
        retType = retType.upper()
        if retType == 'INT[]':
            retType = 'INT_ARRAY'
        if retType != 'INT' and retType != 'INT_ARRAY' and retType != 'BOOLEAN' and (not retType_bkcp in self.classes):
            lista = ctx.children
            self.erro_generico_detectado("DecMethod: Classe "+retType+" nao encontrada ", \
                                         lista[0].getSymbol())
            sys.exit()
        #Pega e checa parametros
        scope = self.scopoLocal
        for i in range(1, len(ctx.mtype())):
            type = ctx.mtype(i).accept(self)
            name = ctx.Identifier(i).getText()
            scope.insert(VariableEntry(type, name))


        # Checa declaracao de variaveis
        for i in ctx.varDeclaration():
            i.accept(self)

        #Checa os comandos
        for i in ctx.statement():
            i.accept(self)

        # Checa retorno do tipo
        if not self.isCompatible(retType, ctx.exp_retorno.accept(self).upper()):
            self.erro_generico_detectado("Dec_Method: Metodo deve retornar o tipo "+retType, \
                                         ctx.Identifier(0).getSymbol())
            sys.exit()
        method.clear()
        return None


    # Visit a parse tree produced by MiniJavaParser#mtype.
    def visitMtype(self, ctx):
        type_back = ctx.getText()
        type = ctx.getText().upper()
        if type != 'INT' and type != 'INT[]' and type != 'BOOLEAN' and (not type_back in self.classes):
            lista = ctx.children
            self.erro_generico_detectado("MType1:Classe nao encontrada " + type, \
                                         lista[0].getSymbol())
            sys.exit()

        if type == 'INT' or type == 'INT[]' or  type == 'BOOLEAN':
            return type
        else:
            return type_back


    # Visit a parse tree produced by MiniJavaParser#state_lrparents.
    def visitState_lrparents(self, ctx):
        for i in ctx.statement():
            i.accept(self)
        return None


    # Visit a parse tree produced by MiniJavaParser#state_if.
    def visitState_if(self, ctx):
        # Checa a condicao do tipo
        res = ctx.expression().accept(self).upper()
        if res != 'BOOLEAN':
            lista = ctx.children
            self.erro_generico_detectado("State_IF: Funcao do IF deve ser do tipo BOOLEAN", \
                                         lista[0].getSymbol())
            sys.exit()
        for i in ctx.statement():
            i.accept(self)
        return None


    # Visit a parse tree produced by MiniJavaParser#state_while.
    def visitState_while(self, ctx):
        # Checa a condicao do tipo
        res = ctx.expression().accept(self).upper()
        if res != 'BOOLEAN':
            lista = ctx.children
            self.erro_generico_detectado("State_while: Funcao do While deve ser do tipo BOOLEAN", \
                                         lista[0].getSymbol())
            sys.exit()
        ctx.statement().accept(self)
        return None


    # Visit a parse tree produced by MiniJavaParser#state_print.
    def visitState_print(self, ctx):
        argType = ctx.expression().accept(self)
        argType = argType.upper()
        if argType != 'INT' and argType != 'BOOLEAN':
            lista = ctx.children
            self.erro_generico_detectado("State_print: Funcao print so aceita INT ou BOOLEAN", \
                                        lista[0].getSymbol())
            sys.exit()
        ctx.expression().accept(self)
        return None


    # Visit a parse tree produced by MiniJavaParser#state_assign.
    def visitState_assign(self, ctx):
        # Lado esquerdo: tipo
        scope = self.scopoLocal
        varName = ctx.Identifier().getText()
        ltype = self.lookupField(scope, varName)
        if ltype == None:
            self.erro_generico_detectado("State_Assign: Variavel " + varName + ' nao foi declarada antes do uso!', \
                                         ctx.Identifier().getSymbol())
            sys.exit()
        # Lado direito: tipo
        rtype = ctx.expression().accept(self)

        #Checa os tipos
        if not self.isCompatible(ltype.upper(), rtype.upper()):
            self.erro_generico_detectado("State_Assign: Variavel " + varName + ' tipos incompativeis!', \
                                         ctx.Identifier().getSymbol())
            sys.exit()


        return None


    # Visit a parse tree produced by MiniJavaParser#state_array_assign.
    def visitState_array_assign(self, ctx):
        # Checa tipo do indice
        res = ctx.expression(0).accept(self)
        if res != 'INT':
            self.erro_generico_detectado("State_Array_Assign: O indice deve sempre ser do tipo INT", \
                                         ctx.Identifier().getSymbol())
            sys.exit()

        #Checa o tipo do array
        arrayID = ctx.Identifier().getText()
        scopo = self.scopoLocal
        if self.lookupField(scopo, arrayID) == None:
            self.erro_generico_detectado("State_Array_Assign: Variavel "+arrayID+" nao foi declarada", \
                                         ctx.Identifier().getSymbol())
            sys.exit()

        tipo = self.lookupField(scopo, arrayID)
        if tipo.upper() == 'INT[]':
            tipo = 'INT_ARRAY'

        if tipo != 'INT_ARRAY':
            self.erro_generico_detectado("State_Array_Assign: Array com id " + arrayID + " diferente de INT_ARRAY", \
                                         ctx.Identifier().getSymbol())
            sys.exit()

        #Checa tipo da expressao esquerda
        rest1 = ctx.expression(1).accept(self)
        if rest1 != 'INT':
            self.erro_generico_detectado("State_ArraYy_Assign: Arrays pode somente valores do tipo INT", \
                                         ctx.Identifier().getSymbol())
            sys.exit()

        return None


    # Visit a parse tree produced by MiniJavaParser#expr_op_and.
    def visitExpr_op_and(self, ctx):
        ltype = ctx.expression(0).accept(self).upper()
        rtype = ctx.expression(1).accept(self).upper()
        if ltype != 'BOOLEAN' or rtype != 'BOOLEAN':
            lista = ctx.children
            self.erro_generico_detectado("Expr_op_and: Ambos os lados da expressao && devem ser do tipo BOOLEAN", \
                                         lista[1].getSymbol())
            sys.exit()
        return "BOOLEAN"

    # Visit a parse tree produced by MiniJavaParser#expr_op_less.
    def visitExpr_op_less(self, ctx):
        ltype = ctx.expression(0).accept(self).upper()
        rtype = ctx.expression(1).accept(self).upper()
        if ltype != 'INT' or rtype != 'INT':
            lista = ctx.children

            self.erro_generico_detectado("Ambos os lados da expressao < devem ser do tipo INT", \
                                         lista[1].getSymbol())
            sys.exit()
        return "BOOLEAN"

    # Visit a parse tree produced by MiniJavaParser#expr_op_plus.
    def visitExpr_op_plus(self, ctx):
        ltype = ctx.expression(0).accept(self).upper()
        rtype = ctx.expression(1).accept(self).upper()
        if ltype != 'INT' or rtype != 'INT':
            lista = ctx.children
            self.erro_generico_detectado("Ambos os lados da expressao + devem ser do tipo INT", \
                                         lista[1].getSymbol())
            sys.exit()
        return "INT"

    # Visit a parse tree produced by MiniJavaParser#expr_op_minus.
    def visitExpr_op_minus(self, ctx):
        ltype = ctx.expression(0).accept(self).upper()
        rtype = ctx.expression(1).accept(self).upper()
        if ltype != 'INT' or rtype != 'INT':
            lista = ctx.children
            self.erro_generico_detectado("Ambos os lados da expressao - devem ser do tipo INT", \
                                         lista[1].getSymbol())
            sys.exit()
        return "INT"

    # Visit a parse tree produced by MiniJavaParser#expr_op_multi.
    def visitExpr_op_multi(self, ctx):
        ltype = ctx.expression(0).accept(self).upper()
        rtype = ctx.expression(1).accept(self).upper()
        if ltype != 'INT' or rtype != 'INT':
            lista = ctx.children
            self.erro_generico_detectado("Ambos os lados da expressao * devem ser do tipo INT", \
                                         lista[1].getSymbol())
            sys.exit()
        return "INT"

    # Visit a parse tree produced by MiniJavaParser#expr_array.
    def visitExpr_array(self, ctx):
        arrayType = ctx.expression(0).accept(self)
        if arrayType.upper() == 'INT[]':
            arrayType = 'INT_ARRAY'

        if arrayType != 'INT_ARRAY':
            lista = ctx.children
            self.erro_generico_detectado("Expr_array: Matrizes so podem conter valores do tipo INT", \
                                         lista[1].getSymbol())
            sys.exit()
        indexType = ctx.expression(1).accept(self)
        if indexType != 'INT':
            lista = ctx.children
            self.erro_generico_detectado("Expr_array: Indice do array so pode ser do tipo INT", \
                                         lista[1].getSymbol())
            sys.exit()

        return "INT"

    # Visit a parse tree produced by MiniJavaParser#expr_length.
    def visitExpr_length(self, ctx):
        arrayType = ctx.expression().accept(self).upper()
        if arrayType == 'INT[]':
            arrayType = 'INT_ARRAY'
        if arrayType != 'INT_ARRAY':
            lista = ctx.children
            self.erro_generico_detectado("Expressao nao eh do tipo INT_ARRAY", \
                                         lista[1].getSymbol())
            sys.exit()
        return "INT"


    # Visit a parse tree produced by MiniJavaParser#expr_method_calling.
    def visitExpr_method_calling(self, ctx):
        #Checar a clasee
        global classe_atual
        scope = self.scopoLocal
        className = ctx.expression(0).accept(self)
        if not className in self.classes:
            className = self.lookupField(scope, className)
        if className == None or (not className in self.classes):
            self.erro_generico_detectado("Expr_method_calling: Chamada para uma classe inexistente!!", \
                                         ctx.Identifier().getSymbol())
            sys.exit()

        #Checa o metodo
        method = ctx.Identifier().getText()
        methodInfo = self.lookupMethod(className, method)
        if methodInfo == None:
            self.erro_generico_detectado("Expr_method_calling: Class "+className+" nao possui o metodo da chamada", \
                                         ctx.Identifier().getSymbol())

        #Checa os parametros
        for i in range(1, len(ctx.expression())):
            self.tempParameters.append(ctx.expression(i).accept(self))

        # Verificacao cruzada
        parameterAgree = True
        if len(methodInfo.parameters) != len(self.tempParameters):
            parameterAgree = False


        for i in range(0, len(self.tempParameters)):
            if not self.isCompatible(methodInfo.parameters[i].toString(), self.tempParameters[i].upper()):
                parameterAgree = False

        if not parameterAgree:
            self.erro_generico_detectado(
                "Expr_method_calling: Metodo " + className + "." + method + ' esta com chamada de argumentos erradas', \
                ctx.Identifier().getSymbol())
            sys.exit()

        self.tempParameters.clear()

        return methodInfo.returnType.toString()


    # Visit a parse tree produced by MiniJavaParser#expr_bool.
    def visitExpr_bool(self, ctx):
        return "BOOLEAN"

    # Visit a parse tree produced by MiniJavaParser#expr_int.
    def visitExpr_int(self, ctx):
        return "INT"


    # Visit a parse tree produced by MiniJavaParser#expr_int_array.
    def visitExpr_int_array(self, ctx):
        indexType = ctx.expression().accept(self)
        if indexType != 'INT':
            self.erro_generico_detectado("Expr_int_array: O tamanho do Array deve ser expressao do tipo INT", ctx.Identifier().getSymbol())
            sys.exit()
        return "INT_ARRAY"


    # Visit a parse tree produced by MiniJavaParser#expr_new_array.
    def visitExpr_new_array(self, ctx):
        className = ctx.Identifier().getText()
        if not className in self.classes:
            self.erro_generico_detectado("Expr_new_array: Tentando instanciar um objeto de classe inexistente",
                                         ctx.Identifier().getSymbol())
            sys.exit()
        return className



    # Visit a parse tree produced by MiniJavaParser#expr_not.
    def visitExpr_not(self, ctx):
        return ctx.expression().accept(self)


    # Visit a parse tree produced by MiniJavaParser#expr_id.
    def visitExpr_id(self, ctx):
        var = ctx.Identifier().getText()
        scope = self.scopoLocal
        type = self.lookupField(scope, var)

        if type == None:
            self.erro_generico_detectado("Expressao Identificador : Variavel "+ var + " nao declarada!",
                                         ctx.Identifier().getSymbol())
            sys.exit()
        var = type
        return var

    # Visit a parse tree produced by MiniJavaParser#expr_this.
    def visitExpr_this(self, ctx):
        scopo = self.scopoLocal
        return scopo.currentClassName

    # Visit a parse tree produced by MiniJavaParser#expr_this.
    def visitExpr_lrparents(self, ctx):
        return ctx.expression().accept(self)

class Visitor3(MiniJavaVisitor):

    # Construtor
    def __init__(self, classes):
        self.classes = classes
        for i in self.classes:
            i.initParent(classes)
        self.tempParameters = []
        self.argumentRegisters = []

        self.finalSpigletCode = ''
        self.labels = Generator("L")
        self.registers = Generator("TEMP")

        self.adressRegister = None
        self.argumentCounter = None
        self.justID = None
        self.excludeFields = None

        self.scopoGlobal = None
        self.scopoLocal = None


    def emit(self, toEmit):
        self.finalSpigletCode += toEmit + '\n'
        #print(toEmit)

    def lookupField(self, scope, fieldName):
        #Checa o escopo
        ret = scope.lookup(fieldName)
        if ret != None:
            return ret

        #Checa as super classses
        className1 = scope.currentClassName
        className = self.classes.get(className1).extendName
        while className != None:
            superClass = self.classes.get(className)
            if fieldName in superClass.fields:
                return superClass.fields.get(fieldName).toString()

            className = self.classes.get(className).extendName

        return None

    def lookupMethod(self, className, methodName):
        classInfo = self.classes.get(className)

        #Checa a classe
        if methodName in classInfo.methods:
            return classInfo.methods.get(methodName)

        #Checa super classes
        extendName = classInfo.extendName
        while extendName != None:
            classInfo = self.classes.get(extendName)
            if methodName in classInfo.methods:
                return classInfo.methods.get(methodName)
            extendName = classInfo.extendName
        return None

    def construcGlobalVTables(self):

        for entry in self.classes:
            clazz = entry.getValue()
            methods = clazz.getMethods()
            #Cria vTable label
            vTableLabel = clazz.name + "_vTable"
            labelRegister = self.registers.next()
            self.emit("\t\tMOVE "+ labelRegister +" "+ vTableLabel)
            #Obtem tamanho de vTable
            vTableSize = len(methods) * 4 #4bytes por endereco
            methodCodeRegister = self.registers.next()
            #Aloca vTable
            self.emit("\t\tMove "+ methodCodeRegister + " HALLOCATE "+ vTableSize)
            self.emit("\t\tHSTORE "+labelRegister+" 0 "+methodCodeRegister)
            # Store method code in vTable
            offset = 0
            methodReg = self.registers.next()
            for method in methods:
                self.emit("\t\tMOVE "+methodReg+" "+method)
                self.emit("\t\tHSTORE "+methodCodeRegister+" "+offset+" "+methodReg)
                offset +=4

    # Visit a parse tree produced by MiniJavaParser#goal.
    def visitGoal(self, ctx):
        ctx.mainClass().accept(self)
        for i in ctx.classDeclaration():
            i.accept(self)
            print(dir(i))
        #self.classes.clear()
        return None


    # Visit a parse tree produced by MiniJavaParser#mainclass.
    def visitMainclass(self, ctx):
        global classe_atual
        global regiao
        self.emit("MAIN")
        classe_atual = ctx.Identifier(0).getText()
        self.scopoGlobal = Scope(None)
        self.justID = True
        ret = ctx.Identifier(0).getText()
        self.scopoGlobal.currentClasseName = ctx.Identifier(0).getText()
        self.justID = False

        #Verifica o statement
        ctx.statement().accept(self)

        self.scopoGlobal.clear()
        self.emit("END")
        return None




    # Visit a parse tree produced by MiniJavaParser#dec_class.
    def visitDec_class(self, ctx):
        global classe_atual
        global regiao
        main = Scope(None)
        self.justID = True
        ret = ctx.Identifier(0).accept(self)
        main.currentClassName = ret.type
        self.justID = False

        #Checa declaracao de variaveis
        for i in ctx.varDeclaration():
            i.accept(self)

        #Checa os cmd
        for i in ctx.

        #Obtem
        return None

    '''
    # Visit a parse tree produced by MiniJavaParser#dec_var.
    def visitDec_var(self, ctx:MiniJavaParser.Dec_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#dec_method.
    def visitDec_method(self, ctx:MiniJavaParser.Dec_methodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#mtype.
    def visitMtype(self, ctx:MiniJavaParser.MtypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#state_lrparents.
    def visitState_lrparents(self, ctx:MiniJavaParser.State_lrparentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#state_if.
    def visitState_if(self, ctx:MiniJavaParser.State_ifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#state_while.
    def visitState_while(self, ctx:MiniJavaParser.State_whileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#state_print.
    def visitState_print(self, ctx:MiniJavaParser.State_printContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#state_assign.
    def visitState_assign(self, ctx:MiniJavaParser.State_assignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#state_array_assign.
    def visitState_array_assign(self, ctx:MiniJavaParser.State_array_assignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#err_miss_RHS.
    def visitErr_miss_RHS(self, ctx:MiniJavaParser.Err_miss_RHSContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#expr_this.
    def visitExpr_this(self, ctx:MiniJavaParser.Expr_thisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#err_many_lparents.
    def visitErr_many_lparents(self, ctx:MiniJavaParser.Err_many_lparentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#expr_op_multi.
    def visitExpr_op_multi(self, ctx:MiniJavaParser.Expr_op_multiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#expr_bool.
    def visitExpr_bool(self, ctx:MiniJavaParser.Expr_boolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#expr_length.
    def visitExpr_length(self, ctx:MiniJavaParser.Expr_lengthContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#expr_op_and.
    def visitExpr_op_and(self, ctx:MiniJavaParser.Expr_op_andContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#expr_lrparents.
    def visitExpr_lrparents(self, ctx:MiniJavaParser.Expr_lrparentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#err_many_rparents.
    def visitErr_many_rparents(self, ctx:MiniJavaParser.Err_many_rparentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#expr_array.
    def visitExpr_array(self, ctx:MiniJavaParser.Expr_arrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#expr_int.
    def visitExpr_int(self, ctx:MiniJavaParser.Expr_intContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#expr_int_array.
    def visitExpr_int_array(self, ctx:MiniJavaParser.Expr_int_arrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#expr_op_minus.
    def visitExpr_op_minus(self, ctx:MiniJavaParser.Expr_op_minusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#expr_op_plus.
    def visitExpr_op_plus(self, ctx:MiniJavaParser.Expr_op_plusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#expr_new_array.
    def visitExpr_new_array(self, ctx:MiniJavaParser.Expr_new_arrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#expr_op_less.
    def visitExpr_op_less(self, ctx:MiniJavaParser.Expr_op_lessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#err_miss_LHS.
    def visitErr_miss_LHS(self, ctx:MiniJavaParser.Err_miss_LHSContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#expr_method_calling.
    def visitExpr_method_calling(self, ctx:MiniJavaParser.Expr_method_callingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#expr_not.
    def visitExpr_not(self, ctx:MiniJavaParser.Expr_notContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#expr_id.
    def visitExpr_id(self, ctx:MiniJavaParser.Expr_idContext):
        return self.visitChildren(ctx)
    '''

