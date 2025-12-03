print()

notas = []

while True:
    valor = float(input("Digite uma nota [-1 para encerrar]: "))
    if valor == -1:
        break
    notas.append(valor)

quantidade_notas = len(notas)
soma_notas = sum(notas)
media = soma_notas / quantidade_notas
ordem_inversa = notas[::-1]
acima_media = [nota for nota in notas if nota > media]
abaixo_sete = [nota for nota in notas if nota < 7]

print(f"\nQuantidade de notas: {quantidade_notas}")
print(f"notas: {notas}")
print(f"notas invertidas: {ordem_inversa}")
print(f"Soma das notas: {soma_notas:.2f}")
print(f"Média das notas: {media:.2f}")
print(f"Número de notas acima da média: {len(acima_media)}")
print(f"Número de notas abaixo de 7: {len(abaixo_sete)}\n")