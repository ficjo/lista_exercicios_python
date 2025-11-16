preco_1 = float(input("\nPreço do primeiro produto: "))
preco_2 = float(input("Preço do segundo produto: "))
preco_3 = float(input("Preço do terceiro produto: "))

preco_mais_barato = preco_1
produto_recomendado = "Produto 1"

if preco_2 < preco_mais_barato:
    preco_mais_barato = preco_2
    produto_recomendado = "Produto 2"

if preco_3 < preco_mais_barato:
    preco_mais_barato = preco_3
    produto_recomendado = "Produto 3"

print("\nRESULTADO")
print(f"Valor mais barato: R$ {preco_1:.2f}")
print(f"Produto recomendado: {produto_recomendado}\n")