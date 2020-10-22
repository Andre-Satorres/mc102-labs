#######################################################################################################################
# MC102W - 2020 - 1º Semestre
# Aluno: André Amadeu Satorres
# RA: 231300
# Data: 09/06/2020
# Descrição: Programa que  implementa um único turno do jogo de um jogador fixo (bot do turno) do jogo "Duvido".
#######################################################################################################################


class Valores:
    valores = tuple('A 2 3 4 5 6 7 8 9 10 J Q K'.split())  # para facilitar o acesso

    @staticmethod
    def comparar(v1, v2):
        if v1 == v2:
            return 0

        if Valores.valores.index(v1) > Valores.valores.index(v2):  # o valor das cartas é correspondente a sua posicao
            return 1

        return -1


class Carta:
    def __init__(self, valor, naipe):
        self.valor = valor
        self.naipe = naipe

    def __str__(self):
        return self.valor + self.naipe  # formatacao de saida necessaria

    def __eq__(self, other):  # ve se duas cartas sao iguais simplesmemte ao se utilizar o operator ==.
        if not isinstance(other, Carta):  # se o segundo objeto nao é uma carta, entao nao sao iguais
            return False

        if self.naipe != other.naipe:
            return False

        if self.valor != other.valor:
            return False

        return True

    def __ne__(self, other):  # ve se duas cartas sao diferentes simplesmemte ao se utilizar o operator !=.
        if not isinstance(other, Carta):
            return True

        if self.naipe != other.naipe:
            return True

        if self.valor != other.valor:
            return True

        return False

    def __gt__(self, other):  # (greater) compara duas cartas simplesmemte ao se utilizar o operator >.
        if not isinstance(other, Carta):
            return super().__gt__(self, other)

        comp = Valores.comparar(self.valor, other.valor)

        if comp < 0:  # entao self.valor < other.valor
            return False
        elif comp > 0:
            return True

        if self.naipe <= other.naipe:
            return False

        return True

    def __ge__(self, other):  # (greater equals) compara duas cartas simplesmemte ao se utilizar o operator >=.
        if not isinstance(other, Carta):
            return super().__ge__(self, other)

        comp = Valores.comparar(self.valor, other.valor)

        if comp < 0:  # entao self.valor < other.valor
            return False
        elif comp > 0:
            return True

        if self.naipe < other.naipe:
            return False

        return True

    def __lt__(self, other):  # (lower) compara duas cartas simplesmemte ao se utilizar o operator <.
        if not isinstance(other, Carta):
            return super().__lt__(self, other)

        comp = Valores.comparar(self.valor, other.valor)

        if comp > 0:  # entao self.valor > other.valor
            return False
        elif comp < 0:
            return True

        if self.naipe >= other.naipe:  # >= pois essa funcao eh para checar estritamente <
            return False

        return True

    def __le__(self, other):  # (lower equals) compara duas cartas simplesmemte ao se utilizar o operator <=.
        if not isinstance(other, Carta):
            return super().__le__(self, other)

        comp = Valores.comparar(self.valor, other.valor)

        if comp > 0:  # entao self.valor > other.valor
            return False
        elif comp < 0:
            return True

        if self.naipe > other.naipe:
            return False

        return True


class Jogador:
    def __init__(self):
        self.cartas = []  # armazena as cartas da mao no jogador

    def busca_valor(self, valor):
        inicio = 0
        fim = len(self.cartas) - 1

        while inicio <= fim:  # busca binaria na lista para eu saber se o jogador possui o valor x
            meio = (inicio + fim) // 2

            if self.cartas[meio].valor == valor:  # possui o valor x
                return meio

            elif Valores.comparar(self.cartas[meio].valor, valor) > 0:
                fim = meio - 1

            else:
                inicio = meio + 1

        return -1  # caso ele nao possua o valor

    def descartar(self, cartas):
        for carta in cartas:
            self.cartas.remove(carta)

    def ordenar(self):
        for i in range(1, len(self.cartas)):  # ordenacao simples por insertion sort
            aux = self.cartas[i]
            j = i

            while j > 0 and self.cartas[j - 1] > aux:
                self.cartas[j] = self.cartas[j - 1]  # deslocar para a direita
                j -= 1

            self.cartas[j] = aux  # faço a inserção no local certo

    def obter_todas_com_valor(self, valor):
        pos = self.busca_valor(valor)  # posicao de uma carta com o valor procurado
        cartas_com_valor = []

        if pos < 0:  # nao achei
            return cartas_com_valor  # vazia

        # achei a posicao --> outras cartas com o mesmo valor serao adjacentes

        i = pos
        while i >= 0 and self.cartas[i].valor == valor:  # andar ate a menor com esse valor
            i -= 1

        i += 1  # somo antes, pois parei numa com valor menor ou na posicao -1

        while i < len(self.cartas) and self.cartas[i].valor == valor:  # inserir uma a uma em ordem crescente
            cartas_com_valor.append(self.cartas[i])
            i += 1

        return cartas_com_valor  # retorno uma lista com todas as cartas que o jogador tem com o valor procurado


def main():
    bot = Jogador()
    mao = input().strip().split()

    # Criar as cartas da mao do bot
    for carta in mao:
        bot.cartas.append(Carta(carta[:-1], carta[-1]))  # vou inserindo cada carta

    # Leitura das cartas despejadas na mesa
    mesa = [Carta(x[:-1], x[-1]) for x in input().strip().split()]

    valor_atual = input().strip()  # valor atual da rodada

    duvidou = input().strip()  # representa se o bot adversario duvidou ou nao da jogada do nosso bot

    if bot.busca_valor(valor_atual) >= 0:  # porque busca_valor retornara -1 se, e somente se, nao tem o valor na lista):
        blefando = False  # se ele possui o valor da rodada, ele irá jogá-lo, e, portanto, nao estara blefando
    else:
        blefando = True  # caso contrario jogara o menor valor q tem em maos e estara, por tanto, blefando
        valor_atual = bot.cartas[0].valor  # o valor a descartar vai ser o menor em maos

    jogada = bot.obter_todas_com_valor(valor_atual)  # obter a lista de todas as cartas a serem descartadas

    bot.descartar(jogada)  # remove da lista de cartas do bot cada carta da jogada dele

    for carta in jogada:
        mesa.append(carta)  # e adiciona elas na mesa

    print("Jogada: {}".format(" ".join(str(carta) for carta in jogada)))

    if duvidou == "S":
        print("Um bot adversário duvidou")

        if blefando:
            print("O bot estava blefando")
            bot.cartas.extend(mesa)  # entao o bot tera q comprar toda a mesa
            bot.ordenar()  # para ficar na ordem desejada
        else:
            print("O bot não estava blefando")  # o outro bot que teria que comprar tudo, mas nao programamos isso

        mesa.clear()  # o nosso bot ou o bot que duvidou vai pegar todas as cartas da mesa
    else:
        print("Nenhum bot duvidou")

    print("Mão: {}".format(" ".join(str(carta) for carta in bot.cartas)))

    print("Pilha: {}".format(" ".join(str(carta) for carta in mesa)))

    if len(bot.cartas) == 0:  # o bot venceu se está sem cartas na mao:
        print("O bot venceu o jogo")


main()
