
soma = 0
maior_temp = 0
menor_temp = 0
num_temperaturas = int(input("\nDigite o número de temperaturas: "))

print()

for i in range(num_temperaturas):
    temp = float(input(f"Digite a {i + 1}ª temperatura: "))
    soma += temp
    if i == 0:
        maior_temp = temp
        menor_temp = temp
    else:
        if temp >= maior_temp:
            maior_temp = temp
        elif temp <= menor_temp:
            menor_temp = temp

media = soma / num_temperaturas

print("\n* * * RESULTADOS * * *")
print(f"Total de temperaturas   : {num_temperaturas:.2f}")
print(f"Soma das temperaturas   : {soma:.2f}")
print(f"Média das temperaturas  : {media:.2f}")
print(f"Maior temperatura       : {maior_temp:.2f}")
print(f"Menor temperatura       : {menor_temp:.2f}\n")