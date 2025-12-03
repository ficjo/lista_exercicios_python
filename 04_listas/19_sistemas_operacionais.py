opcoes_os = [
    "Windows Server",
    "Unix",
    "Linux",
    "Netware",
    "Mac OS",
    "Outro"
]

votos = [0] * 6
resultados = []
total_votos = 0

print("""\nQual o melhor Sistema Operacional para uso em servidores?" 
As possíveis respostas são: 
1- Windows Server 
2- Unix 
3- Linux 
4- Netware 
5- Mac OS 
6- Outro 
""")

while True:
    voto = int(input("Digite a opção [1-6]: "))
    if voto == 0:
        print("\n* * VOTAÇÃO ENCERRADA * *")
        break
    if 1 <= voto <= 6:
        votos[voto - 1] += 1
        total_votos += 1
    else:
        print("Valor inválido.")

if total_votos == 0:
    print("\nNenhum voto computado. PROGRAMA ENCERRADO.\n")
else:
    print(f"{'Sistema Operacional':<15} {'Votos':>10} {'%':>10}")
    print(f"{'-------------------':<15} {'-----':>10} {'---':>12}")
    for i in range(6):
        votos_os = votos[i]
        # if votos_os > 0:
        percentual = int((votos_os / total_votos) * 100.0)
        resultados.append((i, votos_os, percentual))
        print(f"{opcoes_os[i]:<15} {votos_os:>14} {percentual:>11}%")
    print(f"{'-------------------':<15} {'-----':>10} {'---':>12}")
    print(f"{'Total':<15} {total_votos:>14}")

mais_votado = resultados[0]
for res in resultados:
    if res[1] > mais_votado[1]:
        mais_votado = res

print(f"\nO SO mais votado foi o {opcoes_os[mais_votado[0]]}, com {mais_votado[1]}, correspondendo a {mais_votado[2]}% dos votos")