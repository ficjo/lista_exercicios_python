import random

NUMERO_LANCAMENTOS = 100
NUMERO_FACES = 6

contadores = [0] * NUMERO_FACES

resultados_lancamentos = [] 

print(f"Simulação de {NUMERO_LANCAMENTOS} Lançamentos de Dado")

for _ in range(NUMERO_LANCAMENTOS):
    valor_dado = random.randint(1, NUMERO_FACES)
    resultados_lancamentos.append(valor_dado)
    contadores[valor_dado - 1] += 1

print("\nFrequência dos Resultados")
print("---------------------------")

for face in range(1, NUMERO_FACES + 1):
    contagem = contadores[face - 1]
    percentual = (contagem / NUMERO_LANCAMENTOS) * 100
    print(f"Face {face}: {contagem:3} vezes ({percentual:.1f}%)")

print()