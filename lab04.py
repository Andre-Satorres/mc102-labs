#  Feito por André Amadeu Satorres - 231300
#  Este laboratório consiste num programa que calcula o montante final de um investimento feito por um usuário
#  Como entrada, recebe o valor inicial investido, a taxa de juros mensal e o número de meses considerados. Então, será fornecido o valor aplicado (positivo) ou resgatado (negativo) em cada mês dentro do prazo informado.
#  Como saída, exibe o montante final após os n meses.

#  Import Decimal para evitar problemas com float
from decimal import Decimal

#  Entradas exigidas pelo enunciado.
v_0 = Decimal(input())  # Valor inicial investido
t = Decimal(input())    # Taxa de juros mensal
n = int(input())        # Número de meses

#  Este será o montante final, a saída do programa
reserva = v_0

#  Loop pelos n meses, para reajustar o montante a cada mês
for i in range(n):

    #  Multiplicando o montante pela taxa de juros
    reserva *= 1 + t

    #  Leitura do valor aplicado/resgatado no mês
    v_i = Decimal(input())

    #  While "infinito", até que o usuário digite um valor de resgate que não exceda o montante, assim, o i do for não incrementa até que se insira um valor válido.
    while v_i < -reserva:

        #  A cada entrada inválida, um print de alerta
        print("Valor inválido no mês", str(i) + ". Tente novamente.")

        #  Lendo o valor novamente, após pedir ao usuário que redigitasse
        v_i = Decimal(input())

    #  Somando o valor aplicado/resgatado no montante final. Logicamente, se v_i < 0 então o montante diminuirá
    reserva += v_i

#  Ao final das operações por n meses, exibimos o montante final, usando o format para ter apenas 2 casas decimais.
print("O total após", n, "meses é de R$", '{:.2f}'.format(reserva) + ".")