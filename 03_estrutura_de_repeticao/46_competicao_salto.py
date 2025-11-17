nome_atleta = ' '

while nome_atleta != '':
    nome_atleta = input("\nNome do Atleta (ou pressione Enter para sair): ")
    
    if nome_atleta == '':
        print("Programa encerrado.\n")
        break
    
    i = 1
    soma_saltos = 0.0
    melhor_salto = -1.0
    pior_salto = 9999.0
    
    print("-" * 30)

    while i <= 5:
        salto = float(input(f"{i}º Salto (metros): "))
        
        soma_saltos += salto
        
        if salto > melhor_salto:
            melhor_salto = salto
        
        if salto < pior_salto:
            pior_salto = salto
            
        i += 1
        
    soma_restante = soma_saltos - melhor_salto - pior_salto
    
    media_salto = soma_restante / 3.0
    
    print(f"\nAtleta: {nome_atleta}")
    print(f"Melhor salto: {melhor_salto:.1f} m")
    print(f"Pior salto: {pior_salto:.1f} m")
    print(f"Média dos demais saltos: {media_salto:.1f} m")
    print(f"Resultado final: {nome_atleta}: {media_salto:.1f} m\n")