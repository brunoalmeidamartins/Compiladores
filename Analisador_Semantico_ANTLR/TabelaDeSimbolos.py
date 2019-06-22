from EntradaTabelaSimbolos import *

class TabelaDeSimbolos:
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
