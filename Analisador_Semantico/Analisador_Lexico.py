#import Tabelas as tb

class Tabelas():
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
    def __init__(self):
        pass

    def retornaPosicaoAlfabeto(self, palavra):
        resp_posicao = -1
        alfabeto = ['letra', 'numero', '_', '(', ')', '[', ']', '{', '}', ';', '.', ',', '=', '!', '+', '-', '*', '/', '>', '<',
                '&', '\n', '\r','\t', ' ', 'EOF']
        for posicao in range(0,len(alfabeto)):
            if palavra == alfabeto[posicao]:
                resp_posicao = posicao
        return resp_posicao


    def retornaTabelaTransicao(self):##Preenchimento da tabela_transicao
        tabela_transicao =[
                        [1, 3, 1, 39, 41, 51, 53, 43, 45, 49, 55, 47, 8, 27, 12, 14, 16, 18, 34, 30, 57, 0, 0, 0, 0, 0] ,
                        [1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2] ,
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] ,
                        [4, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4] ,
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] ,
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] ,
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] ,
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] ,
                        [11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 9, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11] ,
                        [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10] ,
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] ,
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] ,
                        [13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13] ,
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] ,
                        [15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15] ,
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] ,
                        [17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17] ,
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] ,
                        [19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 23, 20, 19, 19, 19, 19, 19, 19, 19, 19] ,
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] ,
                        [20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 22, 20, 20, 20, 21] ,
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] ,
                        [63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63] ,
                        [23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 24, 23, 0, 0, 23, 23, 23, 23, 23, 62] ,
                        [23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 24, 25, 23, 23, 23, 23, 23, 23, 23, 62] ,
                        [63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63] ,
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] ,
                        [61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 28, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61] ,
                        [29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29] ,
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] ,
                        [33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 31, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33] ,
                        [32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32] ,
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] ,
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] ,
                        [37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 35, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37] ,
                        [36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36] ,
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] ,
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] ,
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] ,
                        [40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40] ,
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] ,
                        [42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42] ,
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] ,
                        [44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44] ,
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] ,
                        [46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46] ,
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] ,
                        [48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48] ,
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] ,
                        [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50] ,
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] ,
                        [52, 52, 52, 52, 52, 52, 52, 52, 52, 52, 52, 52, 52, 52, 52, 52, 52, 52, 52, 52, 52, 52, 52, 52, 52, 52] ,
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] ,
                        [54, 54, 54, 54, 54, 54, 54, 54, 54, 54, 54, 54, 54, 54, 54, 54, 54, 54, 54, 54, 54, 54, 54, 54, 54, 54] ,
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] ,
                        [56, 56, 56, 56, 56, 56, 56, 56, 56, 56, 56, 56, 56, 56, 56, 56, 56, 56, 56, 56, 56, 56, 56, 56, 56, 56] ,
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] ,
                        [60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 58, 60, 60, 60, 60, 60] ,
                        [59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59] ,
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] ,
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] ,
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] ,
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] ,
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] ,
                        ]

        return tabela_transicao

    def retornaConjuntoEstadosFinais(self):
        estados_aceitacao = [2,4,10,11,13,15,17,19,21,26,29,32,33,36,37,38,40,42,44,46,48,50,52,54,56,59,60,61,62,63]
        return estados_aceitacao

    def retornaEstadoInicial(self):
        return 0

    def retornaIntLexama(self, lexema):
        #print(len(todosJuntos))
        num = -1
        # Devolve a posicao do vetor indicando o inteiro equivalente ao token
        if lexema in self.palavras_reservadas:
            for i in range(0,len(self.palavras_reservadas)):
                if lexema == self.palavras_reservadas[i]:
                    num = i
                    #break
                    return ['PALAVRA_RESERVADA', num]
        elif lexema in self.operadores_separadores:
            for i in range(0,len(self.operadores_separadores)):
                if lexema == self.operadores_separadores[i]:
                    num = i + len(self.palavras_reservadas)
                    #break
                    return ['OPERADOR_SEPARADOR', num]
        elif lexema in self.literal_logico:
            for i in range(0,len(self.literal_logico)):
                if lexema == self.literal_logico[i]:
                    num = i + len(self.palavras_reservadas) + len(self.operadores_separadores)
                    #break
                    return ['LITERAL_LOGICO', num]
        elif lexema in self.literal_nulo:
            for i in range(0,len(self.literal_nulo)):
                if lexema == self.literal_nulo[i]:
                    num = i + len(self.palavras_reservadas) + len(self.operadores_separadores) + len(self.literal_logico)
                    #break
                    return ['LITERAL_NULO', num]

        else:
            if lexema.isdigit(): #eh um literal inteiro
                num = 82
                return ['INTEIRO', num]
            else:
                num = 83 #eh um ID
                return ['ID', num]

class analisador_lexico():
    tb = Tabelas()
    #Verifica se o caracter eh uma letra, numero ou outro
    def __init__(self):
        '''Definicao dos vetores'''
        self.tb = Tabelas()
        self.alfha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u',
                 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
                 'P',
                 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '_']
        self.numerico = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        self.brancos = [' ', '\n', '\t', '\r', '\f']

        self.fim_arquivo = ['EOF']

        self.alfabeto = self.alfha + self.numerico + self.brancos + self.fim_arquivo + self.tb.operadores_separadores + [
            '&']  # Define o alfabeto do automato

    def retornaValorCaracter(self, caracter):
        elemento = -1
        if caracter in self.alfha:
            elemento = self.tb.retornaPosicaoAlfabeto('letra')
        elif caracter in self.numerico:
            elemento = self.tb.retornaPosicaoAlfabeto('numero')
        else:
            elemento = self.tb.retornaPosicaoAlfabeto(caracter)
        return elemento

    #Faz a analise de todos os tokens e retorna o vetor de tokens contendo informando se existe erro
    def retornaVetorTokens(self, texto, vet_soma_cada_linha):
        contador_posicao_caracter = 0
        erro = False #Monitora se ha erro ou nao no lexico
        vetor_tokens = []
        tabela_transicao = self.tb.retornaTabelaTransicao()
        estados_finais = self.tb.retornaConjuntoEstadosFinais()
        estado_inicial = self.tb.retornaEstadoInicial()
        posicao = 0

        text = texto
        estado = estado_inicial
        elemento = -1
        lexema = ''

        while (posicao < len(text)):
            elemento = self.retornaValorCaracter(text[posicao])  # Pega a posicao do elemento na tabela
            if self.verificaCaracterValido(text[posicao]): #Verifica caracter valido
                estado = tabela_transicao[estado][elemento]  # Funcao de transicao
                if text[posicao] not in self.brancos:
                    lexema = lexema + text[posicao]

                ##Logica: Olha para o proximo e verificar se vai formar token
                if posicao + 1 < len(text):
                    elemento = self.retornaValorCaracter(text[posicao + 1])
                    estado_aux = tabela_transicao[estado][elemento]
                    if estado_aux in estados_finais:
                        if estado_aux == 62:
                            print('ERRO: Nao pode terminar o arquivo sem fechar o comentario de multiplas linhas!!')
                            erro = True
                            self.verificaLinhaErro(contador_posicao_caracter, vet_soma_cada_linha)
                            break
                        #print('token:', lexema, self.verificaLexema(lexema)[0])
                        posicao_lexema = self.verificaLexema(lexema)
                        linha_token = self.verificaLinhaLexema(contador_posicao_caracter, vet_soma_cada_linha) #Retorna um vetor
                        if self.verificaLexemaComentario(lexema):
                            vetor_tokens.append([posicao_lexema[0],posicao_lexema[1],lexema, linha_token]) #[O que eh, inteiro que representa, token, linha]
                        estado = estado_inicial
                        lexema = ''
                        posicao = posicao + 1
                    else:
                        posicao = posicao + 1
                else:
                    posicao = posicao + 1
            else:
                print('ERRO: Caracter invalido!!')
                erro = True
                self.verificaLinhaErro(contador_posicao_caracter, vet_soma_cada_linha)
                break
            if erro != True:
                contador_posicao_caracter = contador_posicao_caracter + 1
        #Corrigindo o System.out.println
        vet_aux = []
        vet_posicoes_descartadas = []
        for i in range(0,len(vetor_tokens)):
            if vetor_tokens[i][2] == 'System': #Verificar as 4 posicoes posteriores para saber se eh o comando "System.out.println"
                if len(vetor_tokens) - i > 4:
                    if vetor_tokens[i+1][2] == '.' and vetor_tokens[i+2][2] == 'out' and vetor_tokens[i+3][2] == '.' and vetor_tokens[i+4][2] == 'println':
                        posicao_lexema = self.verificaLexema('System.out.println')
                        vet_aux.append([vetor_tokens[i][0],posicao_lexema[1],'System.out.println',vetor_tokens[i][3]])
                        vet_posicoes_descartadas.append(i + 1)
                        vet_posicoes_descartadas.append(i + 2)
                        vet_posicoes_descartadas.append(i + 3)
                        vet_posicoes_descartadas.append(i + 4)
                    else:
                        vet_aux.append(vetor_tokens[i])
                else:
                    vet_aux.append(vetor_tokens[i])
            else:
                vet_aux.append(vetor_tokens[i])
        vet_aux_2 = []
        #Retira as posicoes a serem descartadas do vetor de tokens
        for i in range(0,len(vet_aux)):
            if i not in vet_posicoes_descartadas:
                vet_aux_2.append(vet_aux[i])
        vetor_tokens = vet_aux_2


        return [erro, vetor_tokens]

    #Verifica se o lexema eh um comentario pequeno ou grande
    def verificaLexemaComentario(self,lexema):
        lexema_notiscomentario = True
        if len(lexema) > 1:
            if lexema[0] == '/' and lexema[1] == '/' or lexema[1] == '*':
                lexema_notiscomentario = False
        return lexema_notiscomentario


    #Verifica o inteiro que representa o lexema
    def verificaLexema(self,lexema):
        return self.tb.retornaIntLexama(lexema)

    #Verifica se o caracter eh valido
    def verificaCaracterValido(self, caracter):
        if caracter in self.alfabeto:
            return True
        else:
            return False

    #Verifica a linha do lexema
    def verificaLinhaLexema(self, posicao, vet_soma_cada_linha):
        # Busca Binaria
        retorno = -1
        linha = self.BinSearch(posicao, vet_soma_cada_linha, 0,len(vet_soma_cada_linha) - 1)  # Recebe um vetor
        if linha[1] == -1:
            retorno = linha[0] + 1
        else:
            retorno = linha[0] + 2
        return retorno

    #Verifica a linha que contem o erro
    def verificaLinhaErro(self, posicao_erro, vet_soma_cada_linha):
        #Busca Binaria
        retorno = -1
        linha_erro = self.BinSearch(posicao_erro,vet_soma_cada_linha,0,len(vet_soma_cada_linha)-1) #Recebe um vetor
        if linha_erro[1] == -1:
            retorno = linha_erro[0] + 1
        else:
            retorno = linha_erro[0] + 2
        print("Erro na linha: ",retorno)

    #Funcao de Busca Binaria
    def BinSearch(self, chave, D, minD, maxD):  # Retorna posicao
        # Condicao de parada da recursao
        if minD <= maxD:
            q = (minD + maxD) // 2
            if chave > D[q]:
                return self.BinSearch(chave, D, q + 1, maxD)
            elif chave < D[q]:
                return self.BinSearch(chave, D, minD, q - 1)
            else:
                return [q, chave]  # Retorna a posicao e valor ## Achou o valor midQval
        # Elemento nao encontrado no vetor
        if maxD + 1 < len(D):
            return [maxD + 1,
                    -1]  # Retorna a posicao mais alta depois do valor a ser encontrado \  ex: 5 entre 4 e 6; retorna a posicao do 6
        else:
            return [maxD, -1]

    def funcaoPrincipalAnalisadorLexico(self, path_arquivo):
        #arq = open('programa.txt', 'r')
        arq = open(path_arquivo, 'r')
        texto = arq.readlines()
        arq.close()

        vetor_caracter = []

        vet_tam_cada_linha = []  # Guarda o tamanho de cada linha do arquivo

        for linha in texto:
            vet_tam_cada_linha.append(len(linha))  # Captura o tam da linha
            for caracter in linha:
                vetor_caracter.append(caracter)

        vetor_caracter.append('EOF')
        vet_tam_cada_linha[len(vet_tam_cada_linha) - 1] = vet_tam_cada_linha[len(
            vet_tam_cada_linha) - 1] + 1  # Aumenta mais um por causa do EOF acrescentado no final

        # Vetor de soma de caracter de cada linha
        vet_soma_cada_linha = []
        aux_soma = 0
        for i in range(0, len(vet_tam_cada_linha)):
            if i == 0:
                vet_soma_cada_linha.append(vet_tam_cada_linha[i])
                aux_soma = vet_tam_cada_linha[i]
            else:
                aux_soma = aux_soma + vet_tam_cada_linha[i]
                vet_soma_cada_linha.append(aux_soma)

        vetor_tokens = self.retornaVetorTokens(vetor_caracter, vet_soma_cada_linha)
        # Imprime Resultado
        #if not vetor_tokens[0]:
            # print(a[1])
            #for i in vetor_tokens[1]:
                #print(i)
        return vetor_tokens[1]



#MAIN()
'''
if __name__ == "__main__":
    analisador_lexico = analisador_lexico()
    tokens = analisador_lexico.funcaoPrincipalAnalisadorLexico('Programas_MiniJava/programa2.java') #Path do arquivo
    print(tokens)
'''







