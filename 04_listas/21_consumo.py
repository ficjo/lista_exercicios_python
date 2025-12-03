DISTANCIA_VIAGEM = 1000 
PRECO_GASOLINA = 2.25
NUMERO_CARROS = 5

modelos = []
consumo_kml = []

print("Comparativo de Consumo de Combustível")
print("=====================================")

for i in range(1, NUMERO_CARROS + 1):
    print(f"\nVeículo {i}")
    
    while True:
        nome = input("Nome: ").strip()
        if nome:
            modelos.append(nome)
            break
        print("O nome do veículo não pode ser vazio.")
        
    while True:
        kml = float(input("Km por litro: "))
        if kml > 0:
            consumo_kml.append(kml)
            break
        else:
            print("O consumo deve ser um valor positivo.")

melhor_consumo = -1.0
modelo_mais_economico = ""

print("\nRelatório Final")

for i in range(NUMERO_CARROS):
    modelo = modelos[i]
    kml = consumo_kml[i]
    
    litros_gastos = DISTANCIA_VIAGEM / kml
    custo_total = litros_gastos * PRECO_GASOLINA
    
    if kml > melhor_consumo:
        melhor_consumo = kml
        modelo_mais_economico = modelo
        
    print(f"{i+1:2} - {modelo:<15} - {kml:>5.1f} - {litros_gastos:>5.1f} litros - R$ {custo_total:>6.2f}")

print(f"\nO menor consumo é do **{modelo_mais_economico.lower()}**.")
