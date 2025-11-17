soma = 0

print()

for i in range(1, 6):
    numero = int(input(f"Digite o {i}º número: "))
    soma += numero

media = soma / 5

print("\n* * * RESULTADOS * * *")
print(f"Soma        : {soma}")
print(f"Média       : {media:.2f}\n")
    