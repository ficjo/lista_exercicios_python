num_inteiro_1 = int(input("\nDigite o primeiro número inteiro: "))
num_inteiro_2 = int(input("Digite o segundo número inteiro: "))
numero_real = float(input("Digite um número real: "))

res_1 = (2 * num_inteiro_1) * (num_inteiro_2 / 2)
res_2 = (num_inteiro_1 * 3) + numero_real
res_3 = numero_real ** 3

print("\n* * * Resultados * * *")
print(f"1. Produto do dobro do 1º com metade do 2º: {res_1}")
print(f"Soma do tripo do 1º com o 3º: {res_2}")
print(f"3º elevado ao cubo: {res_3:.2f}\n")