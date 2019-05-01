import csv

#Definicicoes
palavras_reservadas = ['abstract', 'assert', 'boolean', 'break', 'byte', 'case', 'catch', 'char', 'class', 'const',
                           'continue', 'default', 'do', 'double', 'else', 'enum', 'extends', 'final', 'finally',
                           'float',
                           'for', 'if', 'goto', 'implements', 'import', 'instanceof', 'int', 'interface', 'long',
                           'native',
                           'new', 'package', 'private', 'protected', 'public', 'return', 'short', 'static', 'strictfp',
                           'super', 'switch', 'synchronized', 'this', 'throw', 'throws', 'transient', 'try', 'void',
                           'volatile', 'while', 'main', 'String', 'length', 'System', 'out',
                           'println','System.out.println'] #Tam palavras_reservadas = 57
operadores_separadores = ['(',')', '[',']', '{','}', ';','.', ',','=', '==','!=', '+','-', '*','/', '&&', '!', '<', '>',
                          '<=','>=']
literal_logico = ['true', 'false']
literal_nulo = ['null']

todosJuntos = palavras_reservadas + operadores_separadores + literal_logico + literal_nulo #Tam = 82


#Definicao das funcoes
def retornaPosicaoAlfabeto(palavra):
    resp_posicao = -1
    alfabeto = ['letra', 'numero', '_', '(', ')', '[', ']', '{', '}', ';', '.', ',', '=', '!', '+', '-', '*', '/', '>', '<',
            '&', '\n', '\r','\t', ' ', 'EOF']
    for posicao in range(0,len(alfabeto)):
        if palavra == alfabeto[posicao]:
            resp_posicao = posicao
    return resp_posicao


def retornaTabelaTransicao():##Preenchimento da tabela_transicao
    tabela_transicao = []

    arquivo = open('TabelaAutomato.csv')

    linhas = csv.reader(arquivo)
    t = 0
    for linha in linhas: #Pula a primeira linha
        if t != 0:
            vet_aux = []
            i = 0
            for posicao in linha:
                if i != 0: # Pula a primeira coluna
                    if posicao == '':
                        vet_aux.append(0)
                    else:
                        vet_aux.append(int(posicao))
                i = i + 1
            tabela_transicao.append(vet_aux)
        t = t + 1

    #for linha in tabela_transicao:
        #print(linha)

    return tabela_transicao

def retornaConjuntoEstadosFinais():
    estados_aceitacao = [2,4,10,11,13,15,17,19,21,26,29,32,33,36,37,38,40,42,44,46,48,50,52,54,56,59,60,61,62,63]
    return estados_aceitacao

def retornaEstadoInicial():
    return 0

def retornaIntLexama(lexema):
    #print(len(todosJuntos))
    num = -1
    # Devolve a posicao do vetor indicando o inteiro equivalente ao token
    if lexema in palavras_reservadas:
        for i in range(0,len(palavras_reservadas)):
            if lexema == palavras_reservadas[i]:
                num = i
                #break
                return ['PALAVRA_RESERVADA', num]
    elif lexema in operadores_separadores:
        for i in range(0,len(operadores_separadores)):
            if lexema == operadores_separadores[i]:
                num = i + len(palavras_reservadas)
                #break
                return ['OPERADOR_SEPARADOR', num]
    elif lexema in literal_logico:
        for i in range(0,len(literal_logico)):
            if lexema == literal_logico[i]:
                num = i + len(palavras_reservadas) + len(operadores_separadores)
                #break
                return ['LITERAL_LOGICO', num]
    elif lexema in literal_nulo:
        for i in range(0,len(literal_nulo)):
            if lexema == literal_nulo[i]:
                num = i + len(palavras_reservadas) + len(operadores_separadores) + len(literal_logico)
                #break
                return ['LITERAL_NULO', num]

    else:
        if lexema.isdigit(): #eh um literal inteiro
            num = 82
            return ['INTEIRO', num]
        else:
            num = 83 #eh um ID
            return ['ID', num]

