"""
Como estou seguindo a ordem de estudos e funções e arquivos são 
assuntos futuros, resolvi esse exercício usando apenas listas.
"""

# Simula o txt
dados_brutos = [
    ("alexandre", 456123789),
    ("anderson", 1245698456),
    ("antonio", 123456456),
    ("carlos", 91257581),
    ("cesar", 987458),
    ("rosemary", 789456125)
]

BYTE_TO_MB = 1024 * 1024

usuarios = []
espacos_mb = []
total_bytes = 0

for nome, espaco_bytes in dados_brutos:
    total_bytes += espaco_bytes   
    espaco_mb = espaco_bytes / BYTE_TO_MB
    usuarios.append(nome)
    espacos_mb.append(espaco_mb)

total_mb = total_bytes / BYTE_TO_MB
num_usuarios = len(usuarios)
espaco_medio_mb = total_mb / num_usuarios if num_usuarios > 0 else 0

print("\nACME Inc.              Uso do espaço em disco pelos usuários")
print("------------------------------------------------------------------------")
print("Nr. Usuário        Espaço utilizado     % do uso")

for i in range(num_usuarios):
    nome = usuarios[i]
    espaco = espacos_mb[i]
    percentual_uso = (espaco / total_mb) * 100
    
    print(
        f"{i+1:<3} {nome:<15} {espaco:>10.2f} MB         {percentual_uso:>6.2f}%"
    )

print("------------------------------------------------------------------------")
print(f"Espaço total ocupado: {total_mb:.2f} MB")
print(f"Espaço médio ocupado: {espaco_medio_mb:.2f} MB\n")