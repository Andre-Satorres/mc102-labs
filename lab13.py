#######################################################################################################################
# MC102W - 2020 - 1º Semestre
# Aluno: André Amadeu Satorres
# RA: 231300
# Data: 09/06/2020
# Descrição: Programa que simula o jogo "Onde está Carmen Sandiego?", numa versão console.
#######################################################################################################################


class Pais:
    def __init__(self, nome, pistas):
        self.nome = nome
        self.pistas = pistas

    def __str__(self):
        return "Pais({}: {})".format(self.nome, self.pistas)


def encontrar_carmen(pais_atual, possibilidades: list):
    resposta = achar_destino(pais_atual, possibilidades, 0)

    # resposta[0] sera um pais ou "carmen" se cheguei aqui
    if resposta[0] == "carmen":
        print("Descobri com", resposta[1], "pistas que Carmen Sandiego está no país")
        return

    print("Descobri com", resposta[1], "pistas que devo viajar para", resposta[0].nome)

    encontrar_carmen(resposta[0], possibilidades)


def eh_anagrama(palavra, outra):
    for letra in palavra:
        if letra not in outra:
            return False
        outra = outra.replace(letra, '', 1)  # para se caso 'palavra' tenha 2 letras iguais eu ter certeza que 'outra' tambem tem

    return True


def achar_destino(pais_atual: Pais, possibilidades: list, indice):
    if len(possibilidades) == 1:
        return [possibilidades[0], indice]  # possibilidades[0] é o pais destino ou é "carmen". Retorno o indice pra usar no print

    pistas_atuais = "".join(pais_atual.pistas[:indice+1])
    possibilidades_novas = []

    for possibilidade in possibilidades:
        if not isinstance(possibilidade, Pais):  # se a possibilidade é um Pais, eu comparo pelo pais.nome, senao, comparo pelo proprio valor de 'possibilidade'
            if eh_anagrama(pistas_atuais, possibilidade):
                if (indice < 2) or (indice == 2 and len(possibilidade) == len(pistas_atuais)):
                    possibilidades_novas.append(possibilidade)  # adiciona se a possibilidade é anagrama de carmen ou das pistas do pais ate o indice atual
        elif eh_anagrama(pistas_atuais, possibilidade.nome):
            if (indice < 2) or (indice == 2 and len(possibilidade.nome) == len(pistas_atuais)):
                possibilidades_novas.append(possibilidade)

    # chamo recursivamente, agora pegando mais pistas para elimitar mais possibilidades
    return achar_destino(pais_atual, possibilidades_novas, indice + 1)


def main():
    nome_pais_atual = input().strip()
    paises = []
    pais_atual = None

    while True:
        pais_e_pistas = input().strip().split(":")  # ler cada pais da entrada e as pistas

        if len(pais_e_pistas) < 2:  # entrada invalida ou é o X --> terminou
            break

        pistas = pais_e_pistas[1].split(",")  # separa as 3 pistas em uma lista
        pais = Pais(pais_e_pistas[0], pistas)

        if pais_e_pistas[0] == nome_pais_atual:
            pais_atual = pais  # guardo em qual pais da lista devo começar a busca

        paises.append(pais)

    print("Iniciando as buscas em {}".format(pais_atual.nome))

    possibilidades = []
    possibilidades.extend(paises)
    possibilidades.append("carmen")

    encontrar_carmen(pais_atual, possibilidades)  # recursivamente vai passar pelos paises ate achar onde está carmen


main()
