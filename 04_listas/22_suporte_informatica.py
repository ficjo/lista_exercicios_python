situacoes_defeito = [
    "necessita da esfera",
    "necessita de limpeza",
    "necessita troca do cabo ou conector",
    "quebrado ou inutilizado"
]

contagem_defeitos = [0] * len(situacoes_defeito)
total_mouses = 0

print("Levantamento de Sucata de Mouses")
print("--------------------------------")
print("Situações de defeito:")
for i, situacao in enumerate(situacoes_defeito, 1):
    print(f"  {i}- {situacao}")
print("--------------------------------")

while True:
    id_mouse = int(input("Digite o número de identificação do mouse (ou 0 para encerrar): "))
    
    if id_mouse == 0:
        break 
    
    defeito = int(input(f"Digite o código do defeito (1 a {len(situacoes_defeito)}): "))
    
    if 1 <= defeito <= len(situacoes_defeito):
        contagem_defeitos[defeito - 1] += 1
        total_mouses += 1
    else:
        print("Código de defeito inválido. Tente novamente.")
            
if total_mouses == 0:
    print("\nNenhum mouse foi registrado. Encerrando.")

print("\nRelatório Final")
print(f"Quantidade de mouses: {total_mouses}")
print("\nSituação                                 Quantidade      Percentual")
print("---------------------------------------  ----------      ----------")

for i in range(len(situacoes_defeito)):
    nome_situacao = situacoes_defeito[i]
    quantidade = contagem_defeitos[i]
    
    # Cálculo do percentual
    percentual = (quantidade / total_mouses) * 100
    
    # Formatação para exibição: alinhamento à esquerda, números alinhados à direita
    print(f"{i+1}- {nome_situacao:<37} {quantidade:>10} {percentual:>15.0f}%")

print()