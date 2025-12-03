"""
Como estou seguindo a ordem de estudos e funções e arquivos são 
assuntos futuros, resolvi esse exercício usando apenas listas.
"""

print("\n* * MELHOR JOGADOR * *\n")

votos = [0] * 24
total_votos = 0


while True:
    voto = int(input("Número do jogador [0 para sair]: "))
    if voto == 0:
        print("\nVOTAÇÃO ENCERRADA.\n")
        break
    elif 1 <= voto <= 23:
        votos[voto] += 1
        total_votos += 1
    else:
        print("Voto inválido, deve ser entre 1 e 23")

print("RESULTADO")
if total_votos == 0:
    print("\nNenhum voto computado.\n")
else:
    resultados = []
    print(f"Foram computados: {total_votos} votos.")
    print(f"{'Jogador':<10} {'Votos':>10} {'%':>10}")

    for i in range(1, 24):
        votos_jogador = votos[i]
        if votos_jogador > 0:
            percentual = (votos_jogador / total_votos) * 100.0
            resultados.append((i, votos_jogador, percentual))
            print(f"{i:<10} {votos_jogador:>10} {percentual:>10.2f}")

mais_votado = resultados[0]
for res in resultados:
    if res[1] > mais_votado[1]:
        mais_votado = res

print(f"\nO melhor jogador foi o número {mais_votado[0]}, com {mais_votado[1]} votos, correspondendo a {mais_votado[2]:.2f}% do total de votos.\n")