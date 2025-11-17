votos_candidato_1 = 0
votos_candidato_2 = 0
votos_candidato_3 = 0
votos_invalidos = 0

num_eleitores = int(input("\nDigite o número de eleitores: "))

print()

for i in range(num_eleitores):
    voto = int(input(f"Digite o {i + 1}º voto [1/2/3]: "))
    if voto == 1:
        votos_candidato_1 += 1
    elif voto == 2:
        votos_candidato_2 += 1
    elif voto == 3:
        votos_candidato_3 += 1
    else:
        votos_invalidos += 1
        
print(f"\n* * * RESULTADOS * * *")
print(f"Candidato 1     : {votos_candidato_1}")
print(f"Candidato 2     : {votos_candidato_2}")
print(f"Candidato 3     : {votos_candidato_3}")
print(f"Votos inválidos : {votos_invalidos}\n")
    