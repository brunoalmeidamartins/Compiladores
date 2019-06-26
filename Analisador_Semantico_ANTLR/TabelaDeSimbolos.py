from collections import defaultdict
import sys
if __name__ is not None and "." in __name__:
    from .EntradaTabelaSimbolos import *

else:
    from EntradaTabelaSimbolos import *
    from Grafos import *

class TabelaDeSimbolos(object):
    def __init__(self):
        self.tabelaDeSimbolos = {} #{Nome, EntradaTabelaDeSimbolos}

    def inserir(self, nome, valor):
        etds = EntradaTabelaSimbolos
        etds.nome = nome
        etds.valor = valor
        self.tabelaDeSimbolos[nome] = etds

    def verificar(self, nome):
        if not nome in self.tabelaDeSimbolos:
            return None
        else:
            return self.tabelaDeSimbolos.get(nome)

class TabelaDeClasses(object):
    def __init__(self):
        self.tabelaClasses = {}

    def inserirClasse(self, nome, extendeQuem='Ninguem'):
        if not self.verificarClasseJaExiste(nome):
            tc = EntradaTabelaSimbolosClasses()
            tc.nome = nome
            if extendeQuem != 'Ninguem':
                tc.extendeQuem = extendeQuem
                tc.extends = True
            self.tabelaClasses[nome] = tc
        else:
            tc = self.tabelaClasses.get(nome)
            if extendeQuem != 'Ninguem':
                tc.extendeQuem = extendeQuem
                tc.extends = True

    def obterTabelaDaClasse(self, nome):
        return self.tabelaClasses.get(nome)

    def obterListaParametros(self, nomeMetodo, nomeClasse='', tipoChamador=''):
        classeContemMetodo = ''
        if nomeClasse == '':
            valores = self.tabelaClasses.keys()
            for i in valores:
                tc = self.tabelaClasses.get(i)
                lista = tc.lista_methodos
                for j in lista:
                    if j == nomeMetodo:
                        classeContemMetodo = i
                        break
            tc = self.tabelaClasses.get(classeContemMetodo)
            lista = tc.lista_methodos.get(nomeMetodo).parametros
            return lista
        else:
            tc = self.tabelaClasses.get(nomeClasse)
            lista = tc.lista_methodos.get(nomeMetodo).parametros
            return lista



        #return tc.lista_methodos.get(nomeMetodo).parametros

    def inserirMetodos(self, nomeClasse, nomeMetodo, tipoMetodo):
        metodo = EntradaTabelaSimbolosMethodos()
        metodo.nome = nomeMetodo
        metodo.tipoMetodo = tipoMetodo
        if self.verificarClasseJaExiste(nomeClasse):
            tc = self.tabelaClasses.get(nomeClasse)
            tc.lista_methodos[nomeMetodo] = metodo
        else:
            self.inserirClasse(nomeClasse)
            tc = self.tabelaClasses.get(nomeClasse)
            tc.lista_methodos[nomeMetodo] = metodo

    def inserirParametros(self, nomeClasse, nomeMetodo, tipoParametro):
        tc = self.tabelaClasses.get(nomeClasse)
        lista = tc.lista_methodos.get(nomeMetodo).parametros
        lista.append(tipoParametro)

    def imprimirTabela(self):
        valores = self.tabelaClasses.keys()
        for i in valores:
            print("Classe:", self.tabelaClasses[i].nome)
            print("Lista de Metodos:")
            #for j in self.tabelaClasses[i].lista_methodos:
            #    print(j.nome)
            self.imprimirLisstaMethodos(self.tabelaClasses[i].lista_methodos)
            print('\n')

    def imprimirLisstaMethodos(self, lista_methodos):
        valores = lista_methodos.keys()
        for i in valores:
            print("Metodo:",lista_methodos[i].nome, "Tipo:", lista_methodos[i].tipoMetodo)
            print('Lista parametros: ', lista_methodos[i].parametros)

    def verificarClasseJaExiste(self, nomeClasse):
        if nomeClasse in self.tabelaClasses:
            return True
        else:
            return False

    def verificaCircularidadeHierarquica(self):
        grafo = Grafo()

        valores = self.tabelaClasses.keys()
        lista_nos = []
        for i in valores:
            if self.tabelaClasses[i].extends:
                lista_nos.append(self.tabelaClasses[i].nome)
                print(self.tabelaClasses[i].nome, self.tabelaClasses[i].extendeQuem)
                grafo.conectar(self.tabelaClasses[i].nome, self.tabelaClasses[i].extendeQuem)

        for no in lista_nos:
            if grafo.verificar_ciclos(no):
                print("Circularidade Hieraquica encontrada!!")
                print("Classe:", no)
                sys.exit()

class TabelaDeVariaveis(object):
    def __init__(self):
        self.tabelaVariaveis = {}

    def adicionar(self, nome, tipo, valor, regiao, classe, metodo):
        tv = EntradaTabelaSimbolosVariavel()
        tv.nome = nome
        tv.tipo = tipo
        tv.valor = valor
        tv.regiao = regiao
        tv.classe = classe
        tv.metodo = metodo
        if not self.verificaExisteRegiao(regiao):
            self.tabelaVariaveis[regiao] = [tv]
        else:
            lista = self.tabelaVariaveis.get(regiao)
            lista.append(tv)


    def verificaExisteRegiao(self, regiao):
        if regiao in self.tabelaVariaveis:
            return True
        else:
            return False
    def imprimeListaVariaveis(self):
        valores = self.tabelaVariaveis.keys()
        for i in valores:
            for j in self.tabelaVariaveis[i]:
                print("Regiao:",j.regiao," Classe:",j.classe," Metodo:",j.metodo,"Variavel:",j.nome, " Tipo:", j.tipo, " Valor: ", j.valor)

    def obterListaVariaveisClasse(self, classe):
        lista = {}
        tipo_classe = ''
        values = self.tabelaVariaveis.keys()
        for i in values:
            for j in self.tabelaVariaveis.get(i):
                if classe == j.classe:
                    lista[j.nome] = j.tipo
        return lista

class TabelaDeChamadaFuncao(object):

    def __init__(self):
        self.listaChamdaFuncao =[]

    def adicionarListaChamadaFuncao(self, nome, listaParametros, classe, metodo):
        tcf = EntradaTabelaSimbolosChamadaFuncao()
        tcf.nome = nome
        tcf.classe = classe
        tcf.metodo = metodo
        for i in listaParametros:
            tcf.lista_parametros.append(i)
        self.listaChamdaFuncao.append(tcf)

    def imprimeListaChamadaFuncao(self):
        for i in self.listaChamdaFuncao:
            print("Nome Funcao:", i.nome, " Lista Parametros Passados:", i.lista_parametros, " Classe:", i.classe, " Metodo:", i.metodo)



