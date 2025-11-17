soma_turmas = 0
num_turmas = int(input("\nDigite o número de turmas: "))

contador = 1

while contador <= num_turmas:
    num_alunos = int(input(f"Número de alunos da {contador}ª turma: "))
    if 0 <= num_alunos <= 40:
        soma_turmas += num_alunos
        contador += 1
    else:
        print("ERRO: A turma deve ter até 40 alunos.")
        
media_alunos = soma_turmas / num_turmas

print("\n* * * RESULTADOS * * *")
print(f"Total de turmas             : {num_turmas}")
print(f"Total de alunos             : {soma_turmas}")
print(f"Média de alunos por turma   : {media_alunos:.1f}")