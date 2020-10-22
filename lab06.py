#####################################################################################################################################################
# MC102W - 2020 - 1º Semestre
# Aluno: André Amadeu Satorres
# RA: 231300
# Data: 27/04/2020
# Descrição: Programa que faz uma representação de uma fábrica de cajuína e imprime a situação da linha de produção da fábrica em cada instante (loop)
######################################################################################################################################################


def print_tempo(p_tempo, remessas, linha_de_prod, p_produzidas):
    """
    Função para exibir o print de cada tempo na industria
    Parâmetros:
        p_tempo: int, loop atual do programa
        remessas: a lista de cada uma das remessas inseridas
        linha_de_prod: a lista que representa a linha de produção da fabrica
        produzidas: lista que representa as quantidades de caruiras produzidas para cada remessa
    """
    print("T=" + str(p_tempo) + " | " + str(remessas) + " -> " + str(linha_de_prod) + " -> " + str(p_produzidas))


def ler_remessas(p_qtd_remessas, p_as_remessas):
    """
    Função para ler as remessas inseridas pelo usuário, uma a uma, a salvar nos indices da lista de remessas
    Parâmetros:
        p_qtd_remessas: quantidade de remessas que o usuario disse que vai inserir
        p_as_remessas: lista onde vamos armazenar cada remessa
    Retorno:
        False, se ha menos do que 2 cajus na remessa
        True, se ha mais do que dois cajus na remessa
    Print:
        Mensagem de erro se em alguma das remessas temos menos do que 2 cajus.
    """
    for a in range(int(p_qtd_remessas)):
        qtd_da_remessa = int(input())
        if qtd_da_remessa > 1:
            p_as_remessas.append(qtd_da_remessa)
        else:
            print("É necessário pelo menos dois cajus para produção de cajuína!")
            return False
    return True


def classificacao(quantidade):
    """
    Envolve descartar cajus de baixa qualidade, diminuirá em 1/3 da quantidade da remessa.
    Parâmetros:
        quantidade: int, representando a quatidade de cajus na primeira fase da linha de produção
    Retorno:
        quantidade apos a fase de classificação
    """
    return int(quantidade * (2 / 3))


def prensagem(quantidade):
    """
    Converte o caju em suco de caju. O rendimento obtido é de 2x o valor da remessa antes da prensagem se houver pelo menos 10 cajus.
    Se houver menos do que 10 cajus, então polpa de caju é adicionada a mistura, de forma que o rendimento é de 5x.
    Parâmetros:
        quantidade: int, representando a quatidade de cajus na segunda fase da linha de produção
    Retorno:
        quantidade apos a fase de prensagem
    """
    if quantidade < 10:
        return 5 * quantidade

    return quantidade * 2


def filtragem(quantidade):
    """
    Diminui a quantidade do suco obtido e é ineficiente quando há muito suco.
    Haverá a perda de 9/10 do suco se a quantidade de suco for maior do que 45 (> 45) e diminuirá 1/9 caso contrário.
    Parâmetros:
        quantidade: int, representando a quatidade de cajus na terceira fase da linha de produção
    Retorno:
        quantidade apos a fase de filtragem
    """
    if quantidade > 45:
        return int(quantidade / 10)

    return int((quantidade * 8) / 9)


def tratamento(quantidade):
    """
    Por envolver adição de água, multiplicará por 2 o valor obtido na filtração.
    Parâmetros:
        quantidade: int, representando a quatidade de cajus na ultima fase da linha de produção
    Retorno:
        quantidade apos a fase de tratamento
    """
    return quantidade * 2


def lista_vazia(lista):
    """
    Função que verifica se a lista está vazia (nesse caso, só contendo zeros)
    Parâmetros:
        lista: uma lista da qual se quer fazer as verificações
    Retorno:
        False, se a lista nao esta vazia
        True, se a lista esta vazia
    """
    for b in range(len(lista)):
        if lista[b] != 0:
            return False

    return True


qtd_remessas = input()            # representa a quantidade de remessas que serão inseridas
as_remessas = list()              # lista que armazenará a qtd de cajus de cada remessa, a ser inserida
linha_de_producao = [0, 0, 0, 0]  # lista representando a linha de produção da maquina
produzidas = list()               # lista que representa as remessas de cajuira produzidas
tempo = 0                         # variavel que controla em qual repreticao estou no momento.

if ler_remessas(qtd_remessas, as_remessas):  # so executa se ha mais de 1 caju EM TODAS as remessas
    print_tempo(tempo, as_remessas, linha_de_producao, produzidas)  # print do tempo inicial

    while not lista_vazia(as_remessas) or not lista_vazia(linha_de_producao):  # printará a situação da industria a cada tempo ate que tudo tenha sido processado

        if linha_de_producao[3] != 0:  # se tenho uma remessa saindo da linha de producao, crio mais um indice na lista de remessas produzidas
            produzidas.append(linha_de_producao[3])  # e insiro a remessa

        for i in range(4):
            if i < 3:
                linha_de_producao[3 - i] = linha_de_producao[2 - i]  # movo cada remessa para a etapa de producao posterior. Detalhe que a etapa 0 pegará o ultimo indice da lista de remessas inseridas

        if tempo < len(as_remessas):                   # se eu ainda nao processei todas as remessas inseridas
            linha_de_producao[0] = as_remessas[tempo]  # ponho mais uma das remessas no inicio da linha de producao
            as_remessas[tempo] = 0                     # zero a remessa, pois o enunciado pede para ser assim.
        elif tempo == len(as_remessas):                # se eu terminei de ler as remessas inseridas, mas ainda estou processando a linha de producao
            linha_de_producao[0] = 0                   # ja posso colocar zero no inicio da linha de producao. Com isso, com o tempo vou zerando todo o resto da lista, pois receberão multiplos de zero (0)

        #  Aqui é para realizar as etapas da linha de produção
        linha_de_producao[0] = classificacao(linha_de_producao[0])   # Classificacao para o que esta no inicio da linha
        linha_de_producao[1] = prensagem(linha_de_producao[1])       # Prensagem para o que esta na segunda etapa
        linha_de_producao[2] = filtragem(linha_de_producao[2])       # Filtragem para o que esta na terceira etapa
        linha_de_producao[3] = tratamento(linha_de_producao[3])      # Tratamento para o que esta na ultima etapa

        tempo += 1  # Incremento a variavel de controle que uso neste loop

        print_tempo(tempo, as_remessas, linha_de_producao, produzidas)  # Imprimo a situacao atual da industria