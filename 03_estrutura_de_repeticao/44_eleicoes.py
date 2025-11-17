votos_candidato1 = 0
votos_candidato2 = 0
votos_candidato3 = 0
votos_candidato4 = 0
votos_nulos = 0
votos_em_branco = 0
total_votos = 0

print("\n* * * Eleição Presidencial * * *")
print("Candidatos:")
print("1 - João")
print("2 - José")
print("3 - Maria")
print("4 - Ana")
print("Opções: 5 (Nulo), 6 (Branco)")
print("Digite 0 para finalizar a votação.")

while True:
    codigo_str = input("Digite seu voto (código): ")
    codigo = int(codigo_str)

    if codigo == 0:
        break

    if 1 <= codigo <= 4:
        total_votos += 1
        if codigo == 1:
            votos_candidato1 += 1
        elif codigo == 2:
            votos_candidato2 += 1
        elif codigo == 3:
            votos_candidato3 += 1
        elif codigo == 4:
            votos_candidato4 += 1
    elif codigo == 5:
        votos_nulos += 1
        total_votos += 1
    elif codigo == 6:
        votos_em_branco += 1
        total_votos += 1
    else:
        print("CÓDIGO INVÁLIDO. Voto não registrado.")

print("\n* * * Apuração * * *")

if total_votos > 0:
    
    percentual_nulos = (votos_nulos / total_votos) * 100
    percentual_brancos = (votos_em_branco / total_votos) * 100
    
    print("\n[TOTAL DE VOTOS POR CANDIDATO]")
    print(f"João            : {votos_candidato1} votos")
    print(f"José            : {votos_candidato2} votos")
    print(f"Maria           : {votos_candidato3} votos")
    print(f"Ana             : {votos_candidato4} votos")
    
    print("\n[OUTROS VOTOS]")
    print(f"Votos Nulos     : {votos_nulos} votos ({percentual_nulos:.2f}%)")
    print(f"Votos em Branco : {votos_em_branco} votos ({percentual_brancos:.2f}%)")
    print(f"Total de votos  : {total_votos}\n")
    
else:
    print("Nenhum voto foi registrado.")
    
print()