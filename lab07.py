########################################################################################################################################################
# MC102W - 2020 - 1º Semestre
# Aluno: André Amadeu Satorres
# RA: 231300
# Data: 05/05/2020
# Descrição: Programa que simula uma Guerra Virtual entre duas comunidades rivais, Snowland e Sunny Kingdom, cada qual escolhendo seu heroi para batalha.
#########################################################################################################################################################


#  Bloco: Criando constantes de texto e inserindo-as numa lista, para uma manipulação mais fácil
CARTA_CURA, CARTA_FORCA, CARTA_PROTECAO, CARTA_ETER, CARTA_DRENAGEM, CARTA_INSANO, CARTA_ESTRELA = 'C', 'F', 'P', 'E', 'D', 'I', 'S'
tipos_cartas = [CARTA_CURA, CARTA_FORCA, CARTA_PROTECAO, CARTA_ETER, CARTA_DRENAGEM, CARTA_INSANO, CARTA_ESTRELA]
nomes_cartas = ["Cura", "Força", "Proteção", "Éter", "Drenagem", "Insano", "Estrela"]
# sei que o mesmo indice de 'C' em tipos_cartas sera o de 'Cura' em nomes_cartas, por exemplo


class Heroi:
    """
    A classe Heroi representa um heroi de batalha escolhido por um reino.
    Cada heroi possui atributos de vida, mana, dano, bloqueio, nome e seu respectivo reino
    Essa classe também controla os ataques e defesas de cada herói, assim como o uso de suas
    cartas mágicas.
    """

    def __init__(self, nome, max_vida, dano, bloqueio, max_mana, reino):
        self.nome = nome
        self.max_vida = max_vida
        self.dano = dano
        self.bloqueio = bloqueio
        self.max_mana = max_mana
        self.reino = reino
        self.mana = max_mana
        self.vida = max_vida
        self.cartas = []  # armazenará somente as cartas de ativacao e passivas (as que ficam guardadas)

    def __str__(self):
        return "{nome} possui {vida} de vida, {mana} pontos mágicos, {dano} de dano e {bloqueio}% de bloqueio".format(nome=self.nome,
                                                                                                                      vida=self.vida,
                                                                                                                      mana=self.mana,
                                                                                                                      dano=self.dano,
                                                                                                                      bloqueio=self.bloqueio)

    # Procura e remove uma carta da lista, dada o seu tipo, dado que nunca pode haver duas cartas do mesmo tipo no inventário
    def remover_carta(self, tipo):
        for carta in self.cartas:
            if carta.tipo == tipo:
                self.cartas.remove(carta)

    # Procura e devolve uma carta do tipo fornecido
    def get_carta(self, tipo):
        for carta in self.cartas:
            if carta.tipo == tipo:
                return carta

    # Verifica se uma carta esta com seu poder ativado
    def carta_esta_ativada(self, tipo):
        carta = self.get_carta(tipo)
        if carta is None:
            return False

        if not carta.ativada:
            return False

        return True

    def atacar(self, outro_guerreiro):

        # Bloco: verificar se devo realizar um ataque insano
        carta_insano = self.get_carta(CARTA_INSANO)
        if self.carta_esta_ativada(CARTA_INSANO):
            print("{nome_heroi} deu um ataque insano em {outro_heroi}".format(nome_heroi=self.nome,
                                                                              outro_heroi=outro_guerreiro.nome))
            carta_insano.n -= 1  # diminuo a qtd de atks insanos disponiveis
            outro_guerreiro.defender(self.dano + carta_insano.pontos)  # ja chamo o metodo de defesa do outro heroi
        else:
            print("{nome_heroi} atacou {outro_heroi}".format(nome_heroi=self.nome,
                                                             outro_heroi=outro_guerreiro.nome))
            outro_guerreiro.defender(self.dano)

        # Bloco: Utilizar carta de drenagem no outro
        carta_drenagem = self.get_carta(CARTA_DRENAGEM)  # reduzo a mana independente se ele estava invulnerável
        if carta_drenagem is not None:  # ele possui a carta de drenagem
            outro_guerreiro.mana -= carta_drenagem.pontos

            if outro_guerreiro.mana < 0:  # garantir q continuara 0
                outro_guerreiro.mana = 0

        if self.carta_esta_ativada(CARTA_INSANO) and carta_insano.n <= 0:  # acabou os ataques insanos disponiveis
            self.remover_carta(CARTA_INSANO)  # removo a carta de INSANO somente qd acabarem os ataques insanos dele

    def defender(self, dano):
        # Bloco: verificar se tem carta estrela
        carta_estrela = self.get_carta(CARTA_ESTRELA)
        if self.carta_esta_ativada(CARTA_ESTRELA):
            carta_estrela.n -= 1  # reduzo a qtd de usos disponiveis
            print("{nome_heroi} estava invulnerável".format(nome_heroi=self.nome))

            if carta_estrela.n <= 0:  # aqui dentro para eu so remover uma vez
                self.remover_carta(CARTA_ESTRELA)
            return

        #  nao tinha carta estrela ativada
        dano_bloqueado = int((dano * self.bloqueio) / 100)
        self.vida -= dano - dano_bloqueado
        if self.vida < 0:  # Garantir que nao sera menor que zero
            self.vida = 0

    def tem_mana_suficiente(self, carta):
        return self.mana >= carta.custo

    def encontrar_carta(self, carta_magica):
        if self.get_carta(carta_magica.tipo) is not None:  # ja tenho essa carta
            print("{nome_heroi} já possui a carta {carta}".format(nome_heroi=self.nome,
                                                                  carta=nomes_cartas[tipos_cartas.index(carta_magica.tipo)]))

        # nao tenho a carta ainda
        elif carta_magica.tipo in [CARTA_DRENAGEM, CARTA_ESTRELA, CARTA_INSANO]:  # so armazeno ativacao e passivas
            self.cartas.append(carta_magica)

        elif carta_magica.tipo in [CARTA_CURA, CARTA_FORCA, CARTA_PROTECAO, CARTA_ETER]:  # uso imediato
            if not self.tem_mana_suficiente(carta_magica):
                print("{nome_heroi} não possui mana suficiente para a mágica".format(nome_heroi=self.nome))
            else:
                self.usar_carta(carta_magica)  # se nao for carta de ativacao eu ja tenho que usar

    def ativar_carta(self, tipo):
        carta = self.get_carta(tipo)
        if carta is None:  # tentou ativar uma carta q ele n tem
            print("{nome_heroi} não possui a carta {carta}".format(nome_heroi=self.nome,
                                                                   carta=nomes_cartas[tipos_cartas.index(tipo)]))

        # tem a carta
        elif carta.ativada:  # ja foi ativada
            print("{nome_heroi} já ativou a carta {carta}".format(nome_heroi=self.nome,
                                                                  carta=nomes_cartas[tipos_cartas.index(carta.tipo)]))

        # tem a carta e nao foi ativada
        elif not self.tem_mana_suficiente(carta):  # nao tem mana suficiente para ativar
            print("{nome_heroi} não possui mana suficiente para a mágica".format(nome_heroi=self.nome))

        # tem a carta, não foi ativada e tem mana suficiente
        else:
            carta.ativada = True  # ativo a carta
            self.mana -= carta.custo
            print("{nome_heroi} ativou a carta {carta}".format(nome_heroi=self.nome,
                                                               carta=nomes_cartas[tipos_cartas.index(carta.tipo)]))

            if carta.n <= 0:  # descartar
                self.remover_carta(carta.tipo)

    def usar_carta(self, carta):
        if carta.tipo == CARTA_CURA:
            return self.usar_carta_cura(carta)
        elif carta.tipo == CARTA_FORCA:
            return self.usar_carta_forca(carta)
        elif carta.tipo == CARTA_PROTECAO:
            return self.usar_carta_protecao(carta)
        elif carta.tipo == CARTA_ETER:
            return self.usar_carta_eter(carta)

    def usar_carta_cura(self, carta):
        self.mana -= carta.custo
        self.vida += carta.pontos

        if self.vida < 0:  # so por seguranca..
            self.vida = 0

        if self.vida > self.max_vida:
            self.vida = self.max_vida

    def usar_carta_forca(self, carta):
        self.mana -= carta.custo
        self.dano += carta.pontos

        if self.dano < 0:  # so por seguranca ...
            self.dano = 0

    def usar_carta_protecao(self, carta):
        self.mana -= carta.custo
        self.bloqueio += carta.pontos

        if self.bloqueio < 0:  # so por seguranca...
            self.bloqueio = 0

        if self.bloqueio > 100:  # nao pode exceder 100
            self.bloqueio = 100

    def usar_carta_eter(self, carta):
        self.mana += carta.pontos

        if self.mana < 0:  # so por seguranca, novamente ...
            self.mana = 0

        if self.mana > self.max_mana:
            self.mana = self.max_mana


class CartaMagica:
    """
    A classe CartaMagica representa uma Carta Magica que pode ser utilizada pelos heróis, em batalha.
    Só possui seus atributos e um construtor.
    """
    def __init__(self, tipo, custo, pontos):
        self.tipo = tipo
        self.custo = custo
        self.pontos = pontos


class CartaAtivacao(CartaMagica):
    """
    A classe CartaAtivacao é subclasse de CartaMagica. Ela representa as cartas de ativacao do jogo.
    Por isso, possui dois atributos a mais, especificando se ja foi ativada ou não, e quantos usos ainda tem.
    """
    def __init__(self, tipo, custo, pontos, n=0):
        super().__init__(tipo, custo, pontos)
        self.ativada = False
        self.n = n


#  Metodo para verificar se o heroi achou uma carta
def heroi_achou_carta(representacao, heroi_atual):
    if representacao[1] == 'X':  # n achou carta
        print("{nome_heroi} não encontrou nenhuma carta".format(nome_heroi=heroi_atual.nome))
        return

    print("{nome_heroi} encontrou a carta {carta}".format(nome_heroi=heroi_atual.nome,
                                                          carta=nomes_cartas[tipos_cartas.index(representacao[1])]))

    if representacao[1] in [CARTA_CURA, CARTA_FORCA, CARTA_PROTECAO]:  # 3 parametros (tipo, custo, pontos)
        heroi_atual.encontrar_carta(CartaMagica(representacao[1],
                                                int(representacao[2]),
                                                int(representacao[3])))

    elif representacao[1] in [CARTA_ETER, CARTA_DRENAGEM]:  # 2 parametros (tipo, custo = 0, pontos)
        heroi_atual.encontrar_carta(CartaMagica(representacao[1],
                                                0,
                                                int(representacao[2])))

    elif representacao[1] == CARTA_INSANO:  # 4 parametros: vem (tipo, custo, n, pontos), mas fica (tipo, custo, pontos, n)
        heroi_atual.encontrar_carta(CartaAtivacao(representacao[1],
                                                  int(representacao[2]),
                                                  int(representacao[4]),
                                                  int(representacao[3])))

    elif representacao[1] == CARTA_ESTRELA:  # 3 parametros: vem (tipo, custo, n) mas fica (tipo, custo, 0, n)
        heroi_atual.encontrar_carta(CartaAtivacao(representacao[1],
                                                  int(representacao[2]),
                                                  0,
                                                  int(representacao[3])))


rodada_atual = 1
primeiro_a_jogar = None
ja_atacou = True
nova_rodada = True
procurou_carta = False


def sit_atual(heroi1, heroi2):
    # Printar o status de cada heroi
    print(heroi1)
    print(heroi2)


# Metodo para ler uma acao digitada no console
def ler_acao(heroi1, heroi2, heroi_atual):
    global rodada_atual, primeiro_a_jogar, ja_atacou, nova_rodada, procurou_carta
    acao = input().strip().split(" ")

    if acao[0] == 'H' and ja_atacou:  # nao deixo trocar de heroi se ainda nao atacou
        if acao[1] == '1' and heroi_atual != heroi1:  # so mudo para o heroi1 se a jogada anterior foi do 2
            heroi_atual = heroi1

        elif acao[1] == '2' and heroi_atual != heroi2:  # so mudo para o heroi2 se a jogada anterior foi do 1
            heroi_atual = heroi2

        else:  # nao mudei o heroi. Ja era a vez do 1 e digitaram o 1 de novo
            if not nova_rodada:  # pq se for igual de uma rodada pra outra td bem
                return heroi_atual  # so saio e nao faco nada, vai ter q digitar ne novo

        if nova_rodada:
            primeiro_a_jogar = heroi_atual
            nova_rodada = False
        else:
            nova_rodada = True

        procurou_carta = False  # acabei de mudar de heroi, entao ele ainda nao fez nenhuma acao
        ja_atacou = False
        print("Rodada {rodada}: vez de {nome_heroi}".format(rodada=rodada_atual,
                                                            nome_heroi=heroi_atual.nome))

    elif acao[0] == 'M' and not procurou_carta and not ja_atacou:  # eh uma carta, e ainda n procurou
        procurou_carta = True
        heroi_achou_carta(acao, heroi_atual)  # "acao" sera a descricao da carta

    elif acao[0] == 'A' and procurou_carta and not ja_atacou:  # ataque
        ja_atacou = True
        if heroi_atual == heroi1:
            heroi_atual.atacar(heroi2)
        else:
            heroi_atual.atacar(heroi1)

        if primeiro_a_jogar != heroi_atual:  # So incremento a rodada atual e printo o status se o 2º da rodada q jogou
            rodada_atual += 1
            sit_atual(heroi1, heroi2)

    # se caiu aqui, eh pq ativou uma carta de ativação (ou fez outra coisa aleatoria/nao prevista)
    elif acao[0] in [CARTA_INSANO, CARTA_ESTRELA] and not ja_atacou and procurou_carta:
        heroi_atual.ativar_carta(acao[0])

    return heroi_atual  # Para eu poder controlar quem acabou de jogar


def terminar(heroi_vencedor, heroi1, heroi2):
    print("O herói {nome_heroi} do reino {reino} venceu o duelo".format(nome_heroi=heroi_vencedor.nome,
                                                                        reino=heroi_vencedor.reino))
    sit_atual(heroi1, heroi2)


def ler_heroi(reino):
    nome = input()
    max_vida = int(input())
    dano = int(input())
    bloqueio = int(input())
    max_mana = int(input())
    return Heroi(nome, max_vida, dano, bloqueio, max_mana, reino)


def main():
    global primeiro_a_jogar
    heroi1 = ler_heroi("Snowland")
    print("O reino {reino} indicou o herói {nome_heroi}".format(reino=heroi1.reino,
                                                                nome_heroi=heroi1.nome))

    heroi2 = ler_heroi("Sunny Kingdom")
    print("O reino {reino} indicou o herói {nome_heroi}".format(reino=heroi2.reino,
                                                                nome_heroi=heroi2.nome))

    heroi_atual = heroi1

    primeiro_a_jogar = ler_acao(heroi1, heroi2, heroi_atual)  # para que eu printe a situacao atual na hora certa
    heroi_atual = primeiro_a_jogar

    while heroi1.vida > 0 and heroi2.vida > 0:
        heroi_atual = ler_acao(heroi1, heroi2, heroi_atual)  # fica lendo as entradas

    if heroi2.vida == 0:  # heroi 1 venceu
        terminar(heroi1, heroi1, heroi2)
    else:
        terminar(heroi2, heroi1, heroi2)  # heroi 2 venceu


main()
