codigo = 1
total_clientes = 0
soma_alturas = 0
soma_pesos = 0

mais_alto_codigo = 0
mais_alto_valor = 0

mais_baixo_codigo = 0
mais_baixo_valor = 0

mais_gordo_codigo = 0
mais_gordo_valor = 0

mais_magro_codigo = 0
mais_magro_valor = 0

contador = 1

while True:
    codigo = int(input("\nDigite o código: "))
    
    if codigo == 0:
        break
    
    altura = float(input("Altura: "))
    peso = float(input("Peso: "))

    total_clientes += 1
    soma_alturas += altura
    soma_pesos += peso
    
    if contador == 1:
        mais_alto_codigo = codigo
        mais_alto_valor = altura
        mais_baixo_codigo = codigo
        mais_baixo_valor = altura
        mais_gordo_codigo = codigo
        mais_gordo_valor = peso
        mais_magro_codigo = codigo
        mais_magro_valor = peso
    else:
        if altura >= mais_alto_valor:
            mais_alto_valor = altura
            mais_alto_codigo = codigo
        if altura <= mais_baixo_valor:
            mais_baixo_valor = altura
            mais_baixo_codigo = codigo
        if peso >= mais_gordo_valor:
            mais_gordo_valor = peso    
            mais_gordo_codigo = codigo
        if peso <= mais_magro_valor:
            mais_magro_valor = peso
            mais_magro_codigo = codigo
    contador += 1

media_alturas = soma_alturas / total_clientes
media_pesos = soma_pesos / total_clientes

print("\n* * * RESULTADOS * * *")
print(f"Mais Alto           : COD. {mais_alto_codigo} | {mais_alto_valor:.2f}m")
print(f"Mais Baixo          : COD. {mais_baixo_codigo} | {mais_baixo_valor:.2f}m")
print(f"Mais Gordo          : COD. {mais_gordo_codigo} | {mais_baixo_valor:.2f}kg")
print(f"Mais Magro          : COD. {mais_magro_codigo} | {mais_magro_valor:.2f}")
print(f"Média das Alturas   : {media_alturas:.2f}m")
print(f"Média dos pesos     : {media_pesos}kg\n")
        