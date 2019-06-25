class EntradaTabelaSimbolos(object):

    def __init__(self):
        self.nome = ''
        self.valor = ''

class EntradaTabelaSimbolosClasses(object):

    def __init__(self):
        self.nome = ''
        self.lista_methodos = {}
        self.extends = False
        self.extendeQuem = ''


class EntradaTabelaSimbolosMethodos(object):

    def __init__(self):
        self.nome = ''
        self.parametros = []
        self.tipoMetodo = ''

class EntradaTabelaSimbolosVariavel(object):

    def __init__(self):
        self.nome = ''
        self.tipo = ''
        self.valor = ''
        self.regiao = -1
        self.classe = ''
        self.methodo = ''

class EntradaTabelaSimbolosChamadaFuncao(object):

    def __init__(self):
        self.nome = ''
        self.lista_parametros = []
        self.classe = ''
        self.metodo = ''
