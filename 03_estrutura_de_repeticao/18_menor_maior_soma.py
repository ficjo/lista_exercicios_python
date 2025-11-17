menor = 0
maior = 0
soma = 0

total = int(input("\nDigite o total de números: "))

print()

for i in range(total):
    num = int(input("Digite um número: "))
    if i == 0:
        menor = num
        maior = num
    else:
        if num <= menor:
            menor = num
        elif num >= maior:
            maior = num
    soma += num

print(f"\n* * * RESULTADOS * * * ")
print(f"Menor       : {menor}")
print(f"Maior       : {maior}")
print(f"Soma        : {soma}\n")