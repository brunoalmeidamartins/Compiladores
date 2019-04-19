class analisador_lexico():
    '''
    Definicao dos vetores
    '''
    alfha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
             'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '_']
    numerico = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    brancos = [' ', '\n', '\t', '\r', '\f']

    fim_arquivo = 'eof'

    palavras_reservadas = ['abstract', 'assert', 'boolean', 'break', 'byte', 'case', 'catch', 'char', 'class', 'const',
                            'continue', 'default', 'do', 'double', 'else', 'enum', 'extends', 'final', 'finally', 'float',
                            'for', 'if', 'goto', 'implements', 'import', 'instanceof', 'int', 'interface', 'long', 'native',
                            'new', 'package', 'private', 'protected', 'public', 'return', 'short', 'static', 'strictfp',
                            'super', 'switch', 'synchronized', 'this', 'throw', 'throws', 'transient', 'try', 'void',
                            'volatile', 'while', 'main', 'String', 'length', 'System.out.println']

    def imprimeDefCaracteres(self, texto):
        for linha in texto:
            for caracter in linha:
                if caracter in self.alfha:
                    print(caracter + ':alfha')
                elif caracter in self.numerico:
                    print(caracter + ':numero')
                elif caracter in self.brancos:
                    print(caracter + ":Espaco em branco")
                elif caracter == self.fim_arquivo:
                    print(caracter + ":Fim de arquivo")
                else:
                    print(caracter + ':ERROR!!!')
                #print(caracter.isalpha())
    def analisa_token(self, ch):
        pass
    def obtenToken(self, linha, numero_linha):
        token = ''
        vetor_token = []
        count = 0
        for ch in linha:
            self.analisa_token(ch)
            '''
            if count == 0:
                if ch in self.alfha:
                    token = token + ch
                    count = count + 1
                elif ch in self.numerico:
                    token = token + ch
                    count = count + 1
                else:
                    print("Chama rotina de tratamento")
            elif count != 0 and ((ch in self.alfha or ch in self.numerico)):
                token = token + ch
                count = count + 1
            else:
            '''


#Programa MAIN()

lexico = analisador_lexico()

arq = open('programa.txt', 'r')
texto = arq.readlines()
arq.close()



print(texto[0])

#lexico.imprimeDefCaracteres(texto)
for i in range(0, len(texto)):
    lexico.obtenToken(texto[i], i + 1)

