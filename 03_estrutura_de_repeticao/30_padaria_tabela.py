PRECO_UNIDADE = 0.18
contador = 1

print(f"\nPreço do pão: R$ {PRECO_UNIDADE:.2f}")
print("Panificadora Pão de Ontem - Tabela de Preços\n")

while contador <= 50:
    valor = contador * PRECO_UNIDADE
    print(f"{contador} - R$ {valor:.2f}")
    contador += 1

print()