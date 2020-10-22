#################################################################################################################################################################
# MC102W - 2020 - 1º Semestre
# Aluno: André Amadeu Satorres
# RA: 231300
# Data: 02/07/2020
# Descrição: Programa que implementa um programa que retorna o impacto de uma Fake News através de um relatórios de quem recebeu fake news (ordenado pelo nome).
#################################################################################################################################################################


# Função recursiva para criar e retornar a lista de usuarios atingidos por uma fake news
def atingidos_por_fake_news(pessoas, compartilhador):
    # Avaliar um caso base --> não compartilhou com ninguem
    if pessoas[compartilhador][0] == 0:  # Entao ele nao compartilhou na FN com ninguem (fluxo acaba nele)
        return [compartilhador]  # retorno uma lista só com o compartilhador

    atingidos = [compartilhador]  # vai armazenar todos os atingidos a partir de um usuario especifico

    # Se chegou aqui então é gerador ou compartilhador (pessoas[compartilhador][0] == 1 ou 2)
    for i in range(len(pessoas[compartilhador][1])):  # percorrer lista de amigos dele
        # obter a lista de usuarios atingidos a partir do usuario atual
        for pessoa in atingidos_por_fake_news(pessoas, pessoas[compartilhador][1][i]):
            atingidos.append(pessoa)  # adiciono os atingidos a partir do usuario atual

    return atingidos  # retorno a lista com todos os atingidos a partir de um usuario especifico


pessoas = {}
gerador_da_fn = None  # armazenar o gerador da noticia falsa (de onde partiu)

# Ler entrada = Guardar cada pessoa inserida
for i in range(int(input())):
    info = input().strip().split()  # info[0] = n compartilhou/gerador/compartilhou, info[1] = nome, info[2:] = amigos
    pessoas[info[1]] = int(info[0]), info[2:]  # armazenar os dados

    if int(info[0]) == 1:  # geradora de fake news
        gerador_da_fn = info[1]  # saber de onde comecar o fluxo

if gerador_da_fn is not None:  # apenas por garantia
    # Criar a lista dos atingidos pela fake news e ordenar por nome
    atingidos = sorted(set(atingidos_por_fake_news(pessoas, gerador_da_fn)))  # converto para set para retirar duplicados

    print("Ordenação por nome")

    # Saida = printar cada usuario
    for k in range(len(atingidos)):
        print(atingidos[k])
