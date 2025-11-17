contagem_25 = 0
contagem_50 = 0
contagem_75 = 0
contagem_100 = 0

print("\n1Digite um número negativo para encerrar a entrada de dados.\n")

while True:
    numero_str = input("Digite um número: ")
    numero = float(numero_str)

    if numero < 0:
        break

    if 0 <= numero <= 25:
        contagem_25 += 1
    elif 26 <= numero <= 50:
        contagem_50 += 1
    elif 51 <= numero <= 75:
        contagem_75 += 1
    elif 76 <= numero <= 100:
        contagem_100 += 1
    else:
        print("Número fora do intervalo [0-100] e não será contado.")

print("\n* * * Resultados * * *")
print(f"Intervalo [0-25]    : {contagem_25} números")
print(f"Intervalo [26-50]   : {contagem_50} números")
print(f"Intervalo [51-75]   : {contagem_75} números")
print(f"Intervalo [76-100]  : {contagem_100} números\n")