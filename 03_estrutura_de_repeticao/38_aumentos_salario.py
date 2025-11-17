# Coloquei o ano em 2000 pois se fosse o ano atual, o valor
# ... ficaria MUITO alto.
ANO_ATUAL = 2000

print("\n* * * PARTE 1: Salário Inicial Fixo * * *")

salario = 1000.00
percentual = 0.015
ano_calculo = 1996

while ano_calculo <= ANO_ATUAL:
    
    aumento = salario * percentual
    salario += aumento
    
    if ano_calculo >= 1997:
        percentual *= 2
        
    ano_calculo += 1

print(f"O salário atual (2025) é de: R$ {salario:.2f}")

# -------------------------------------------------------------- 

print("\n* * * PARTE 2: Salário Inicial Variável * * *")

while True:
    try:
        salario_inicial = float(input("Digite o salário inicial (Ex: 1000.00): R$ "))
        if salario_inicial > 0:
            break
        else:
            print("O salário deve ser positivo.")
    except ValueError:
        print("Entrada inválida. Digite um valor numérico.")

salario = salario_inicial
percentual = 0.015 
ano_calculo = 1996

while ano_calculo <= ANO_ATUAL:
    
    aumento = salario * percentual
    salario += aumento
    
    if ano_calculo >= 1997:
        percentual *= 2
        
    ano_calculo += 1

print(f"Com salário inicial de R$ {salario_inicial:.2f}, o salário atual (2025) é de: R$ {salario:.2f}\n")