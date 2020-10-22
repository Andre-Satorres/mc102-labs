#  Feito por André Amadeu Satorres - 231300
#  Este laboratório consiste num programa que gera um código CRC de N-1 bits (sendo N a quantidade de bits de um
#  polinômio inserido na entrada) para uma mensagem de M bits. Ou seja, dada uma entrada composta por uma mensagem e um
#  polinômio, o programa deve gerar o código CRC correspondente.
#  ---------------------------------------------------------------------------------------------------------------------

#  INÍCIO DO PROGRAMA

#  Esta variavel representa a mensagem a ser digitada (em binario)
mensagem = list(input())

#  Esta variavel representa o polinomio a ser inserido
polinomio = list(input())

#  A quantidade de bits do codigo CRC sera n-1 bits, sendo N a quantidade de bits do polinômio inserido na entrada (enunciado)
qtdBitsCRC = len(polinomio) - 1

#  Salvo o length antigo da mensagem para usar posteriormente
lenAntiga = len(mensagem)

#  Nesse bloco vou verificar o quao maior o polinomio é em relação à mensagem (quantos zeros à direita terei que inserir na mensagem para poder fazer o xor bit a bit posteriormente)
if len(mensagem) < len(polinomio):
    diferenca = len(polinomio) - len(mensagem)
#  Se a mensagem é maior ou igual em tamanho, não preciso inserir zeros
else:
    diferenca = 0

#  Detalhe: nao "complemento" o polinomio caso ele for menor, pois já verificarei isso no loop!

#  Aqui insiro os zeros. Estou inserindo junto com os zeros para "completar a mensagem" (difereça), tambem os bits do CRC
for i in range(qtdBitsCRC + diferenca):
    mensagem.append('0')

#  Percorrer a mensagem para fazer os xors (aqui o uso da lenAntiga: preciso percorrer so a quantidade de indices que eu tinha antes, sem os zeros adicionais e os indices do CRC)
for i in range(lenAntiga):
    #  não devo comparar se o indice for zero
    if mensagem[i] != '0':
        #  fazer um xor para cada bit a partir do indice atual da mensagem (bit atual)
        for k in range(i, len(mensagem)):
            #  só checando se nao vai ter out of range (como eu avisei em "detalhe")
            if k < len(polinomio) and k < len(mensagem):
                mensagem[k] = str(int(mensagem[k] != polinomio[k]))
                #  xor bit a bit:
                #  ==> bits diferentes -> 1
                #  ==> bits iguais     -> 0
                #  se mensagem[k] != polinomio[k] a condicao retorna 1 (TRUE), que é o esperado para um xor entre 2 bits diferentes
                #  se mensagem[k] == polinomio[k] a condicao retorna 0 (FALSE), que é o esperado para um xor entre 2 bits iguais
                #  mas o python retorna 'True' e 'False' com essas condiçoes. Simples, basta fazer um cast para int, e, depois para
                #  string novamente (pois tenho uma lista de strings!)

    #  BLOCO: DESLOCAR O POLINOMIO PARA A DIREITA

    polinomio.append('0')  # append para poder mover tudo para a direita sem dar out of range

    #  Loop reverso
    for j in range(len(polinomio)-1, 0, -1):
        polinomio[j] = polinomio[j - 1]
    #  Basicamente, estou pegando o indice n + 1, que acabei de criar com um "append('0')" e pondo o que esta no indice n
    #  Em seguida, estou pondo o que esta no indice n - 1 no indice n
    #  E assim, sucessivamente, até pegar o conteudo do indice 0 e colocar no indice 1
    #  Esse foi o algoritmo que encontrei, porque, se eu fizesse na ordem crescente, eu perderia o indice superior
    #  Ex: se eu pegasse o conteudo do indice 1 e colocasse no indice 2, eu perderia o conteudo do indice 2 (a nao ser que criasse uma variavel para isso (mais tempo e memoria à toa))
    #  Daí você se pergunta: e o primeiro indice? Ah, basicamente ele é um lixo agora :(... como 'i' vai incrementar nem vou comparar mais com tal posicao
    #  Na verdade, vai ter sido basicamente um "deslocar para a direita" de algum modo.

    #  FIM DO BLOCO DE DESLOCAMENTO

#  BLOCO: PRINTAR O CODIGO CRC

#  Criando a variavel de saida para printar os dados (crio antes para poder usar no loop concatenando-a)
saida = ""

#  Obviamente, devo construir uma saida com o mesmo numero de caracteres que o CRC
for i in range(qtdBitsCRC):
    saida += mensagem[i + lenAntiga]
    #  Aqui, mais um uso da lenAntiga, pois, pulo direto para os indices do CRC

#  Exibindo a saida
print(saida)

#  FIM DO BLOCO DE PRINTAR CRC

#  FIM DO PROGRAMA