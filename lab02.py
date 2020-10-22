from decimal import Decimal
nome = input()
d = int(input())
v = Decimal(input())

if d < 8 or d > 14:
    print("Número de horas diárias não admitido")
else:
    multiplicador = 0
    horasAdicionais = d - 8
    if 0 < horasAdicionais <= 4:
        multiplicador = 1.25
    else:
        multiplicador = 1.5

    novoSalario = 22 * v * Decimal(8 + multiplicador * horasAdicionais)  # multiplicador sera 0 se nao houver horas adicionais

    #formatando
    novoSalario = Decimal((novoSalario * 100) // 1)
    decimal = Decimal(int(novoSalario % 100) / 10)
    novoSalario = Decimal(novoSalario / 100)

    aMais = ""
    if decimal == 0:
        aMais = ".00"
    elif decimal % 1 == 0:
        aMais = aMais + "0"

    print("O salário do(a) funcionário(a)", nome, "será de R$" + str(novoSalario) + aMais, "para esse mês")