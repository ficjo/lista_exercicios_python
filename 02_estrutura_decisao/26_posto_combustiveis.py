PRECO_ALCOOL = 1.90
PRECO_GASOLINA = 2.50

valor_bruto = 0
valor_desconto = 0
percentual_desconto = 0

litros = float(input("\nDigite o número de litros vendidos: "))
tipo_combustivel = input("Digite o tipo de combustível [A | G]: ").upper()

if tipo_combustivel == 'A':
    valor_bruto = litros * PRECO_ALCOOL
    if litros <= 20:
        percentual_desconto = 3
    else:
        percentual_desconto = 5
elif tipo_combustivel == 'G':
    valor_bruto = litros * PRECO_GASOLINA
    if litros <= 20:
        percentual_desconto = 4
    else:
        percentual_desconto = 6
else:
    print("COMBUSTÍVEL INVÁLIDO.")
    print("* * * saindo do programa... * * *\n")
    exit()

valor_desconto = valor_bruto * (percentual_desconto / 100)
valor_a_pagar = valor_bruto - valor_desconto

print()

print("-" * 50)
print(f"Tipo de Combustível : {tipo_combustivel}")
print(f"Litros Vendidos     : {litros:.2f} L")
print(f"Valor Bruto         : R$ {valor_bruto:.2f}")
print(f"Desconto Aplicado   : {percentual_desconto}% (R$ {valor_desconto:.2f})")
print(f"Valor Total a Pagar : R$ {valor_a_pagar:.2f}")
print("-" * 50)

print()