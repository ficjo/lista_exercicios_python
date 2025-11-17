usuario = ""
senha = ""

print()

while senha == usuario:
    usuario = input("Digite o nome do usuário: ")
    senha = input("Digite a senha: ")
    
    if senha == usuario:
        print("ERRO! A senha não pode ser igual ao usuário! Tente novamente!\n")

print(f"\nUsuário cadastrado: {usuario}")
print(f"Senha: {'*' * len(senha)}\n")