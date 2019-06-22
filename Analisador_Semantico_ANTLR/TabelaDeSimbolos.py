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

    def inserirMetodos(self, nomeClasse, nomeMetodo):
        if self.verificarClasseJaExiste(nomeClasse):
            tc = self.tabelaClasses.get(nomeClasse)
            tc.methodos.append(nomeMetodo)
        else:
            self.inserirClasse(nomeClasse)
            tc = self.tabelaClasses.get(nomeClasse)
            tc.methodos.append(nomeMetodo)

    def imprimirTabela(self):
        valores = self.tabelaClasses.keys()
        for i in valores:
            print("Classe:", self.tabelaClasses[i].nome)
            print("Metodos:", self.tabelaClasses[i].methodos, '\n')

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
                grafo.conectar(self.tabelaClasses[i].nome, self.tabelaClasses[i].extendeQuem)

        for no in lista_nos:
            if grafo.verificar_ciclos(no):
                print("Circularidade Hieraquica encontrada!!")
                print("Classe:", no)
                sys.exit()



