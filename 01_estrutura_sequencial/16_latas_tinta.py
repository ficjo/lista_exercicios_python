import math

COBERTURA_LITRO = 3.0
CAPACIDADE_LATA = 18.0
PRECO_LATA = 80.0

area_a_pintar = float(input("\nTamanho da área a ser pintada: "))

litros_necessarios = area_a_pintar / COBERTURA_LITRO
latas_necessarias = math.ceil(litros_necessarios / CAPACIDADE_LATA)
preco_total = latas_necessarias * PRECO_LATA

print("\n* * * ORÇAMENTO * * *")
print(f"Litros de tinta necessários: {litros_necessarios:.1f}")
print(f"Quantidade de latas a comprar: {latas_necessarias}")
print(f"Preço total: R$ {preco_total:.2f}\n")
