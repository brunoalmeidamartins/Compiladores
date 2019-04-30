import csv

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

    arquivo = open('TabelaAutomato2.csv')

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
    return tabela_transicao

def retornaConjuntoEstadosFinais():
    estados_aceitacao = [2,4,10,11,13,15,17,19,21,26,29,32,33,36,37,38,40,42,44,46,48,50,52,54,56,59,60,61,62]
    return estados_aceitacao

def retornaEstadoInicial():
    return 0