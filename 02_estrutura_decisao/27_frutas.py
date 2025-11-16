PRECO_MORANGO_ATE_5 = 2.50
PRECO_MORANGO_ACIMA_5 = 2.20
PRECO_MACA_ATE_5 = 1.80
PRECO_MACA_ACIMA_5 = 1.50

try:
    kg_morango = float(input("\nDigite a quantidade de morangos (Kg): "))
    kg_maca = float(input("Digite a quantidade de maçãs (Kg): "))
except ValueError:
    print("Erro: Digite apenas números válidos para o peso.")
    exit()

if kg_morango <= 5:
    valor_morango = kg_morango * PRECO_MORANGO_ATE_5
else:
    valor_morango = kg_morango * PRECO_MORANGO_ACIMA_5

if kg_maca <= 5:
    valor_maca = kg_maca * PRECO_MACA_ATE_5
else:
    valor_maca = kg_maca * PRECO_MACA_ACIMA_5

peso_total = kg_morango + kg_maca
valor_bruto_total = valor_morango + valor_maca
valor_a_pagar = valor_bruto_total

if peso_total > 8 or valor_bruto_total > 25.00:
    desconto = valor_bruto_total * 0.10
    valor_a_pagar = valor_bruto_total - desconto
    tem_desconto = True
else:
    desconto = 0.0
    tem_desconto = False

print()

print("-" * 40)
print(f"Peso Total Adquirido    : {peso_total:.2f} Kg")
print(f"Valor Bruto da Compra   : R$ {valor_bruto_total:.2f}")

if tem_desconto:
    print(f"Desconto (10%)          : R$ {desconto:.2f}")
    print(f"Valor Final a Pagar     : R$ {valor_a_pagar:.2f}")
else:
    print("Não houve desconto aplicado.")
    print(f"Valor Final a Pagar     : R$ {valor_a_pagar:.2f}")
print("-" * 40)

print()