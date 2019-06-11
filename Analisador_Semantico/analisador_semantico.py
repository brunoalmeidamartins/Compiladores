txt = ' '
cont = 0
def incrementaContador():
    global cont
    cont +=1
    return "%d" %cont

class Nodo():
    pass

class Null(Nodo):
    def __init__(self):
        self.type = 'void'
    def imprimir(self, ident):
        print(ident + "nodo nulo")
    def traduzir(self):
        global txt
        id = incrementaContador()
        txt += id+"[label="+"nodo_nulo"+"]"+"\n\t"
        return id

#Funcao da Gramatica
class prog(Nodo):
    '''
    prog : main prog2
    '''
    def __init__(self,filho1, filho2 ,name):
        self.name = name
        self.filho1 = filho1
        self.filho2 = filho2
    def imprimir(self, ident):
        self.filho1.imprimir(" "+ident)
        self.filho2.imprimir(" " + ident)
        print(ident + "Nodo: "+self.name)

    def traduzir(self):
        global txt
        id = incrementaContador()
        filho1 = self.filho1.traduzir()
        filho2 = self.filho1.traduzir()

        txt += id +"[label= "+self.name+"]"+"\n\t"
        txt += id + "->"+filho1+"\n\nt"
        txt += id + "->" + filho2 + "\n\nt"
        return "digraph G {\n\t"+txt+"}"

#Funcao extendida de prog
class prog2(Nodo):
    '''
    prog2 : class prog2
          | empty
    '''

    def __init__(self, filho1, filho2=None, name="prog2"):
        self.name = name
        if filho2 ==  None:
            self.filho1 = filho1
        else:
            self.filho1 = filho1
            self.filho2 = filho2
    def imprimir(self, ident):
            self.filho1.imprimir(" "+ident)
            self.filho2.imprimir(" " + ident)
            print(ident+ "Nodo: "+self.name)

    def traduzir(self):
        global txt
        id = incrementaContador()
        return id

#Funcao da Gramatica
class main(Nodo):
    '''
    main : CLASS ID CE PUBLIC STATIC VOID MAIN PE STRING COLCE COLCD ID PD CE cmd CD CD
    '''

    def __init__(self, filho1, name):
        self.name = name
        self.filho1 = filho1
    def imprimir(self, ident):
        self.filho1.imprimir(" "+ident)
        print(ident+"Nodo: "+self.name)

    def traduzir(self):
        global txt
        id = incrementaContador()
        return id

#Funcao da Gramatica
class class1(Nodo):
    '''
    class : CLASS ID class2 CE class3 class4 CD
    '''

    def __init__(self, filho1, filho2, filho3, name):
        self.name = name
        self.filho1 = filho1
        self.filho2 = filho2
        self.filho3 = filho3

    def imprimir(self, ident):
        self.filho1.imprimir(" "+ident)
        self.filho3.imprimir(" " + ident)
        self.filho3.imprimir(" " + ident)
        print(ident + "Nodo: " + self.name)

    def traduzir(self):
        global txt
        id = incrementaContador()
        return id

#Funcao extendida de class
class class2(Nodo):
    '''
    class2 : EXTENDS ID
           | empty
    '''

    def __init__(self, filho1, name):
        self.name = name
        self.filho1 = filho1

    def imprimir(self, ident):
        self.filho1.imprimir(" "+ident)
        print(ident + "Nodo: " + self.name)

    def traduzir(self):
        global txt
        id = incrementaContador()
        return id

#Funcao extendida de class
class class3(Nodo):
    '''
    class3 : var class3
            | empty
    '''

    def __init__(self, filho1, filho2=None, name='class3'):
        self.name = name
        self.filho1 = filho1
        if filho2 != None:
            self.filho2 = filho2
    def imprimir(self, ident):
        self.filho1.imprimir(" "+ident)
        self.filho1.imprimir(" " + ident)
        print(ident + "Nodo: "+ self.name)

    def traduzir(self):
        global txt
        id = incrementaContador()
        return id


#TODO



#Funcao extendida de class
class class4(Nodo):
    '''
    class4 : method class4
            | empty
    '''

    def __init__(self, name):
        self.name = name

    def traduzir(self):
        global txt
        id = incrementaContador()
        return id

#Funcao da Gramatica
class var(Nodo):
    '''
    var : type ID PONTOVIRGULA
    '''

    def __init__(self, name):
        self.name = name

    def traduzir(self):
        global txt
        id = incrementaContador()
        return id

#Funcao da Gramatica
class method(Nodo):
    '''
    method : PUBLIC type ID PE method2 PD CE method3 method4 RETURN exp PONTOVIRGULA CD
    '''

#Funcao extendida de method
class method2(Nodo):
    '''
    method2 : params
            | empty
    '''

    def __init__(self, name):
        self.name = name

    def traduzir(self):
        global txt
        id = incrementaContador()
        return id

#Funcao extendida de method
class method3(Nodo):
    '''
    method3 : var method3
            | empty
    '''

    def __init__(self, name):
        self.name = name

    def traduzir(self):
        global txt
        id = incrementaContador()
        return id

#Funcao extendida de method
class method4(Nodo):
    '''
    method4 : cmd method4
            | empty
    '''

    def __init__(self, name):
        self.name = name

    def traduzir(self):
        global txt
        id = incrementaContador()
        return id

#Funcao da Gramatica
class params(Nodo):
    '''
    params : type ID params2
    '''

    def __init__(self, name):
        self.name = name

    def traduzir(self):
        global txt
        id = incrementaContador()
        return id

#Funcao extendida de params
class params2(Nodo):
    '''
    params2 : VIRGULA type ID params2
            | empty
    '''

    def __init__(self, name):
        self.name = name

    def traduzir(self):
        global txt
        id = incrementaContador()
        return id

#Funcao da Gramatica
class type(Nodo):
    '''
    type : INT COLCE COLCD
         | BOOLEAN
         | INT
         | ID
    '''

    def __init__(self, name):
        self.name = name

    def traduzir(self):
        global txt
        id = incrementaContador()
        return id

#Funcao da Gramatica
class cmd(Nodo):
    '''
    cmd : CE cmd2 CD
        | IF PE exp PD cmd
        | IF PE exp PD cmd ELSE cmd
        | WHILE PE exp PD cmd
        | SYSTEMOUTPRINTLN PE exp PD PONTOVIRGULA
        | ID IGUAL exp PONTOVIRGULA
        | ID COLCE exp COLCD IGUAL exp PONTOVIRGULA
    '''

    def __init__(self, name):
        self.name = name

    def traduzir(self):
        global txt
        id = incrementaContador()
        return id

#Funcao extendida de cmd
class cmd2(Nodo):
    '''
    cmd2 : cmd cmd2
         | empty
    '''

    def __init__(self, name):
        self.name = name

    def traduzir(self):
        global txt
        id = incrementaContador()
        return id

#Funcao da Gramatica
#Conflito de exp && exp => exp && rexp
class exp(Nodo):
    '''
    exp : exp ECOMERCIAL rexp
        | rexp
    '''

    def __init__(self, name):
        self.name = name

    def traduzir(self):
        global txt
        id = incrementaContador()
        return id

#Funcao da Gramatica
class rexp(Nodo):
    '''
    rexp : rexp MENOR aexp
         | rexp COMPARACAO aexp
         | rexp DIFERENTE aexp
         | aexp
    '''

    def __init__(self, name):
        self.name = name

    def traduzir(self):
        global txt
        id = incrementaContador()
        return id

#Funcao da Gramatica
class aexp(Nodo):
    '''
    aexp : aexp MAIS mexp
         | aexp MENOS mexp
         | mexp
    '''

    def __init__(self, name):
        self.name = name

    def traduzir(self):
        global txt
        id = incrementaContador()
        return id

#Funcao da Gramatica
class mexp(Nodo):
    '''
    mexp : mexp MULTIPLICA sexp
         | mexp DIVIDE sexp
         | sexp
    '''

    def __init__(self, name):
        self.name = name

    def traduzir(self):
        global txt
        id = incrementaContador()
        return id

#Funcao da Gramatica
class sexp(Nodo):
    '''
    sexp : NEGACAO sexp
         | MENOS sexp
         | TRUE
         | FALSE
         | NUMERO
         | NULL
         | NEW INT COLCE exp COLCD
         | pexp PONTO LENGTH
         | pexp COLCE exp COLCD
         | pexp
    '''

    def __init__(self, name):
        self.name = name

    def traduzir(self):
        global txt
        id = incrementaContador()
        return id

#Funcao da Gramatica
class pexp(Nodo):
    '''
    pexp : ID
         | THIS
         | NEW ID PE PD
         | PE exp PD
         | pexp PONTO ID
         | pexp PONTO ID PE pexp2 PD
    '''

    def __init__(self, name):
        self.name = name

    def traduzir(self):
        global txt
        id = incrementaContador()
        return id
#Funcao extendida de pexp
class pexp2(Nodo):
    '''
    pexp2 : exps
          | empty
    '''

    def __init__(self, name):
        self.name = name

    def traduzir(self):
        global txt
        id = incrementaContador()
        return id

#Funcao da Gramatica
class exps(Nodo):
    '''
    exps : exp exps2
    '''
#Funcao extendida de exps
class exps2(Nodo):
    '''
    exps2 : VIRGULA exp exps2
          | empty
    '''

    def __init__(self, name):
        self.name = name

    def traduzir(self):
        global txt
        id = incrementaContador()
        return id

#Funcao para gerar o log de erro!
class error(Nodo):
    '''
    error
    '''
    #global codigo_valido
    #codigo_valido = False
    #print("Erro Sintatico encontrado: ", p)
    def __init__(self, name):
        self.name = name

    def traduzir(self):
        global txt
        id = incrementaContador()
        return id


#Funcao para gerar vazio
class empty(Nodo):
    ''' empty : '''

    def __init__(self, name):
        self.name = name

    def traduzir(self):
        global txt
        id = incrementaContador()
        return id