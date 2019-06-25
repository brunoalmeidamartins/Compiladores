# -*- coding: utf-8 -*-

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


#ctx: Contexto

tabela = []

tabela_classe = TabelaDeClasses()

tabela_variaveis = TabelaDeVariaveis()

tabela_Chamada_Funcao = TabelaDeChamadaFuncao()

numero_regiao = 0

classe_atual = ''

methodo_atual = ''

matrix_parametros = []


class Regiao_Identificador(object):
    '''
    Usa um dicionario para guardar o identificadores e seus valores em uma regiao
    '''
    def __init__(self):
        self.num_regiao = numero_regiao
        self.identificadores = {} #dict
    def push(self, identificador, valor, regiao):
        try:
            self.identificadores[identificador] = valor
            self.num_regiao = regiao
        except:
            print("Erro ao adicionar o identificador")
    def pop(self, identificador):
        try:
            self.identificadores.pop(identificador)
        except:
            print("Erro ao remover identificador")
    def checar(self, identificador):
        try:
            res = self.identificadores[identificador] # true ou false
        except:
            res = False
        return res
    def pegarNumeroRegiao(self):
        return self.num_regiao
class pilha_regiao_identificadores(object):
    ''' 
    Usando uma pilha para armazenar as regioes validas de um identificador
    '''
    def __init__(self):
        self.num_regiao = 0
        self._identificadores = {} # Valores atuias dos identificadores e seus valores
        self._stack = [] # Os itens da pilha sao regioes com os seus identificadores
        self._history_list = [] #Historico de regioes

    def imprime_pilha(self):
        for regiao in self._stack:
            print([valor for valor in regiao.identificadores ])

    def checar(self, identificador):
        res = None
        for regiao in self._stack:
            try:
                res = regiao.identificadores[identificador]
            except:
                continue
        if res == None:
            return False
        else:
            return res

    def add_novo(self):
        #Adiciona uma nova regiao vazia, nao um novo identificador
        global numero_regiao
        r = Regiao_Identificador()
        self._stack.append(r)
        self._history_list.append(r)
        self.num_regiao = numero_regiao
        numero_regiao += 1
        return r

    def get_top(self):
        return self._stack[-1] #Retorna a pilha original para ser modificada

    def pop_last(self):
        ultimo = self._stack.pop()
        self._history_list.append('POP')
        return ultimo

# Implementacao do Visitor
# Usado para preencher as tabelas de simbolos e tambem analisar alguns erros iniciais
# Exemplo: Verificar se uma variavel foi declarada antes do uso!!
class Meu_Visitor(MiniJavaVisitor):

    def __init__(self):
        self.regioes = pilha_regiao_identificadores()
        self.funcoes = []

    def print_erro(self, msg, token):
        linha = token.line # Numero da linha do erro
        coluna = token.column # Numero da coluna do erro
        print('Linha '+ str(linha) + ':' + str(coluna) + '\t' + 'Erro: ' + msg )

    def erro_id_nao_detectado(self, msg, ctx):
        #Identificador nao definido
        self.print_erro(msg, ctx)

    def erro_id_multi_definido(self, msg, ctx):
        # Identificador Multi definifo
        self.print_erro(msg, ctx)

    def checar(self, identificador):
        return self.regioes.checar(identificador)

    def visitGoal(self, ctx):
        # Comeco, aloca uma nova regiao
        self.regioes.add_novo() #Aloca uma nova regiao
        res = self.visitChildren(ctx)
        self.regioes.pop_last() # Recupera a regiao alocada
        return res

    def visitMainclass(self, ctx):
        '''
        Uma nova classe MAIN. Verifica se foi definida e coloca na regiao atual
        Comeca uma nova regiao
        '''
        regiao_atual = self.regioes.get_top()

        nome_classe = ctx.Identifier(0).getText()
        if not self.checar(nome_classe):
            #Verifica se a MAINCLASS nao foi definida em uma regiao
            global numero_regiao
            regiao_atual.push(nome_classe, 'main_class', numero_regiao)
        else:
            self.erro_id_multi_definido("Multiplas Mainclass Declaradas: " + nome_classe, ctx.Identifier(0).getSymbol())

        #Inicia uma nova regiao
        self.regioes.add_novo() #Adiciona uma nova regiao
        res = self.visitChildren(ctx)
        self.regioes.pop_last() # Recupera a regiao alocada
        return res

    def visitDec_class(self, ctx):
        '''
        Uma nova Class. Verifica se foi definida e coloca na regiao atual
        Comeca uma nova regiao
        '''
        global numero_regiao
        global classe_atual
        global methodo_atual
        methodo_atual = ''

        regiao_atual = self.regioes.get_top()
        nome_classe = ctx.Identifier(0).getText()
        classe_atual = nome_classe
        if not self.checar(nome_classe):
            # Coloca na regiao atual
            regiao_atual.push(nome_classe, 'Classe Declarada', numero_regiao)
        else:
            self.erro_id_multi_definido("Multiplas Classes Declaradas: " + nome_classe, ctx.Identifier(0).getSymbol())

        #comeca uma nova regiao
        self.regioes.add_novo() # Adiciona uma nova regiao
        res = self.visitChildren(ctx)
        self.regioes.pop_last() # Recupera a regiao alocada

        global tabela_classe
        tabela_classe.inserirClasse(nome_classe)
        if str(ctx.Identifier(1)) != 'None':
            extendQuem = str(ctx.Identifier(1))
            tabela_classe.inserirClasse(nome_classe, extendQuem)
        else:
            tabela_classe.inserirClasse(nome_classe)


        return res

    def visitDec_var(self, ctx):
        '''
        Verifica se uma nova variavel declarada foi declarada multiplas vezes
        '''
        regiao_atual = self.regioes.get_top()
        var_name = ctx.Identifier().getText()
        var_type = ctx.mtype().getText()
        global tabela_variaveis
        global numero_regiao
        global classe_atual
        global methodo_atual
        #print(regiao_atual.pegarNumeroRegiao())
        #print(regiao_atual.pegaNumeroRegiao())
        tabela_variaveis.adicionar(var_name, var_type, '0', numero_regiao, classe_atual, methodo_atual)

        if not self.checar(var_name):
            # Coloca na regiao atual
            #global numero_regiao
            regiao_atual.push(var_name, var_type, numero_regiao)
        else:
            self.erro_id_multi_definido("Multiplas Variaveis declaradas: " + var_name, ctx.Identifier().getSymbol())
        return self.visitChildren(ctx)

    def visitDec_method(self, ctx):
        '''
        Verifica se o nome do metodo foi definido
        Comeca uma nova regiao
        '''
        global numero_regiao
        global methodo_atual

        regiao_atual = self.regioes.get_top()
        nome_metodo = ctx.Identifier(0).getText()
        tipo_metodo = ctx.mtype(0).getText()
        methodo_atual = nome_metodo
        if not self.checar(nome_metodo):
            regiao_atual.push(nome_metodo, tipo_metodo, numero_regiao)
        else:
            self.erro_id_multi_definido("Multiplos metodos declarados: " + nome_metodo, ctx.Identifier(0).getSymbol())

        global tabela_classe
        nome_classe = str(ctx.parentCtx.Identifier(0))
        tabela_classe.inserirMetodos(nome_classe,nome_metodo, tipo_metodo)


        nova_regiao = self.regioes.add_novo() # Nova regiao pra o metodo
        # Nao pode obter o numero exato de parametros, verifique os 20 parametros anteriores
        try:
            for i in range(1,20):
                # mtype(0) eh o nome do metodo
                parametro = ctx.Identifier(i)
                nome_parametro = ctx.Identifier(i).getText()
                tipo_parametro = ctx.mtype(i).getText()
                #Adiciona os parametros na tabela_classe
                tabela_classe.inserirParametros(nome_classe, nome_metodo, tipo_parametro)

                #Verfica se tem dois parametros iguais
                # Ok se outra regiao tiver um parametro com o mesmo nome

                if not nova_regiao.checar(nome_parametro):
                    nova_regiao.push(nome_parametro, tipo_parametro, numero_regiao)
                else:
                   self.erro_id_multi_definido("Multiplo parametros declarados: " + nome_parametro, parametro.getSymbol())
        except:
            pass # Para a preocupacao de estouro de parametro

        res = self.visitChildren(ctx)
        self.regioes.pop_last() # Recupera a regiao alocada
        return res

    def visitExpr_id(self, ctx):
        nome_id = ctx.Identifier().getText()
        token = ctx.Identifier().getSymbol()
        if not self.checar(nome_id):
            # O identificador nao foi definido
            self.erro_id_nao_detectado("Identificador nao definido: " + nome_id, token)
        return self.visitChildren(ctx) # ? return self.check(nome_id)

    def visitState_lrparents(self, ctx):
        # Comeca uma nova regiao
        self.regioes.add_novo() # Aloca uma nova regiao
        res = self.visitChildren(ctx)
        self.regioes.pop_last() # Recupera a regiao alocada
        return res

    def visitState_assign(self, ctx):
        # Nao eh uma nova regiao
        regiao_atual = self.regioes.get_top()
        nome_id = ctx.Identifier().getText()
        if not self.checar(nome_id):
            self.erro_id_nao_detectado("Identificador nao definido: " + nome_id, ctx.Identifier().getSymbol())
        res = self.visitChildren(ctx)
        return res

    def visitState_array_assign(self, ctx):
        # Nao eh uma nova regiao
        regiao_atual = self.regioes.get_top()
        nome_id = ctx.Identifier().getText()
        if not self.checar(nome_id):
            self.erro_id_nao_detectado("Identificador nao definido: " + nome_id, ctx.Identifier().getSymbol())
        res = self.visitChildren(ctx)
        return res






    def visitExpr_new_array(self, ctx):
        # Nao eh uma nova regiao
        # Nao pode ter sido declarado
        regiao_atual = self.regioes.get_top()
        nome_array = ctx.Identifier().getText()

        #print("Nome array:",nome_array)
        #if not self.checar(nome_array):
        #    regiao_atual.push(nome_array, 'Usado')
        #else:
        #    self.erro_id_multi_definido("Multiplos Arrays declarados: "+ nome_array, ctx.Identifier().getSymbol())
        #res = self.visitChildren(ctx)
        #return res




    '''
    def visitExpr_method_calling(self, ctx):
        # Nao eh uma nova regiao
        # Deve ter sido declarado
        regiao_atual = self.regioes.get_top()
        nome_metodo = ctx.Identifier().getText()

        if not self.checar(nome_metodo):
            self.erro_id_nao_detectado("Metodo nao declarado: "+ nome_metodo, ctx.Identifier().getSymbol())
        res = self.visitChildren(ctx)
        return res
    '''
    def visitExpr_method_calling(self, ctx):
        #regiao_atual = self.regioes.get_top()
        nome_metodo = ctx.Identifier().getText()
        self.funcoes.append(nome_metodo)
        #print(self.funcoes)
        lista = self.funcoes

        #Adicionando na lista de chamadas de funcoes
        global tabela_Chamada_Funcao
        resultado_lista_parametros = []
        parametro1 = ctx.listaExpCamadaFuncao1
        try:
            resultado_lista_parametros.append(parametro1.getText())
        except:
            pass # Nao tem parametros

        listaParametros = ctx.listaExpCamadaFuncao2
        try:
            for i in listaParametros:
                resultado_lista_parametros.append(i.getText())
        except:
            pass # Nao tem parametros

        if classe_atual == '':
            tabela_Chamada_Funcao.adicionarListaChamadaFuncao(nome_metodo, resultado_lista_parametros, 'Principal', 'Main')
        else:
            tabela_Chamada_Funcao.adicionarListaChamadaFuncao(nome_metodo, resultado_lista_parametros, classe_atual, methodo_atual)

        return self.funcoes

# Segundo Visitor TyperCheker
class TypeChecker(MiniJavaVisitor):

    def __init__(self):
        matrix_metodo_parametros = []
        pass

    def print_erro(self, msg, token):
        linha = token.line # Numero da linha do erro
        coluna = token.column # Numero da coluna do erro
        print('Linha '+ str(linha) + ':' + str(coluna) + '\t' + 'Erro: ' + msg )

    def erro_generico_detectado(self, msg, ctx):
        #Identificador nao definido
        self.print_erro(msg, ctx)




    def visitGoal(self, ctx):
        res = self.visitChildren(ctx)
        return res

    def visitMainclass(self, ctx):
        name_classe = ctx.Identifier(0).getText()
        global classe_atual
        classe_atual = 'Principal'
        global methodo_atual
        methodo_atual = "Main"
        res = self.visitChildren(ctx)
        return res

    def visitDec_class(self, ctx):
        name_classe = ctx.Identifier(0).getText()
        global classe_atual
        classe_atual = name_classe
        res = self.visitChildren(ctx)
        return res

    def visitDec_var(self, ctx):
        var_name = ctx.Identifier().getText()
        var_type = ctx.mtype().getText()
        return self.visitChildren(ctx)

    def visitDec_method(self, ctx):
        global methodo_atual
        global matrix_parametros
        matrix_parametros = []
        nome_metodo = ctx.Identifier(0).getText()
        methodo_atual = nome_metodo
        try:
            #Possui um parametro, pelo menos
            matrix_parametros.append([ctx.tipoP1.getText(), ctx.nomeP1.text])
        except:
            pass
        listaTipos = ctx.listaTipoPs
        listaNomes = ctx.listaNomePs
        try:
            for i in range(0, len(listaNomes)):
                matrix_parametros.append(listaTipos[i].getText(), listaNomes[i].getText())
        except:
            pass
        #for i in listaParametros:
        #    resultado_lista_parametros.append(i.getText())

        res = self.visitChildren(ctx)
        return res

    def visitExpr_op_and(self, ctx):
        #print(ctx.exp1.getText(), "&&", ctx.exp2.getText())
        ctx.exp1.accept(self)
        ctx.exp2.accept(self)

    def visitExpr_op_less(self, ctx):
        #print(ctx.exp3.getText(), "<", ctx.exp4.getText())
        ctx.exp3.accept(self)
        ctx.exp4.accept(self)

    def visitExpr_op_plus(self, ctx):
        #print(ctx.exp5.getText(), "+", ctx.exp6.getText())
        ctx.exp5.accept(self)
        ctx.exp6.accept(self)

    def visitExpr_op_minus(self, ctx):
        #print(ctx.exp7.getText(), "-", ctx.exp8.getText())
        ctx.exp7.accept(self)
        ctx.exp8.accept(self)

    def visitExpr_op_multi(self, ctx):
        #print(ctx.exp9.getText(), "*", ctx.exp10.getText())
        ctx.exp9.accept(self)
        ctx.exp10.accept(self)


    #Verifica a chamada de metodo!!
    #Verifica a conformidade e a quantidade
    def visitExpr_method_calling(self, ctx):
        print("To aqui!!")
        global classe_atual
        global tabela_classe
        global tabela_variaveis
        global matrix_parametros
        name_metodo = ctx.Identifier().getText()
        resultado_lista_parametros = []
        parametro1 = ctx.listaExpCamadaFuncao1
        try:
            resultado_lista_parametros.append(parametro1.getText())
        except:
            pass  # Nao tem parametros

        listaParametros = ctx.listaExpCamadaFuncao2
        try:
            for i in listaParametros:
                resultado_lista_parametros.append(i.getText())
        except:
            pass  # Nao tem parametros

        tabela_etbs = tabela_classe.obterTabelaDaClasse(classe_atual)
        #Primeiro teste
        #tipo_chamador = ctx.exp_chamador.getText()
        tipo_chamador = ctx.exp_chamador.children
        #print(tipo_chamador[0].getText())
        type_call = tipo_chamador[0].getText()
        if type_call == 'new':
            classe_new = tipo_chamador[1].getText()
            #Pegar o tipo de retorno do metodo
            #dicionario = tabela_variaveis.obterListaVariaveisClasse(classe_new)
            listas_parametros = tabela_classe.obterListaParametros(name_metodo, classe_new)
        elif type_call == 'this':
            #dicionario = tabela_variaveis.obterListaVariaveisClasse(classe_atual)
            listas_parametros = tabela_classe.obterListaParametros(name_metodo, classe_atual)
        else:
            #Tipo Variavel para saber qual a classe do metodo
            dicionario = tabela_variaveis.obterListaVariaveisClasse(classe_atual)
            try:
                #Se ele nao tiver na lista de variaveis da classe, entao veio como parametro
                listas_parametros = tabela_classe.obterListaParametros(name_metodo, dicionario[type_call])
            except:
                #Procura na lista de parametros da classe atual
                nome_classe = ''
                for vetor in matrix_parametros:
                    for i in range(0, len(vetor)):
                        if type_call == vetor[1]:
                            nome_classe = vetor[0]
                listas_parametros = tabela_classe.obterListaParametros(name_metodo, nome_classe)

        #Verifica a quantidade de parametros passados
        if len(resultado_lista_parametros) == len(listas_parametros):
            pass
        else:
            print("Erro!! Nao possuem a mesma quantidade de parametros!!!")
            self.erro_generico_detectado("Chamada de Metodo: " + name_metodo, ctx.Identifier().getSymbol())
            sys.exit()
        #Verifica a ordem de parametros passados
        for i in range(0, len(resultado_lista_parametros)):
            tipo = ''
            #print(resultado_lista_parametros[i])
            try:
                #Tenta converter a string em numero
                int(resultado_lista_parametros[i])
                tipo = 'int'
            except:
                if resultado_lista_parametros[i] == 'false' or resultado_lista_parametros[i] == 'true':
                    tipo = 'boolean'



############Novo###################
###################################
##################################
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
    def __init__(self, name, type):
        self.typeName = name
        self.type = type

    def toString(self):
        if self.typeName != None:
            return self.typeName
        else:
            return self.type.toString()

class MethodoInfo(object):
    def __init__(self):
        self. name
        self.returnType
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

    def toString(self, nome):
        if nome == 'INT':
            return 'INT'
        elif nome == 'BOOLEAN':
            return 'BOOLEAN'
        elif nome == 'INT_ARRAY':
            return 'INT_ARRAY'
        elif nome == 'USER_DEFINED':
            return 'USER_DEFINED'
        else:
            return 'UNKKNOW'

class Scope(object):

    def __init__(self, parent):
        self.parent = parent
        if parent != None:
            self.currentClasseName = parent.currentClasseName
        else:
            self.currentClasseName = None
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
    def __init__(self):
        self.name
        self.type

    def VariableEntry(self, type, name):
        self.name = name
        self.type = type

    def toString(self):
        return self.type.toString() + ": " + self.name





class FirstVistor(ParseTreeVisitor):
    def __init__(self):
        self.classes = {}
        self.lineNumber = 1
        self.columnNumber = 1

    def visitGoal(self, ctx, classInfo):
        print(classInfo)
        #ctx.children[0].accept(self)
        ctx.mainClass().accept(self)

        for i in range(1, len(ctx.children)):
            newClass = ClassInfo
            ctx.children[i].accept(self)
        return None

    def visitMainclass(self, ctx, classInfo):
        print("TOOOOOOO AQUI")
        #print(ctx.children())







