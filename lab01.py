from decimal import Decimal

preco = Decimal(input())

parteInteira = preco/1
parteDecimal = preco%1

a = int(parteInteira/10)
b = int(parteInteira % 10)

parteDecimal = parteDecimal * 100

c = int(parteDecimal / 10)
d = int(parteDecimal % 10)

print("R$ " + str(d) + str(c) + "." + str(b) + str(a))
