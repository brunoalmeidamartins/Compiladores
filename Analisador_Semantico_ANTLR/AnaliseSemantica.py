from antlr4 import *
from MiniJavaVisitor import *
from MiniJavaListener import *

#ctx: Contexto

class Regiao_Identificador(object):
    '''
    Usa um dicionario para guardar o identificadores e seus valores em uma regiao
    '''
    def __init__(self):
        self.identificadores = {} #dict
    def adicionar(self, identificador, valor):
        try:
            self.identificadores[identificador] = valor
        except:
            print("Erro ao adicionar o identificador")
    def remover(self, identificador):
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
class pilha_regiao_identificadores(object):
    ''' 
    Usando uma pilha para armazenar as regioes validas de um identificador
    '''
    def __init__(self):
        self.identificadores = {} # Valores atuias dos identificadores e seus valores
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
        r = Regiao_Identificador()
        self._stack.append(r)
        self._history_list.append(r)
        return r

    def get_top(self):
        return self._stack[-1] #Retorna a pilha original para ser modificada

    def pop_last(self):
        ultimo = self._stack.pop()
        self._history_list.append('POP')
        return ultimo

# Implementacao do nosso visitor
class Meu_Visitor(MiniJavaVisitor):

    def __init__(self):
        self.regiao = pilha_regiao_identificadores()

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
        return self.regiao.checar(identificador)

    def visitGoal(self, ctx):
        # Comeco, aloca uma nova regiao
        self.regiao.add_novo() #Aloca uma nova regiao
        res = self.visitChildren(ctx)
        self.regiao.pop_last() # Recupera a regiao alocada
        return res

    def visitMainClass(self, ctx):
        '''
        Uma nova classe MAIN. Verifica se foi definida e coloca na regiao atual
        Comeca uma nova regiao
        '''
        regiao_atual = self.regiao.get_top()

        nome_classe = ctx.Identifier(0).getText()
        if not self.checar(nome_classe):
            #Verifica se a MAINCLASS nao foi definida em uma regiao
            regiao_atual.adicionar(nome_classe, 'main_class')
        else:
            self.erro_id_multi_definido("Multiplas Mainclass Declaradas: " + nome_classe, ctx.Identifier(0).getSymbol())

        #Inicia uma nova regiao
        self.regiao.add_novo() #Adiciona uma nova regiao
        res = self.visitChildren(ctx)
        self.regiao.pop_last() # Recupera a regiao alocada
        return res

    def visitDec_class(self, ctx):
        '''
        Uma nova Class. Verifica se foi definida e coloca na regiao atual
        Comeca uma nova regiao
        '''
        regiao_atual = self.regiao.get_top()

        nome_classe = ctx.Identifier(0).getText()
        if not self.checar(nome_classe):
            # Coloca na regiao atual
            regiao_atual.adicionar(nome_classe, 'Classe Declarada')
        else:
            self.erro_id_multi_definido("Multiplas Classes Declaradas: " + nome_classe, ctx.Identifier(0).getSymbol())

        #comeca uma nova regiao
        self.regiao.add_novo() # Adiciona uma nova regiao
        res = self.visitChildren(ctx)
        self.regiao.pop_last() # Recupera a regiao alocada
        return res

    def visitDec_var(self, ctx):
        '''
        Verifica se uma nova variavel declarada foi declarada multiplas vezes
        '''
        regiao_atual = self.regiao.get_top()
        var_name = ctx.Identifier().getText()
        var_type = ctx.mtype().getText()

        if not self.checar(var_name):
            # Coloca na regiao atual
            regiao_atual.adicionar(var_name, var_type)
        else:
            self.erro_id_multi_definido("Multiplas Variaveis declaradas: " + var_name, ctx.Identifier().getSymbol())
        return self.visitChildren(ctx)

    def visitDec_method(self, ctx):
        '''
        Verifica se o nome do metodo foi definido
        Comeca uma nova regiao
        '''
        regiao_atual = self.regiao.get_top()
        nome_metodo = ctx.Identifier(0).getText()
        tipo_metodo = ctx.mtype(0).getText()
        if not self.checar(nome_metodo):
            regiao_atual.adicionar(nome_metodo, tipo_metodo)
        else:
            self.erro_id_multi_definido("Multiplos metodos declarados: " + nome_metodo, ctx.Identifier(0).getSymbol())
        nova_regiao = self.regiao.add_novo() # Nova regiao pra o metodo
        # Nao pode obter o numero exato de parametros, verifique os 12 parametros anteriores
        try:
            for i in range(1,12):
                # mtype(0) eh o nome do metodo
                parametro = ctx.Identifier(i)
                nome_parametro = ctx.Identifier(i).getText()
                tipo_parametro = ctx.mtype(i).getText()

                #Verfica se tem dois parametros iguais
                # Ok se outra regiao tiver um parametro com o mesmo nome

                if not nova_regiao.checar(nome_parametro):
                    nova_regiao.adicionar(nome_parametro, tipo_parametro)
                else:
                   self.erro_id_multi_definido("Multiplo parametros declarados: " + nome_parametro, parametro.getSymbol())
        except:
            pass # Para a preocupacao de estouro de parametro

        res = self.visitChildren(ctx)
        self.regiao.pop_last() # Recupera a regiao alocada
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
        self.regiao.add_novo() # Aloca uma nova regiao
        res = self.visitChildren(ctx)
        self.regiao.pop_last() # Recupera a regiao alocada
        return res

    def visitState_assign(self, ctx):
        # Nao eh uma nova regiao
        regiao_atual = self.regiao.get_top()
        nome_id = ctx.Identifier().getText()
        if not self.checar(nome_id):
            self.erro_id_nao_detectado("Identificador nao definido: " + nome_id, ctx.Identifier().getSymbol())
        res = self.visitChildren(ctx)
        return res

    def visitState_array_assign(self, ctx):
        # Nao eh uma nova regiao
        regiao_atual = self.regiao.get_top()
        nome_id = ctx.Identifier().getText()
        if not self.checar(nome_id):
            self.erro_id_nao_detectado("Identificador nao definido: " + nome_id, ctx.Identifier().getSymbol())
        res = self.visitChildren(ctx)
        return res

    def visitExpr_new_array(self, ctx):
        # Nao eh uma nova regiao
        # Nao pode ter sido declarado
        regiao_atual = self.regiao.get_top()
        nome_array = ctx.Identifier().getText()
        if not self.checar(nome_array):
            regiao_atual.adicionar(nome_array, 'Usado')
        else:
            self.erro_id_multi_definido("Multiplos Arrays declarados: "+ nome_array, ctx.Identifier().getSymbol())
        res = self.visitChildren(ctx)
        return res

    def visitExpr_method_calling(self, ctx):
        # Nao eh uma nova regiao
        # Deve ter sido declarado
        regiao_atual = self.regiao.get_top()
        nome_metodo = ctx.Identifier().getText()

        if not self.checar(nome_metodo):
            self.erro_id_nao_detectado("Metodo nao declarado: "+ nome_metodo, ctx.Identifier().getSymbol())
        res = self.visitChildren(ctx)
        return res





