while True:
    
    nome_atleta = input("\nNome do Ginasta (ou pressione Enter para sair): ")
    
    if nome_atleta == '':
        print("Programa encerrado.\n")
        break
    
    i = 1
    soma_notas = 0.0
    melhor_nota = -1.0
    pior_nota = 11.0
    
    print("-" * 30)

    while i <= 7:
        nota_str = input(f"Nota do {i}º jurado: ")
        nota = float(nota_str)
        
        if 0 <= nota <= 10:
            
            soma_notas += nota
            
            if nota > melhor_nota:
                melhor_nota = nota
            
            if nota < pior_nota:
                pior_nota = nota
                
            i += 1
        else:
            print("Nota inválida. Digite um valor entre 0 e 10.")

    soma_restante = soma_notas - melhor_nota - pior_nota
    
    media_final = soma_restante / 5.0
    
    print("\nResultado final:")
    print(f"Atleta      : {nome_atleta}")
    print(f"Melhor nota : {melhor_nota:.1f}")
    print(f"Pior nota   : {pior_nota:.1f}")
    print(f"Média       : {media_final:.2f}\n")