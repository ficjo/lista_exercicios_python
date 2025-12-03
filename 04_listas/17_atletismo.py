print()

while True:
    nome = input("Nome do atleta [ENTER para sair]: ")
    if nome == "":
        print("\n* * PROGRAMA ENCERRADO * *\n")
        break

    saltos = []

    for i in range(5):
        distancia = float(input(f"Salto {i + 1}: "))
        saltos.append(distancia)
    
    print(f"\nAtleta: {nome}\n")

    print(f"Primeiro Salto: {saltos[0]} m")
    print(f"Segundo Salto:  {saltos[1]} m")
    print(f"Terceiro Salto: {saltos[2]} m")
    print(f"Quarto Salto:   {saltos[3]} m")
    print(f"Quinto Salto:   {saltos[4]} m")

    media = sum(saltos) / len(saltos)

    print("\nResultado final:")
    print(f"Atleta: {nome}")
    print(f"Saltos: {saltos}")
    print(f"Média dos saltos: {media:.2f}\n")