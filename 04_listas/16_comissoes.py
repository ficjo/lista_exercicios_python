contadores = [0, 0, 0, 0, 0, 0, 0, 0, 0]
vendas = []
salarios = []
intervalos = [
    "$200 - $299",
    "$300 - $399",
    "$400 - $499",
    "$500 - $599",
    "$600 - $699",
    "$700 - $799",
    "$800 - $899",
    "$900 - $999",
    "$1000 ou mais"
]

print()

while True:
    venda = float(input("Valor de vendas [-1 para sair]: "))
    if venda == -1:
        break
    vendas.append(venda)

for venda in vendas:
    salario = 200 + (0.09 * venda)
    faixa = int((salario // 100) - 2)

    if faixa < 0:
        faixa = 0
    
    if faixa > 8:
        faixa = 8

    salarios.append(salario)
    contadores[faixa] += 1

print(f"\nDistribuição de Salários:")
for i in range(9):
    print(f"{intervalos[i]}: {contadores[i]}")

print()