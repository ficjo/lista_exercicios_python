contador = 1
total_veiculos = 0
total_acidentes_menor_2000 = 0
cidades_menor_2000 = 0

maior_indice = -1.0
cidade_maior_indice = 0

menor_indice = 99999999.0
cidade_menor_indice = 0

print("--- Estatística de Trânsito em 5 Cidades ---")

while contador <= 5:
    print(f"\nDados da Cidade {contador}:")
    
    codigo_cidade = int(input("Código da cidade: "))
    num_veiculos = int(input("Número de veículos de passeio (1999): "))
    num_acidentes = int(input("Número de acidentes com vítimas (1999): "))
    
    if num_veiculos > 0:
        indice_acidentes = num_acidentes / num_veiculos
    else:
        indice_acidentes = 0 

    if indice_acidentes > maior_indice:
        maior_indice = indice_acidentes
        cidade_maior_indice = codigo_cidade
        
    if indice_acidentes < menor_indice:
        menor_indice = indice_acidentes
        cidade_menor_indice = codigo_cidade
        
    total_veiculos += num_veiculos
    
    if num_veiculos < 2000:
        total_acidentes_menor_2000 += num_acidentes
        cidades_menor_2000 += 1
        
    contador += 1

print("\nESTATÍSTICAS\n")

print("\n[Índice de Acidentes por Veículo]")
print(f"Maior Índice: {maior_indice:.2f} (Código da Cidade: {cidade_maior_indice})")
print(f"Menor Índice: {menor_indice:.2f} (Código da Cidade: {cidade_menor_indice})")

media_veiculos = total_veiculos / 5
print(f"\nMédia de Veículos de Passeio nas 5 cidades: {media_veiculos:.2f}")

print("\n[Média de Acidentes em Cidades Pequenas (< 2000 Veículos)]")
if cidades_menor_2000 > 0:
    media_acidentes_pequenas = total_acidentes_menor_2000 / cidades_menor_2000
    print(f"Total de cidades com < 2000 veículos: {cidades_menor_2000}")
    print(f"Média de Acidentes nessas cidades: {media_acidentes_pequenas:.2f}")
else:
    print("Nenhuma cidade registrada com menos de 2.000 veículos.")
    
print()