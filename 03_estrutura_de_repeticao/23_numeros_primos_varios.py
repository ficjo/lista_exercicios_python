N = 0
while N < 2:
    N = int(input("\nDigite um número inteiro (N) para o limite superior: "))
    if N < 2:
        print("N deve ser maior ou igual a 2.")

total_divisoes = 0
primos_encontrados = ""
numero = 2 

print("-" * 50)
print(f"Números primos entre 1 e {N}:")

while numero <= N:
    eh_primo = True
    divisor = 2
    
    while divisor < numero:
        total_divisoes += 1 
        
        if numero % divisor == 0:
            eh_primo = False
            break
            
        divisor += 1
        
    if eh_primo:
        if primos_encontrados == "":
            primos_encontrados = str(numero)
        else:
            primos_encontrados += f", {numero}"
            
    numero += 1 
    
print(primos_encontrados)
print("-" * 50)
print(f"Total de testes (divisões) executados: {total_divisoes}")
print("-" * 50)