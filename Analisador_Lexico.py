import Tabelas as tb

class analisador_lexico():
    '''
    Definicao dos vetores
    '''
    alfha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
             'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '_']
    numerico = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    brancos = [' ', '\n', '\t', '\r', '\f']

    fim_arquivo = ['EOF']

    alfabeto = alfha + numerico + brancos + fim_arquivo + tb.operadores_separadores + ['&'] #Define o alfabeto do automato


    #Verifica se o caracter eh uma letra, numero ou outro
    def retornaValorCaracter(self, caracter):
        elemento = -1
        if caracter in self.alfha:
            elemento = tb.retornaPosicaoAlfabeto('letra')
        elif caracter in self.numerico:
            elemento = tb.retornaPosicaoAlfabeto('numero')
        else:
            elemento = tb.retornaPosicaoAlfabeto(caracter)
        return elemento

    #Faz a analise de todos os tokens e retorna o vetor de tokens contendo informando se existe erro
    def retornaVetorTokens(self, texto, vet_soma_cada_linha):
        contador_posicao_caracter = 0
        erro = False #Monitora se ha erro ou nao no lexico
        vetor_tokens = []
        tabela_transicao = tb.retornaTabelaTransicao()
        estados_finais = tb.retornaConjuntoEstadosFinais()
        estado_inicial = tb.retornaEstadoInicial()
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
        return tb.retornaIntLexama(lexema)

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
        if not vetor_tokens[0]:
            # print(a[1])
            for i in vetor_tokens[1]:
                print(i)







#Programa MAIN()
analisador_lexico = analisador_lexico()
analisador_lexico.funcaoPrincipalAnalisadorLexico('programa.txt')







