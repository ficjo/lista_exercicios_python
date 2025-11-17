print()

while True: 
    num = -1
    while num < 0 or num > 15:
        num = int(input("Digite um número inteiro positivo (0 a 15) para calcular o fatorial: "))
        if num < 0 or num > 15:
            print("ERRO: O número deve ser inteiro, positivo e menor ou igual a 15.")

    fatorial = 1

    if num > 1:
        print(f"\n{num}! = {num}", end = "")
        
        contador_impressao = num - 1
        while contador_impressao >= 1:
            print(f" * {contador_impressao}", end = "")
            contador_impressao -= 1
            
        temp_contador = num
        while temp_contador > 0:
            fatorial *= temp_contador
            temp_contador -= 1
        
        print(f" = {fatorial}\n")

    elif num >= 0:
        if num == 0:
            fatorial = 1
        else:
            fatorial = 1
            
        print(f"\n{num}! = {fatorial}\n")
    
    
    print("-" * 50)
    continuar = input("Deseja calcular outro fatorial? (S/N): ").upper()
    if continuar != 'S':
        print("\nPrograma encerrado.\n")
        break