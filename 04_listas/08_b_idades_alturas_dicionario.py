pessoas = []

print() 

for i in range(5):
    print(f"Pessoa {i + 1}:")
    
    idade = int(input("Idade: "))
    altura = float(input("Altura: "))

    pessoa = {
        "idade": idade,
        "altura": altura
    }

    pessoas.append(pessoa)

print(f"\nOrdem inversa:\n")

for pessoa in pessoas[::-1]:
    print(f"Idade: {pessoa.get("idade")}")
    print(f"Altura: {pessoa.get("altura")}")

print()