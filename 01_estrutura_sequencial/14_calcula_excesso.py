# Usando constantes 
LIMITE_PESO = 50
VALOR_MULTA_KG = 4.00

peso = float(input("\nDigite o peso total de peixes (kg): "))

excesso = peso - LIMITE_PESO

if excesso <= 0:
    excesso = 0.0
    
multa = excesso * VALOR_MULTA_KG

print("\n* * * RESULTADO * * *")
print(f"Peso total dos peixes: {peso:.1f}kg")
print(f"Excesso de peso: {excesso} kg")
print(f"Valor da multa: R$ {multa:.2f}\n")