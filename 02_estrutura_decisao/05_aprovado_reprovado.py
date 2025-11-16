nota_1 = float(input("\nDigite a primeira nota: "))
nota_2 = float(input("Digite a segunda nota: "))

media = (nota_1 + nota_2) / 2

if media == 10:
    print("\nAprovado com distinção.\n")
elif media >= 7:
    print("\nAprovado.\n")
else:
    print("\nReprovado.\n")