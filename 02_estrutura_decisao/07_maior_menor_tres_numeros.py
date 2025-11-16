num_1 = int(input("\nDigite o primeiro número: "))
num_2 = int(input("Digite o segundo número: "))
num_3 = int(input("Digite o terceiro númeor: "))

maior = num_1
menor = num_1

if num_2 > maior:
    maior = num_2

if num_3 > maior:
    maior = num_3

if num_2 < menor:
    menor = num_2

if num_3 < menor:
    menor = num_3
    
print(f"\nMaior: {maior}")
print(f"Menor: {menor}\n")