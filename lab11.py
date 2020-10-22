########################################################################################################################
# MC102W - 2020 - 1º Semestre
# Aluno: André Amadeu Satorres
# RA: 231300
# Data: 04/06/2020
# Descrição: Sistema que cadastra países com seus respectivos dados e os ordena por nome, população, pib e idh.
########################################################################################################################


class Pais:
    def __init__(self, nome="", populacao=0, pib=0, longevidade=1, qualidade_de_educacao=0, renda=0, desigualdade=0):
        if int(longevidade) <= 0:  # longevidade deve ser maior que 0
            raise ValueError("Longevidade fora do intervalo")

        if int(qualidade_de_educacao) < 0 or int(qualidade_de_educacao) > 10:  # educacao deve estar de 0 a 10
            raise ValueError("Educação fora do intervalo")

        if int(desigualdade) < 0 or int(desigualdade) > 10:  # desigualdade deve estar de 0 a 10
            raise ValueError("Desigualdade fora do intervalo")

        self.nome = nome
        self.populacao = int(populacao)
        self.pib = int(pib)
        self.longevidade = int(longevidade)
        self.qualidade_de_educacao = int(qualidade_de_educacao)
        self.renda = int(renda)
        self.desigualdade = int(desigualdade)
        self.idh = self.desigualdade * (self.longevidade + self.qualidade_de_educacao + self.renda) // 3  # deve ser inteiro

    def __str__(self) -> str:
        return "{nome} {populacao} {pib} {idh}".format(nome=self.nome, populacao=self.populacao, pib=self.pib,
                                                       idh=self.idh)


class GerenciaPaises:
    def __init__(self):
        self.paises = []

    def cadastrar_pais(self, nome, populacao, pib, longevidade, qualidade_de_educacao, renda, desigualdade):
        try:
            pais = Pais(nome, populacao, pib, longevidade, qualidade_de_educacao, renda, desigualdade)
            self.paises.append(pais)
            return True  # inseri
        except ValueError as e:  # longevidade, educacao ou desigualdade têm valores invalidos
            print(e)

        return False  # erro ao inserir

    def printar_ordenado_por(self, campo, crescente):
        if not hasattr(Pais(), campo):  # o metodo hasattr verifica se determinado objeto possui o atributo x
            raise AttributeError("Pais não possui o atributo " + campo)

        if len(self.paises) == 0:
            return

        saida = self.paises.copy()  # uso a funcao copy para nao ter problemas com ponteiro (alterar a lista original)

        # Metodo Insertion Sort, pois é o mais rápido que vimos ate aqui
        for i in range(1, len(saida)):
            aux = saida[i]
            j = i

            if crescente:
                # uso o método getattribute para deixar o metodo mais generico
                while j > 0 and saida[j - 1].__getattribute__(campo) > aux.__getattribute__(campo):
                    saida[j] = saida[j - 1]  # deslocar para a direita
                    j -= 1
            else:
                while j > 0 and saida[j - 1].__getattribute__(campo) < aux.__getattribute__(campo):
                    saida[j] = saida[j - 1]  # deslocar para a direita
                    j -= 1

            saida[j] = aux  # faço a inserção no local certo

        for pais in saida:
            print(pais)  # precisa ser um país por linha

    def __str__(self):
        # A principio, a lista original já esta ordenada por cadastro
        ret = ""
        for pais in self.paises:
            if pais == self.paises[-1]:
                ret += "{0}".format(str(pais))  # ultima linha sem quebra de linha
            else:
                ret += "{0}\n".format(str(pais))  # precisa ser um país por linha

        return ret


def main():
    ger_paises = GerenciaPaises()  # instancio a classe manipuladora de paises

    while True:  # ate ele digitar um comando nao reconhecido
        comando = input().strip()  # opcao que o usuario quer

        if comando == "1":  # CADASTRAR PAÍSES
            qtd_paises = int(input().strip())

            for i in range(qtd_paises):
                atributos = input().strip().split(" ")  # atributos do pais inserido

                # Tento cadastrar um país
                if not ger_paises.cadastrar_pais(atributos[0], atributos[1], atributos[2], atributos[3], atributos[4],
                                                 atributos[5], atributos[6]):
                    return  # Em caso de erro finalizo a execução

        elif comando == "2":  # LISTAR POR ORDEM DE CADASTRO
            print("Ordenado por Cadastro")
            if len(ger_paises.paises) > 0:  # Se não há dados, nao posso printar nenhuma linha
                print(ger_paises)

        elif comando == "3":  # LISTAR ORDENADO POR NOME
            print("Ordenado por Nome")
            ger_paises.printar_ordenado_por("nome", True)  # se for por nome, ordem crescente

        elif comando == "4":  # LISTAR ORDENADO POR TAMANHO POPULACIONAL
            print("Ordenado por População")
            ger_paises.printar_ordenado_por("populacao", False)

        elif comando == "5":  # LISTAR ORDENADO POR PIB
            print("Ordenado por PIB")
            ger_paises.printar_ordenado_por("pib", False)

        elif comando == "6":  # LISTAR ORDENADO POR IDH
            print("Ordenado por IDH")
            ger_paises.printar_ordenado_por("idh", False)

        else:
            return


main()  # Chama o fluxo principal do programa
