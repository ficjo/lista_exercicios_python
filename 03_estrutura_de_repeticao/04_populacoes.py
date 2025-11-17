pop_pais_a = 80_000
pop_pais_b = 200_000
taxa_crescimento_a = 0.03
taxa_crescimento_b = 0.015
anos = 0

while pop_pais_a < pop_pais_b:
    anos += 1
    pop_pais_a = pop_pais_a * (1 + taxa_crescimento_a)
    pop_pais_b = pop_pais_b * (1 + taxa_crescimento_b)
    
print("\n* * * RESULTADOS * * *")
print(f"Tempo necessário para País A ultrapassar País B: {anos} anos")
print(f"População final do País A: {pop_pais_a:.0f}")
print(f"População final do País B: {pop_pais_b:.0f}\n")
