soma = 0
contador = 1

print()

while True:
    preco_produto = float(input(f"Produto {contador}: R$ "))
    if preco_produto == 0:
        break
    else:
        soma += preco_produto
        contador += 1

print(f"\nValor total: R$ {soma:.2f}")

while True:
    valor_pago = float(input("Digite o valor pago: R$ "))
    if valor_pago < soma:
        print("Valor insuficiente. Tente novamente")
    else:
        troco = valor_pago - soma
        break

print(f"Troco: {troco:.2f}\n")

    