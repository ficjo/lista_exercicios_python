# Inicialização dos valores
total_geral = 0.0

print("\nLanchonete - Cardápio")
print("Código | Preço | Produto")
print("100    | R$ 1,20 | Cachorro Quente")
print("101    | R$ 1,30 | Bauru Simples")
print("102    | R$ 1,50 | Bauru com ovo")
print("103    | R$ 1,20 | Hambúrguer")
print("104    | R$ 1,30 | Cheeseburguer")
print("105    | R$ 1,00 | Refrigerante")
print("Digite 0 no código para fechar o pedido.")

while True:
    
    codigo = int(input("\nDigite o código do item (0 para encerrar): "))

    if codigo == 0:
        break
        
    quantidade = int(input("Quantidade: "))

    if codigo == 100:
        preco_unitario = 1.20
        nome_item = "Cachorro Quente"
    elif codigo == 101:
        preco_unitario = 1.30
        nome_item = "Bauru Simples"
    elif codigo == 102:
        preco_unitario = 1.50
        nome_item = "Bauru com ovo"
    elif codigo == 103:
        preco_unitario = 1.20
        nome_item = "Hambúrguer"
    elif codigo == 104:
        preco_unitario = 1.30
        nome_item = "Cheeseburguer"
    elif codigo == 105:
        preco_unitario = 1.00
        nome_item = "Refrigerante"
    else:
        print("CÓDIGO INVÁLIDO. Tente novamente.")
        continue 
        
    valor_item = preco_unitario * quantidade
    total_geral += valor_item
    
    print(f"-> {nome_item}: {quantidade}x R$ {preco_unitario:.2f} = R$ {valor_item:.2f}\n")

print(f"\nTotal do Pedido: R$ {total_geral:.2f}\n")