########################################################################################################################################################
# MC102W - 2020 - 1º Semestre
# Aluno: André Amadeu Satorres
# RA: 231300
# Data: 13/05/2020
# Descrição: Programa que simula o Jogo da Vida, criado por John Horton Conway, numa versão em console.
#########################################################################################################################################################


class Tabuleiro:
    def __init__(self, linhas, colunas):
        self.matriz = []
        self.inicializar_celulas(linhas, colunas)
        self.qtd_linhas = linhas
        self.qtd_colunas = colunas

    def inicializar_celulas(self, linhas, colunas):
        for i in range(linhas):
            self.matriz.append([])
            for j in range(colunas):
                self.matriz[i].append(False)  # inicio com todas mortas

    def qtd_celulas_vivas_vizinhas(self, x, y):
        qtd = 0

        if y > 0 and self.matriz[y - 1][x]:  # cima
            qtd += 1

        if x > 0 and self.matriz[y][x - 1]:  # esquerda
            qtd += 1

        if y < self.qtd_linhas - 1 and self.matriz[y + 1][x]:  # baixo
            qtd += 1

        if x < self.qtd_colunas - 1 and self.matriz[y][x + 1]:  # direita
            qtd += 1

        if y > 0 and x > 0 and self.matriz[y - 1][x - 1]:  # diagonal sup esq
            qtd += 1

        if y < self.qtd_linhas - 1 and x > 0 and self.matriz[y + 1][x - 1]:  # diagonal inf esq
            qtd += 1

        if y > 0 and x < self.qtd_colunas - 1 and self.matriz[y - 1][x + 1]:  # diagonal sup dir
            qtd += 1

        if y < self.qtd_linhas - 1 and x < self.qtd_colunas - 1 and self.matriz[y + 1][x + 1]:  # diagonal inf dir
            qtd += 1

        return qtd

    # Foi necessario para que eu alterasse os indices levando em consideracao sempre o estado anterior
    def matriz_copia(self):
        ret = []
        for i in range(qtd_linhas):
            ret.append([])
            for j in range(qtd_colunas):
                ret[i].append(self.matriz[i][j])  # se eu copiasse a lista direto, se mudar um a outra mudaria junto
        return ret

    def update(self):
        copia = self.matriz_copia()

        for i in range(self.qtd_linhas):
            for j in range(self.qtd_colunas):
                qtd_vizinhas = self.qtd_celulas_vivas_vizinhas(j, i)

                if not self.matriz[i][j] and qtd_vizinhas == 3:  # verifico na original, mas altero na copia
                    copia[i][j] = True  # reviver
                elif self.matriz[i][j] and qtd_vizinhas not in [2, 3]:
                    copia[i][j] = False  # morrer
                # else --> continua no mesmo estado

        self.matriz = copia  # faço o merge com a original

    def __str__(self):
        ret = ""
        for linha in self.matriz:  # cada linha
            for celula in linha:
                if celula:
                    ret += "+"  # celula viva
                else:
                    ret += "."  # celula morta
            ret += "\n"

        return ret


# Leitura de variaveis de controle importantes
qtd_linhas = int(input())
qtd_colunas = int(input())
qtd_iteracoes = int(input())

tabuleiro = Tabuleiro(qtd_linhas, qtd_colunas)
qtd_vivas = int(input())

for i in range(qtd_vivas):  # inicializar algumas celulas vivas
    x, y = input().split(",")
    tabuleiro.matriz[int(x)][int(y)] = True

for n in range(qtd_iteracoes + 1):
    print(tabuleiro, end="")  # printa cada "etapa"
    print("-")
    tabuleiro.update()  # faz as mudanças no estado da vida das celulas
