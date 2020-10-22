###########################################################################################################################
# MC102W - 2020 - 1º Semestre
# Aluno: André Amadeu Satorres
# RA: 231300
# Data: 24/05/2020
# Descrição: Programa que simula o Respondenator 3000: Encontrar a resposta mais adequada dada uma pergunta e n respostas
###########################################################################################################################

from PontStop import *


def processamento_do_texto(texto, sinonimos):
    tokens = texto.lower().split(" ")  # padronizacao e tokenizacao

    # Retirar as stop words
    tokens = [''.join(char for char in token if char not in pontuacoes) for token in tokens if token.strip() != ""]

    palavras = [token for token in tokens if token not in stop_words]  # limpeza

    # reescrita (usar os sinonimos)
    for i in range(len(palavras)):
        for chave, valor in sinonimos.items():
            if palavras[i] in valor:  # ve se eh uma palavra que tem que ser trocada
                palavras[i] = chave  # se achar substitui ela

    return sorted(set([x for x in palavras]))  # representacao. Cast para set para retirar as duplicadas


def main():
    abre_chaves = input().strip()  # ler o {

    if abre_chaves != "{":  # entrada invalida
        return

    sinonimos = {}  # criar o dicionario

    linha = input().strip()

    while linha != "}":
        representacao, sinon = linha.split(":")
        sinonimos[representacao] = sinon.split(",")  # armazenar as substituicoes a serem feitas

        linha = input().strip()  # vai lendo cada sinonimo-palavras

    pergunta = input().strip()

    pergunta_formatada = processamento_do_texto(pergunta, sinonimos)  # formata a pergunta segunindo os passos

    qtd_respostas = int(input().strip())

    respostas = tuple(input() for x in range(qtd_respostas))  # tupla de strings de resposta

    # formatar cada resposta da tupla de acordo com os passos
    respostas_formatadas = tuple(processamento_do_texto(resposta, sinonimos) for resposta in respostas)

    print("Descritor pergunta: {chaves}".format(chaves=",".join(pergunta_formatada)))

    for i in range(len(respostas_formatadas)):
        print("Descritor resposta {i}: {chaves}".format(i=i + 1, chaves=",".join(respostas_formatadas[i])))

    print()  # uma linha em branco entre os descritores e a resposta final
    resposta_certa = "42"  # caso nao ache nenhuma que é subconjunto dos tokens da pergunta

    # Procurar a resposta para a pergunta
    for j in range(len(respostas_formatadas)):
        if set(pergunta_formatada).issubset(set(respostas_formatadas[j])):  # cast para set para usar a funcao issubset
            resposta_certa = respostas[j]
            break

    print('A resposta para a pergunta "{pergunta}" é "{resp}"'.format(pergunta=pergunta, resp=resposta_certa))


main()
