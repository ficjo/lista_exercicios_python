perguntas = [
     "Telefonou para a vítima?",
    "Esteve no local do crime?",
    "Mora perto da vítima?",
    "Devia para a vítima?",
    "Já trabalhou com a vítima?"
]

respostas = []
positivas = 0

print()

for pergunta in perguntas:
    resposta = input(f"{pergunta} - [s/n]: ").lower()
    respostas.append(resposta)

for resposta in respostas:
    if resposta == "s":
        positivas += 1

if positivas == 2:
    classificacao = "Suspeita"
elif positivas == 3 or positivas == 4:
    classificacao = "Cúmplice"
elif positivas == 5:
    classificacao = "Assassino"
else:
    classificacao = "Inocente"

print(f"\nClassificação: {classificacao}\n")