import math

COBERTURA_LITRO = 6.0
CAPACIDADE_LATA = 18.0
PRECO_LATA = 80.0
CAPACIDADE_GALAO = 3.6
PRECO_GALAO = 25.0
FOLGA = 0.10

area_a_pintar = float(input("\nDigite a área a pintar: "))

litros_base = area_a_pintar / COBERTURA_LITRO
litros_totais = litros_base * (1 + FOLGA)

# APENAS LATAS
latas_1 = math.ceil(litros_totais / CAPACIDADE_LATA)
preco_1 = latas_1 * PRECO_LATA

# APENAS GALÕES
galoes_2 = math.ceil(litros_totais / CAPACIDADE_GALAO)
preco_2 = galoes_2 * PRECO_GALAO

# MISTURADO
latas_3 = math.floor(litros_totais / CAPACIDADE_LATA)
litros_restantes = litros_totais % CAPACIDADE_LATA
galoes_3 = math.ceil(litros_restantes / CAPACIDADE_GALAO)
preco_3 = (latas_3 * PRECO_LATA) + (galoes_3 * PRECO_GALAO)

print("\n* * * RESULTADOS * * *")
print(f"Litros necessários (+10%): {litros_totais:.1f}")

print("\nApenas Latas")
print(f"Latas a comprar: R$ {latas_1}")
print(f"Preço total: R$ {preco_1:.2f}")

print("\nApenas Galões")
print(f"Galões a comprar: {galoes_2}")
print(f"Preço total: R$ {preco_2:2f}")

print("\nMisturando")
print(f"Latas: {latas_3}")
print(f"Galões: {galoes_3}")
print(f"Preço total: R$ {preco_3:.2f}\n")

