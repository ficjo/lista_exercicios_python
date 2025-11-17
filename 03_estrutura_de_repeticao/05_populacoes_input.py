
while True:
    print("\n" + "=" * 50)
    print("\nCálculo de Crescimento Populacional")
    
    populacao_a = 0
    taxa_a_percentual = -1.0
    while populacao_a <= 0 or taxa_a_percentual < 0:
        populacao_a = int(input("\nPopulação inicial do País A: "))
        taxa_a_percentual = float(input("Taxa de crescimento anual de A (em %): "))
        if populacao_a <= 0 or taxa_a_percentual < 0:
            print("Erro: População deve ser positiva e a taxa não pode ser negativa. Tente novamente.")
            
    taxa_a = taxa_a_percentual / 100

    populacao_b = 0
    taxa_b_percentual = -1.0
    while populacao_b <= populacao_a or taxa_b_percentual < 0:
        populacao_b = int(input("\nPopulação inicial do País B: "))
        taxa_b_percentual = float(input("Taxa de crescimento anual de B (em %): "))
        
        if populacao_b <= populacao_a or taxa_b_percentual < 0:
            print("Erro: População B deve ser maior que a População A e a taxa não pode ser negativa. Tente novamente.")
            
    taxa_b = taxa_b_percentual / 100

    anos = 0
    
    if taxa_a <= taxa_b:
        print("\nO País A nunca irá ultrapassar o País B, pois sua taxa é menor ou igual.")
    else:
        while populacao_a < populacao_b:
            anos += 1
            populacao_a = populacao_a * (1 + taxa_a)
            populacao_b = populacao_b * (1 + taxa_b)

        print("\n--- Resultado ---")
        print(f"Taxa de A: {taxa_a_percentual:.2f}% | População A final: {populacao_a:.0f} habitantes")
        print(f"Taxa de B: {taxa_b_percentual:.2f}% | População B final: {populacao_b:.0f} habitantes")
        print(f"Serão necessários **{anos} anos** para a População A ultrapassar a População B.")

    continuar = input("\nDeseja repetir o cálculo? (S/N): ").upper()
    if continuar != 'S':
        print("\nPrograma encerrado.")
        break