from enum import Enum

class TipoVariavel(Enum):
    INTEIRO = 0
    BOOLEAN = 1

class EntradaTabelaDeSimbolos():

    def __init__(self):
        self.tipo = TipoVariavel
        self.nome

class TabelaDeSimbolos():

    def __init__(self):
        self.lista_tabelaDeSimbolos = []

    def instalarNome(self, nome, tipo):

        if self.jaFoiDeclarado(nome):
            print('Erro semantico: Variavel', nome, 'foi declarada duas vezes')
            #Parar a execucao
            breakpoint(0)
        etds = EntradaTabelaDeSimbolos()
        etds.nome = nome
        etds.tipo = tipo
        self.lista_tabelaDeSimbolos.append(etds)
        return len(self.lista_tabelaDeSimbolos) - 1

    def determinaTipo(self, nome):
        for i in self.lista_tabelaDeSimbolos:
            if i.nome == nome:
                return i.tipo
        return None


    def jaFoiDeclarado(self, nome):
        for i in self.lista_tabelaDeSimbolos:
            if i.nome == nome:
                return True
        return False
