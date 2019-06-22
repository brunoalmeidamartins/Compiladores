from TabelaDeSimbolos import *
class Escopos():
    def __init__(self):
        self.pilhaDeTabelas = []
        self.criarNovoEscopo()

    def criarNovoEscopo(self):
        self.pilhaDeTabelas.append(TabelaDeSimbolos())

    def pegarEscopoAtual(self):
        return self.pilhaDeTabelas[-1] #Retorno o topo da pilha

    def percorrerEscoposAninhados(self):
        return self.pilhaDeTabelas

    def abandonarEscopo(self):
        self.pilhaDeTabelas.pop()