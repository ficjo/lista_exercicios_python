nota_1 = float(input("\nDigite a primeira nota: "))
nota_2 = float(input("Digite a segunda nota: "))
nota_3 = float(input("Digite a terceira nota: "))

media = (nota_1 + nota_2 + nota_3) / 3

print(f"\nMédia: {media:.2f}")

if media == 10.0:
    print("Aprovado com Distinção")
elif media >= 7.0:
    print("Aprovado")
else:
    print("Reprovado")

print()