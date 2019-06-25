import os, sys, re
from antlr4 import *
from antlr4.error import ErrorListener
import argparse

if __name__ is not None and "." in __name__:
	from .MiniJavaVisitor import MiniJavaVisitor
	from .MiniJavaListener import MiniJavaListener
    #from .TabelaDeSimbolos import *
else:
    from MiniJavaVisitor import MiniJavaVisitor
    from MiniJavaListener import MiniJavaListener
    from TabelaDeSimbolos import *

############Novo###################
###################################
##################################

classe_atual = ''


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
    def __init__(self):
        self.typeName = None
        self.type = None

    def toString(self):
        if self.typeName != None:
            return self.typeName
        else:
            return self.type.toString()

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
        if name is self.entries:
            ret = self.entries.get(name).type
        else:
            ret = None

        if ret == None:
            return ret
        else:
            if self.parent == None:
                return None
            else:
                return self.parent.lookup(name)

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

    def toString(self):
        return self.type.toString() + ": " + self.name

"""
Primeira Passagem do Visitor
Verificacao de erros:
*- Estende classe nao declarada anteriormente
*- Exclusivadade da variavel
*- Exclusividade do metodo
*- Exclusividade da classe
"""

class Visitor1(MiniJavaVisitor):

    def __init__(self):
        self.classes = {}

    def print_erro(self, msg, token):
        linha = token.line  # Numero da linha do erro
        coluna = token.column  # Numero da coluna do erro
        print('Linha ' + str(linha) + ':' + str(coluna) + '\t' + 'Erro: ' + msg)

    def erro_generico_detectado(self, msg, ctx):
        # Identificador nao definido
        self.print_erro(msg, ctx)

    # Visit a parse tree produced by MiniJavaParser#goal.
    def visitGoal(self, ctx):

        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#mainclass.
    def visitMainclass(self, ctx):
        global classe_atual
        name = ctx.Identifier(0).getText()
        classe_atual = name
        main = ClassInfo()
        main.name = name
        main.extendName = None
        self.classes[name] = main
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#dec_class.
    def visitDec_class(self, ctx):
        global classe_atual
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
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#dec_var.
    def visitDec_var(self, ctx):
        #Pega o tipo do campo
        typeName = ctx.mtype().getText()
        type = FieldInfo()
        if typeName == 'int':
            type.typeName = None
            type.type = VariableType().toString(typeName)
        elif typeName == 'int[]':
            type.typeName = None
            type.type = VariableType().toString(typeName)
        elif typeName == 'boolean':
            type.typeName = None
            type.type = VariableType().toString(typeName)
        else:
            type.typeName = typeName
            type.type = VariableType().toString('USER_DEFINED')

        # Checar a exclusividade da variavel
        classInfo = self.classes.get(classe_atual)

        name = ctx.Identifier().getText()
        if name in classInfo.fields:
            self.erro_generico_detectado("Variavel " + name + ' ja foi declarada anteriormente!',
                                         ctx.Identifier().getSymbol())
            sys.exit()
        classInfo.fields[name] = type
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#dec_method.
    def visitDec_method(self, ctx):
        global classe_atual
        typeName = ctx.mtype(0).getText()
        type = FieldInfo()
        if typeName == 'int':
            type.typeName = None
            type.type = VariableType().toString(typeName)
        elif typeName == 'int[]':
            type.typeName = None
            type.type = VariableType().toString(typeName)
        elif typeName == 'boolean':
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
            self.erro_generico_detectado("Metodo " + newMethod.name + ' ja foi declarada anteriormente!',
                                         ctx.Identifier(0).getSymbol())
            sys.exit()

        #Obter parametros
        parametros = []
        try:
            # Possui um parametro, pelo menos
            parametros.append(ctx.tipoP1.getText())
        except:
            pass
        listaTipos = ctx.listaTipoPs
        try:
            for i in range(0, len(listaTipos)):
                parametros.append(listaTipos[i].getText())
        except:
            pass
        #Se a lista de parametros nao for vazia
        if len(parametros) != 0:
            for i in parametros:
                parType = FieldInfo()
                if i == 'int':
                    parType.typeName = None
                    parType.type = VariableType().toString(i)
                elif i == 'int[]':
                    parType.typeName = None
                    parType.type = VariableType().toString(i)
                elif i == 'boolean':
                    parType.typeName = None
                    parType.type = VariableType().toString(i)
                else:
                    parType.typeName = typeName
                    parType.type = VariableType().toString('USER_DEFINED')
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
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#mtype.
    def visitMtype(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#state_lrparents.
    def visitState_lrparents(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#state_if.
    def visitState_if(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#state_while.
    def visitState_while(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#state_print.
    def visitState_print(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#state_assign.
    def visitState_assign(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#state_array_assign.
    def visitState_array_assign(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#err_miss_RHS.
    def visitErr_miss_RHS(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#expr_this.
    def visitExpr_this(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#err_many_lparents.
    def visitErr_many_lparents(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#expr_op_multi.
    def visitExpr_op_multi(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#expr_bool.
    def visitExpr_bool(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#expr_length.
    def visitExpr_length(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#expr_op_and.
    def visitExpr_op_and(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#expr_lrparents.
    def visitExpr_lrparents(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#err_many_rparents.
    def visitErr_many_rparents(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#expr_array.
    def visitExpr_array(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#expr_int.
    def visitExpr_int(self, ctx):
        #print(ctx.getText())
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#expr_int_array.
    def visitExpr_int_array(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#expr_op_minus.
    def visitExpr_op_minus(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#expr_op_plus.
    def visitExpr_op_plus(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#expr_new_array.
    def visitExpr_new_array(self, ctx):
        #print(ctx.Identifier())
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#expr_op_less.
    def visitExpr_op_less(self, ctx):
        #print(ctx.exp3.getText(), '<', ctx.exp4.getText())
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#err_miss_LHS.
    def visitErr_miss_LHS(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#expr_method_calling.
    def visitExpr_method_calling(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#expr_not.
    def visitExpr_not(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#expr_id.
    def visitExpr_id(self, ctx):
        #print(ctx.Identifier())
        return self.visitChildren(ctx)



class Visitor2(MiniJavaVisitor):

    def __init__(self, classes):
        self.classes = classes
        self.escopos = {}
        self.tempParameters = []

    def print_erro(self, msg, token):
        linha = token.line  # Numero da linha do erro
        coluna = token.column  # Numero da coluna do erro
        print('Linha ' + str(linha) + ':' + str(coluna) + '\t' + 'Erro: ' + msg)

    def erro_generico_detectado(self, msg, ctx):
        # Identificador nao definido
        self.print_erro(msg, ctx)

    #Checa se a class2 eh subclass da class1
    def isCompatible(self, class1, class2):
        if class1 == class2:
            return True
        if not (class1 in self.classes and class2 in self.classes):
            return False
        class2 = self.classes.get(class2).extendName
        while class2 != None:
            if class1 == class2:
                return True
            class2 = self.classes.get(class2).extendName
        return False

    def lookupField(self, scope, fieldName):
        #Checa o escopo
        ret = scope.lookup(fieldName)
        if ret != None:
            return ret

        #Checa as super classses
        className1 = scope.currentClassName

        print(self.classes)
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
        self.classes.clear()
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#mainclass.
    def visitMainclass(self, ctx):
        global classe_atual
        classe_atual = ctx.Identifier(0).getText()
        main = Scope(None)
        main.currentClasseName = ctx.Identifier(0).getText()
        self.escopos[classe_atual] = main
        main.clear()
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#dec_class.
    def visitDec_class(self, ctx):
        global classe_atual
        classe_atual = ctx.Identifier(0).getText()
        scope = Scope(None)
        scope.currentClassName = ctx.Identifier(0).getText()
        self.escopos[classe_atual] = scope
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#dec_var.
    def visitDec_var(self, ctx):
        type = ctx.mtype().getText()
        if type != 'int' and type != 'int[]' and type != 'boolean' and (not type in self.classes):
            self.erro_generico_detectado("Classe nao encontrada "+ type, \
                                         ctx.Identifier().getSymbol())
            sys.exit()

        #Variavel desconhecida
        varName = ctx.Identifier().getText()
        scope = self.escopos.get(classe_atual)
        if varName in scope.entries:
            self.erro_generico_detectado("Variavel" + varName +' ja declarada' , \
                                         ctx.Identifier(0).getSymbol())
            sys.exit()

        scope.insert(VariableEntry(varName, scope))
        return self.visitChildren(ctx)



    # Visit a parse tree produced by MiniJavaParser#dec_method.
    def visitDec_method(self, ctx):
        return self.visitChildren(ctx)
        #return None


    # Visit a parse tree produced by MiniJavaParser#mtype.
    def visitMtype(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#state_lrparents.
    def visitState_lrparents(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#state_if.
    def visitState_if(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#state_while.
    def visitState_while(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#state_print.
    def visitState_print(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#state_assign.
    def visitState_assign(self, ctx):
        scope = self.escopos.get(classe_atual)
        varName = ctx.Identifier().getText()
        ltype = self.lookupField(scope, varName)

        if ltype == None:
            self.erro_generico_detectado("Variavel" + varName + ' nao foi declarada antes do uso!', \
                                         ctx.Identifier(0).getSymbol())
            sys.exit()
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#state_array_assign.
    def visitState_array_assign(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#err_miss_RHS.
    def visitErr_miss_RHS(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#expr_this.
    def visitExpr_this(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#err_many_lparents.
    def visitErr_many_lparents(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#expr_op_multi.
    def visitExpr_op_multi(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#expr_bool.
    def visitExpr_bool(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#expr_length.
    def visitExpr_length(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#expr_op_and.
    def visitExpr_op_and(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#expr_lrparents.
    def visitExpr_lrparents(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#err_many_rparents.
    def visitErr_many_rparents(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#expr_array.
    def visitExpr_array(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#expr_int.
    def visitExpr_int(self, ctx):
        #print(ctx.getText())
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#expr_int_array.
    def visitExpr_int_array(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#expr_op_minus.
    def visitExpr_op_minus(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#expr_op_plus.
    def visitExpr_op_plus(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#expr_new_array.
    def visitExpr_new_array(self, ctx):
        #print(ctx.Identifier())
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#expr_op_less.
    def visitExpr_op_less(self, ctx):
        #print(ctx.exp3.getText(), '<', ctx.exp4.getText())
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#err_miss_LHS.
    def visitErr_miss_LHS(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#expr_method_calling.
    def visitExpr_method_calling(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#expr_not.
    def visitExpr_not(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#expr_id.
    def visitExpr_id(self, ctx):
        #print(ctx.Identifier())
        return self.visitChildren(ctx)




