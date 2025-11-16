num_1 = int(input("\nDigite o primeiro número: "))
num_2 = int(input("Digite o segundo número: "))
num_3 = int(input("Digite o terceiro número: "))

if num_1 >= num_2 and num_1 >= num_3:
    maior = num_1
elif num_2 >= num_1 and num_2 >= num_3:
    maior = num_2
else:
    maior = num_3

print(f"\nO maior número é: {maior}\n")