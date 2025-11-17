gabarito = ['A', 'B', 'C', 'D', 'E', 'E', 'D', 'C', 'B', 'A']
num_questoes = 10

total_alunos = 0
soma_notas = 0.0
maior_acerto = -1
menor_acerto = num_questoes + 1 

print("\nGabarito fixo: A, B, C, D, E, E, D, C, B, A")

while True:
    print(f"ALUNO {total_alunos + 1} - INÍCIO DA PROVA")
    
    acertos = 0
    i = 1
    
    while i <= num_questoes:
        resposta_aluno = input(f"Resposta da questão {i}: ").upper()
        
        if resposta_aluno == gabarito[i - 1]:
            acertos += 1
            
        i += 1
        
    total_alunos += 1
    soma_notas += acertos
    
    if acertos > maior_acerto:
        maior_acerto = acertos
        
    if acertos < menor_acerto:
        menor_acerto = acertos
        
    print(f"Total de acertos do aluno: {acertos} de {num_questoes}")
    
    continuar = input("Outro aluno vai utilizar o sistema? (S/N): ").upper()
    if continuar != 'S':
        break

print("\n* * * Resultados * * *")

if total_alunos > 0:
    media_notas = soma_notas / total_alunos
    
    print(f"Maior Acerto            : {maior_acerto}")
    print(f"Menor Acerto            : {menor_acerto}")
    print(f"Total de Alunos         : {total_alunos}")
    print(f"Média das Notas da Turma: {media_notas:.2f}")
else:
    print("Nenhum aluno utilizou o sistema.")
    
print()