menor = 0
maior = 0
soma = 0
contador = 1

total = int(input("\nDigite o total de números: "))

print()

while contador <= total:
    num = int(input("Digite um número: "))
    if 0 <= num <= 1000:    
        soma += num
        if contador == 1:
            menor = num
            maior = num
        else:
            if num <= menor:
                menor = num
            elif num >= maior:
                maior = num
        contador += 1
    else:
        print("ERRO: Número deve ser entre 0 e 1000. Tente novamente.")

print(f"\n* * * RESULTADOS * * * ")
print(f"Menor       : {menor}")
print(f"Maior       : {maior}")
print(f"Soma        : {soma}\n")