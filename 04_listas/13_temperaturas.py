meses = [
    "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
    "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
]

temperaturas = []

for i in range(12):
    temperatura = float(input(f"Temperatura de {meses[i]}: "))
    temperaturas.append(temperatura)

soma = sum(temperaturas)
media_anual = soma / len(meses)

print(f"\nMédia anual: {media_anual:.2f}\n")

print(f"Temperaturas acima da média:")
for i in range(12):
    if temperaturas[i] > media_anual:
        print(f"{i + 1} - {meses[i]} - {temperaturas[i]}°C")

print()
