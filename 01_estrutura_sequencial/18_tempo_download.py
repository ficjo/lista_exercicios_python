tamanho_mb = float(input("\nDigite o tamanho do arquivo (mb): "))
velocidade_mbps = float(input("Digite a velocidade da internet (mbps): "))

tamanho_megabits = tamanho_mb * 8
tempo_segundos = tamanho_megabits / velocidade_mbps
tempo_minutos = tempo_segundos / 60

print(f"\nTempo aproximado de donwload: {tempo_minutos:.2f}\n")