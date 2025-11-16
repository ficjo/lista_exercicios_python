PRECO_FILE_ATE_5 = 4.90
PRECO_FILE_ACIMA_5 = 5.80
PRECO_ALCATRA_ATE_5 = 5.90
PRECO_ALCATRA_ACIMA_5 = 6.80
PRECO_PICANHA_ATE_5 = 6.90
PRECO_PICANHA_ACIMA_5 = 7.80
DESCONTO_CARTAO = 0.05

print("\nPromoção de Carnes Tabajara:")
print("[F] - Filé Duplo")
print("[A] - Alcatra")
print("[P] - Picanha")

tipo_carne_letra = input("Escolha o tipo de carne (F/A/P): ").upper()
try:
    quantidade_kg = float(input("Digite a quantidade em Kg: "))
    tipo_pagamento = input("O pagamento será feito com Cartão Tabajara? (S/N): ").upper()
except ValueError:
    print("Erro: A quantidade deve ser um número válido.")
    exit()

preco_por_kg = 0.0
nome_carne = ""

if tipo_carne_letra == 'F':
    nome_carne = "Filé Duplo"
    if quantidade_kg <= 5:
        preco_por_kg = PRECO_FILE_ATE_5
    else:
        preco_por_kg = PRECO_FILE_ACIMA_5

elif tipo_carne_letra == 'A':
    nome_carne = "Alcatra"
    if quantidade_kg <= 5:
        preco_por_kg = PRECO_ALCATRA_ATE_5
    else:
        preco_por_kg = PRECO_ALCATRA_ACIMA_5

elif tipo_carne_letra == 'P':
    nome_carne = "Picanha"
    if quantidade_kg <= 5:
        preco_por_kg = PRECO_PICANHA_ATE_5
    else:
        preco_por_kg = PRECO_PICANHA_ACIMA_5

else:
    print("Erro: Tipo de carne inválido.")
    exit()

valor_bruto = quantidade_kg * preco_por_kg
valor_desconto = 0.0
tipo_pagamento_extenso = "Dinheiro/Outros Cartões"

if tipo_pagamento == 'S':
    valor_desconto = valor_bruto * DESCONTO_CARTAO
    tipo_pagamento_extenso = "Cartão Tabajara"

valor_a_pagar = valor_bruto - valor_desconto

print("\n" + "=" * 40)
print(f"{'CUPOM FISCAL - HIPERMERCADO TABAJARA':^40}")
print("=" * 40)
print(f"Carne               : {nome_carne}")
print(f"Quantidade          : {quantidade_kg:.2f} Kg")
print(f"Preço por Kg        : R$ {preco_por_kg:.2f}")
print(f"Preço Total (Bruto) : R$ {valor_bruto:.2f}")
print(f"Tipo de Pagamento   : {tipo_pagamento_extenso}")
print(f"Valor do Desconto   : R$ {valor_desconto:.2f}")
print("-" * 40)
print(f"VALOR A PAGAR       : R$ {valor_a_pagar:.2f}")
print("=" * 40 + "\n")