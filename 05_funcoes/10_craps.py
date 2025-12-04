import random

def lancar_dados():
    dado_1 = random.randint(1, 6)
    dado_2 = random.randint(1, 6)
    soma = dado_1 + dado_2
    return soma

def jogar_craps():
    ponto = 0

    resultado = lancar_dados()
    print(f"Primeiro lançamento: {resultado}")

    if resultado in (7, 11):
        print("NATURAL! Venceu!")
        return
    
    elif resultado in (2, 3, 12):
        print("CRAPS! Perdeu!")
        return
    
    else:
        ponto = resultado
        print(f"Seu ponto é {ponto}. Continue jogando.")
    
    while True:
        resultado = lancar_dados()
        print(f"Próximo lançamento: {resultado}")

        if resultado == ponto:
            print(f"Acertou o ponto ({ponto})! Venceu!")
            break
        elif resultado == 7:
            print("Tirou 7 antes do ponto. Perdeu!")
            break

print("\nCRAPS\n")

while True:
    jogar_craps()

    jogar_novamente = input("\nDeseja jogar novamente? (s/n): ").strip().lower()
    if jogar_novamente != 's':
        break

print("\nPrograma encerrado.\n")
