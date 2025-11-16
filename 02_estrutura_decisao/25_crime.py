respostas_positivas = 0

resp1 = input("\n1. Telefonou para a vítima? (sim/não): ").lower()
if resp1 == 'sim':
    respostas_positivas += 1
    
resp2 = input("2. Esteve no local do crime? (sim/não): ").lower()
if resp2 == 'sim':
    respostas_positivas += 1
    
resp3 = input("3. Mora perto da vítima? (sim/não): ").lower()
if resp3 == 'sim':
    respostas_positivas += 1
    
resp4 = input("4. Devia para a vítima? (sim/não): ").lower()
if resp4 == 'sim':
    respostas_positivas += 1
    
resp5 = input("5. Já trabalhou com a vítima? (sim/não): ").lower()
if resp5 == 'sim':
    respostas_positivas += 1

print("-" * 40)
print(f"Total de respostas 'sim': {respostas_positivas}")

if respostas_positivas == 5:
    classificacao = "Assassino"
elif respostas_positivas >= 3: # Inclui 3 e 4
    classificacao = "Cúmplice"
elif respostas_positivas == 2:
    classificacao = "Suspeita"
else: # 0 ou 1 resposta positiva
    classificacao = "Inocente"

print(f"RESULTADO: {classificacao}")
print("-" * 40)