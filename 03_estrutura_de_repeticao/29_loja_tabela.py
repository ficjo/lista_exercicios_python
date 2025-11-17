PRECO_UNIDADE = 1.99
contador = 1

print("\nLoja Quase Dois - Tabela de Preços\n")

while contador <= 50:
    valor = contador * PRECO_UNIDADE
    print(f"{contador} - R$ {valor:.2f}")
    contador += 1

print()