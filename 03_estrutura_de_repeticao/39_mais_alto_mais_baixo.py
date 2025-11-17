contador = 1
num_aluno_mais_alto = 0
altura_mais_alta = 0.0
num_aluno_mais_baixo = 0
altura_mais_baixa = 0.0

print("\n--- Encontrando o Aluno Mais Alto e Mais Baixo ---")

while contador <= 10:
    numero_aluno = int(input("Número do aluno: "))
    altura = float(input("Altura em centímetros: "))
    
    if contador == 1:
        num_aluno_mais_alto = numero_aluno
        altura_mais_alta = altura
        num_aluno_mais_baixo = numero_aluno
        altura_mais_baixa = altura
    else:
        if altura > altura_mais_alta:
            altura_mais_alta = altura
            num_aluno_mais_alto = numero_aluno
        
        if altura < altura_mais_baixa:
            altura_mais_baixa = altura
            num_aluno_mais_baixo = numero_aluno
            
    contador += 1

print("\n* * * RESULTADOS * * * ")
print(f"Aluno Mais Alto : Número {num_aluno_mais_alto}, Altura {altura_mais_alta:.2f} cm")
print(f"Aluno Mais Baixo: Número {num_aluno_mais_baixo}, Altura {altura_mais_baixa:.2f} cm\n")