########################################################################################################################################################
# MC102W - 2020 - 1º Semestre
# Aluno: André Amadeu Satorres
# RA: 231300
# Data: 10/05/2020
# Descrição: Programa que simula o Governo Brasileiro na sua função de distribuir auxílio financeiro mensal para alguns brasileiros nos tempos de COVID
#########################################################################################################################################################

class Governo:
    """
    A classe Governo representa o Governo nesse momento de pandemia. Possui apenas os atributos importantes para
    as funcionalidades que desejamos, isto é, distribuir os auxílios para parcela da população, avaliando se quem
    receberá se enquadra em certos quesitos.
    """

    def __init__(self):
        self.__beneficios_concedidos = []  # lista de Beneficiários que estão recebendo o auxílio atualmente
        self.__recursos_disponiveis = 0  # quantia em reais de quanto o governo tem disponível para a concessão de auxílios
        self.__beneficios_pendentes = []  # lista de Beneficiários que estão pendendo avaliação

    @property
    def beneficios_concedidos(self):
        return self.__beneficios_concedidos  # getter para os beneficios concedidos

    @beneficios_concedidos.setter
    def beneficios_concedidos(self, beneficios):
        self.__beneficios_concedidos = beneficios  # setter para os beneficios concedidos

    @property
    def recursos_disponiveis(self):
        return self.__recursos_disponiveis  # getter para os recursos disponiveis

    @recursos_disponiveis.setter
    def recursos_disponiveis(self, recursos_disponiveis):
        self.__recursos_disponiveis = recursos_disponiveis  # setter para os recursos disponiveis

    @property
    def beneficios_pendentes(self):
        return self.__beneficios_pendentes  # getter para os beneficios pendentes

    @beneficios_pendentes.setter
    def beneficios_pendentes(self, beneficios_pendentes):
        self.__beneficios_pendentes = beneficios_pendentes  # setter para os beneficios pendentes

    def avaliar_beneficiarios_pendentes(self):
        """
         Avalia se os Beneficiários que ainda não foram aprovados (Pendentes) estão aptos a receber o auxílio,
        e concede o auxílio aos que se enquadram nos requerimentos.
        :return: None
        """

        print("Beneficiários avaliados")

        for beneficiario in self.__beneficios_pendentes:
            if self.esta_apto(beneficiario):
                self.__beneficios_concedidos.append(beneficiario)  # guarda na "fila de aprovados"
                beneficiario.status = "Com auxílio"
            else:  # negar beneficio
                beneficiario.status = "Negado"

        print("Lista de beneficiários atualizada")

    def esta_apto(self, beneficiario: beneficios_concedidos):
        """
        Verifica se certo beneficiario está apto para receber o auxílio, dependendo de certas restrições.
        :param beneficiario: lista de beneficiarios
        :return: False se ele não está apto.
        :return: True se ele está apto.
        """

        if beneficiario.idade < 18:
            return False

        if beneficiario.emprego.lower() not in ["desempregado", "desempregada", "autonomo", "autonoma",
                                                "microempreendedor", "microempreendedora"]:
            return False

        if beneficiario in self.beneficios_concedidos:
            return False

        if beneficiario.status == "Negado":
            return False

        if beneficiario.renda_per_capita > 522.5 and beneficiario.renda_total > 3135:
            return False

        # Nao preciso checar o Status dele, pois garanto que será "Pendente" na função de guardá-los

        return True

    def adicionar_recursos(self, valor):
        """
         Adiciona recursos (em reais) voltados à concessão de auxílios.
        :param valor: string contendo o valor a se adicionar
        :return: None
        """

        self.__recursos_disponiveis += float(valor)
        print("Recursos adicionados")

    def imprimir_recursos_disponiveis(self):
        """
         Imprime na tela quantos reais ainda estão disponíveis para a concessão de auxílios.
        :return: None
        """

        valor_disp = '{:.2f}'.format(self.__recursos_disponiveis)
        print("Recursos disponíveis: R$ {valor}".format(valor=valor_disp))

    def imprimir_beneficiarios_atuais(self):
        """
         Imprime na tela o nome, sobrenome e CPF de quem está recebendo o auxílio atualmente.
        :return: None
        """

        print("Beneficiários atuais:")

        for beneficiario in self.__beneficios_concedidos:
            print("{cpf}: {nome} {sobrenome}".format(cpf=beneficiario.cpf,
                                                     nome=beneficiario.nome[0],
                                                     sobrenome=" ".join(beneficiario.nome[1:])))

    def enviar_auxilio_mensal(self):
        """
         Se houver recursos suficientes, envia o auxílio a todos os beneficiários; caso contrário, envia por ordem
         de solicitação até que os recursos se esgotem.
        :return: None
        """

        if self.recursos_disponiveis < 600 * len(self.beneficios_concedidos):  # 600 para cada um na fila
            print("Recursos insuficientes")
        else:
            print("Auxílio mensal enviado")

        for beneficiario in self.__beneficios_concedidos:  # envia por ordem de solicitacao ate acabar o dinheiro
            if self.__recursos_disponiveis < 600:
                break

            beneficiario.receber_beneficio()  # incremente o tempo de recebimento
            self.__recursos_disponiveis -= 600


class Beneficiario:
    """
    A classe Beneficiario representa uma pessoa que deseja receber o auxílio do Governo nesses tempos de crise. Para
    isso, ela precisa realizar um cadastro em seu perfil, representado pelos seus atributos, e solicitar o auxílio ao
    Governo Federal. Este, por sua vez, avaliará se esta pessoa deve ou não receber o dinheiro. Ela pode receber por
    no máximo 3 meses.
    """

    def __init__(self):
        self.__nome_completo = [""]
        self.__cpf = ""
        self.__status = "Perfil incompleto"
        self.__renda_per_capita = 0
        self.__renda_total = 0
        self.__idade = 0
        self.__emprego = ""
        self.__tempo_de_recebimento = 0

    @property
    def nome(self):
        return self.__nome_completo

    @property
    def cpf(self):
        return self.__cpf

    @property
    def status(self):
        return self.__status

    @property
    def renda_per_capita(self):
        return self.__renda_per_capita

    @property
    def renda_total(self):
        return self.__renda_total

    @property
    def idade(self):
        return self.__idade

    @property
    def emprego(self):
        return self.__emprego

    @status.setter
    def status(self, status):
        self.__status = status

    def faltam_dados(self):
        """
        Verifica se a pessoa inseriu todos os dados necessários para concluir seu perfil
        :return: True se inseriu tudo o que for necessário
        :return: False se não inseriu tudo o que era necessário
        """

        return self.__nome_completo == [""] \
               or self.__cpf == "" \
               or self.__idade == 0 \
               or self.__emprego == ""

    def update_incompleto(self):
        """
        Método que faz um update no status do beneficiário para completo, avaliando se todos os dados já foram
        inseridos corretamente.
        :return: None
        """

        if not self.faltam_dados() and self.__status == "Perfil incompleto":
            self.__status = "Perfil completo"

    def inserir_nome_completo(self, nome):
        """
        Método para iserir o nome do beneficiário.
        :param nome: String representando o nome a ser inserido
        :return: None
        """

        self.__nome_completo = nome.upper().split(" ")  # Nomes e sobrenomes deverão estar full UPPERCASE

        self.update_incompleto()

        print("Nome inserido")

    def inserir_cpf(self, cpf):
        """
        Método para inserir o cpf do beneficiário.
        :param cpf: String que representa o cpf a ser inserido
        :return: None
        """

        self.__cpf = format_cpf(cpf)

        self.update_incompleto()

        print("CPF inserido")

    def inserir_renda_per_capita(self, renda_per_capita):
        """
        Método para inserir a renda per capita do beneficiário.
        :param renda_per_capita: String que representa a renda per capita a ser inserida
        :return: None
        """

        renda_per_capita = float(renda_per_capita)

        if renda_per_capita < 0:
            renda_per_capita = 0

        self.__renda_per_capita = renda_per_capita

        self.update_incompleto()

        print("Renda per capita inserida")

    def inserir_renda_total(self, renda_total):
        """
        Método para inserir a renda total do beneficiário.
        :param renda_total: String que representa a renda total a ser inserida
        :return: None
        """

        renda_total = float(renda_total)

        if renda_total < 0:
            renda_total = 0

        self.__renda_total = renda_total

        self.update_incompleto()

        print("Renda total inserida")

    def inserir_idade(self, idade):
        """
        Método para inserir a idade do beneficiário.
        :param idade: String que representa a idade a ser inserida
        :return: None
        """

        idade = int(idade)

        if idade < 0:
            idade = 0

        self.__idade = idade

        self.update_incompleto()

        print("Idade inserida")

    def inserir_emprego(self, emprego):
        """
        Método para inserir o emprego do beneficiário.
        :param emprego: String que representa o emprego a ser inserido
        :return: None
        """

        self.__emprego = emprego.lower()

        self.update_incompleto()

        print("Emprego inserido")

    def solicitar_beneficio(self, governo):
        """
        Método para solicitar o benefício ao governo. Avalia se o beneficiário já inseriu todos os seus dados antes de
        solicitar. Se não tiver preenchido tudo corretamente, exibe mensagem alertando o beneficiário.
        :param governo: Governo que representa o governo a se solicitar
        :return: None
        """

        if self.__status == "Com auxílio":  # nao pode solicitar se ja estiver recebendo
            return

        if self.__status == "Perfil completo":
            print("Auxílio solicitado, aguarde avaliação")  # so solicita se estiver preenchido todo seu perfil
            self.__status = "Pendente"
            governo.beneficios_pendentes.append(self)

        elif self.__status == "Perfil incompleto":
            print("Complete seu perfil e tente novamente")

    def receber_beneficio(self):
        """
        Método para receber o auxílio do Governo. Incrementa o tempo de recebimento do auxílio toda vez que o método é
        chamado. Se já tiver recebido por mais de 3 meses, altera o status do beneficiário para "Auxílio finalizado".
        :return:
        """

        self.__tempo_de_recebimento += 1

        if self.__tempo_de_recebimento > 3:  # so recebe o auxilio por 3 meses
            self.__status = "Auxílio finalizado"

    def transferir_beneficio(self, conta):
        """ Transfere o benefício completo acumulado a uma conta corrente, podendo transferir de 0 a 3 meses de auxílio
        em seu valor integral.
        :param conta: String que representa o número da conta corrente a ser feita a transferência.
        :return: None
        """

        valor = "{:.2f}".format(self.__tempo_de_recebimento * 600)  # Quanto ele ja recebeu de auxilio
        print("Valor de R$ {quantia} transferido para a conta corrente {numero_conta}".format(quantia=valor,
                                                                                              numero_conta=conta))

    def imprimir_nome_completo(self):
        """
        Método para imprimir o nome completo do beneficiário.
        :return: None
        """

        print("Nome completo: {nome} {sobrenome}".format(nome=self.__nome_completo[0],
                                                         sobrenome=" ".join(self.__nome_completo[1:])))

    def imprimir_status(self):
        """
        Método para imprimir o status do beneficiário.
        :return: None
        """

        print("Status: {status}".format(status=self.__status))

    def imprimir_cpf(self):
        """
        Método para imprimir o CPF do beneficiário.
        :return: None
        """

        print("CPF: {cpf}".format(cpf=self.__cpf))

    def imprimir_todas_infos(self):
        """
        Método para imprimir todas as informações do beneficiário.
        :return: None
        """

        print(self)

    def __str__(self):
        renda_pc = "{:.2f}".format(self.__renda_per_capita)
        renda_tot = "{:.2f}".format(self.__renda_total)

        return "Nome completo: {nome} {sobrenome}\n" \
                   .format(nome=self.__nome_completo[0], sobrenome=" ".join(self.__nome_completo[1:])) + \
               "Status: {status}\n" \
                   .format(status=self.__status) + \
               "CPF: {cpf}\n" \
                   .format(cpf=self.__cpf) + \
               "Renda per capita: R$ {renda_per_capita}\n" \
                   .format(renda_per_capita=renda_pc) + \
               "Renda total: R$ {renda_total}\n" \
                   .format(renda_total=renda_tot) + \
               "Idade: {idade}\n" \
                   .format(idade=self.__idade) + \
               "Emprego: {emprego}\n" \
                   .format(emprego=self.__emprego) + \
               "Tempo de recebimento: {tempo_de_recebimento} meses" \
                   .format(tempo_de_recebimento=self.__tempo_de_recebimento)


def format_cpf(cpf):
    """
    Função para formatar um CPF passado como parâmetro da forma correta.
    :param cpf: String representando o CPF a ser formatado.
    :return: O CPF formatado corretamente.
    """

    if cpf.strip() == "":  # se recebi um CPF nulo ja saio fora
        return ""

    cpf = cpf.replace(".", "").replace("-", "").replace(" ", "")  # preciso tirar por causa da formatacao q vou fazer

    while len(cpf) < 11:
        cpf += "0"  # poe zeros caso falte numeros

    return "{}.{}.{}-{}".format(cpf[:3], cpf[3:6], cpf[6:9], cpf[9:])  # O CPF deverá possuir a forma xxx.xxx.xxx-xx


def get_beneficiario(beneficiarios, cpf: str):
    """
    Pesquisa e retorna um beneficiario numa lista fornecida, a partir de um CPF dado.
    :param beneficiarios: Lista de Beneficiarios onde se pesquisará o beneficiário.
    :param cpf: O CPF do beneficiário que se pretende encontrar.
    :return: Beneficiario representando o Beneficiario encontrado, se encontrar.
    :return: None caso não encontre um Beneficiário para aquele CPF.
    """
    beneficiarios[0].nome = "oi"

    for b in beneficiarios:
        if b.cpf == cpf:
            return b

    return None


def main():
    """
    Fluxo principal do programa.
    :return: None
    """

    beneficiarios_inseridos = []  # guardar quem for ir sendo inserido
    governo = Governo()
    opcao = [""]
    while opcao[0] != 'X':
        opcao = input().upper().split(" ")

        if opcao[0] == "GOVERNO":

            # Com um dicionario ache que ficaria mais "limpo" chamar as funcoes a partir do digitado
            acoes_disponiveis = {
                1: governo.avaliar_beneficiarios_pendentes,
                2: governo.adicionar_recursos,
                3: governo.imprimir_recursos_disponiveis,
                4: governo.imprimir_beneficiarios_atuais,
                5: governo.enviar_auxilio_mensal
            }

            digitado = input().strip().split(" ")

            while digitado[0].upper() != 'F':
                if int(digitado[0]) == 2:  # tem o parametro da quantia
                    acoes_disponiveis[int(digitado[0])]("".join(digitado[1:]).strip())
                else:
                    acoes_disponiveis[int(digitado[0])]()

                digitado = input().strip()

        elif opcao[0] == "BENEFICIARIO":
            try:
                cpf = format_cpf(opcao[1])  # ele passou um cpf. Devo usar o usuario que tem esse CPF
                beneficiario = get_beneficiario(beneficiarios_inseridos, cpf)  # obtenho-o
                acoes_disponiveis = {
                    1: beneficiario.inserir_nome_completo,
                    2: beneficiario.inserir_cpf,
                    3: beneficiario.inserir_renda_per_capita,
                    4: beneficiario.inserir_renda_total,
                    5: beneficiario.inserir_idade,
                    6: beneficiario.inserir_emprego,
                    7: beneficiario.solicitar_beneficio,
                    8: beneficiario.transferir_beneficio,
                    9: beneficiario.imprimir_nome_completo,
                    10: beneficiario.imprimir_status,
                    11: beneficiario.imprimir_cpf,
                    12: beneficiario.imprimir_todas_infos
                }

            except IndexError:  # nao digitou o cpf (quer consultar um novo)
                beneficiario = Beneficiario()
                beneficiarios_inseridos.append(beneficiario)  # guardo o beneficiario inserido

                acoes_disponiveis = {
                    1: beneficiario.inserir_nome_completo,
                    2: beneficiario.inserir_cpf,
                    3: beneficiario.inserir_renda_per_capita,
                    4: beneficiario.inserir_renda_total,
                    5: beneficiario.inserir_idade,
                    6: beneficiario.inserir_emprego,
                    7: beneficiario.solicitar_beneficio,
                    8: beneficiario.transferir_beneficio,
                    9: beneficiario.imprimir_nome_completo,
                    10: beneficiario.imprimir_status,
                    11: beneficiario.imprimir_cpf,
                    12: beneficiario.imprimir_todas_infos
                }

            digitado = input().strip()

            while digitado.upper() != 'F':
                escolha = int(digitado[:2].strip())  # se for '1 ', será int('1') = 1. Se for '12', sera int('12') = 12

                if escolha <= 12:  # garantindo que está num range permitido
                    if 7 > escolha > 0 or escolha == 8:  # ha parametros que sao inseridos pelo input do usuario
                        acoes_disponiveis[escolha]("".join(digitado[1:]).strip())
                    else:
                        if escolha == 7:  # so ha o parametro do governo atual
                            acoes_disponiveis[escolha](governo)
                        else:
                            acoes_disponiveis[escolha]()  # nao ha parametros a serem inseridos

                digitado = input().strip().upper()


main()  # Chama o fluxo principal
