nota = -1

print()

while nota < 0 or nota > 10:
    nota = float(input("Digite uma nota [entre 0 e 10]: "))
    if nota < 0 or nota > 10:
        print("Tente novamente! Apenas valores entre 0 e 10!\n")

print()
print(f"Nota aceita: {nota:.2f}")
print()