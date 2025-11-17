valor_inicial = 0.0
while valor_inicial <= 0:
    valor_inicial = float(input("\nDigite o valor da dívida (R$): "))
    if valor_inicial <= 0:
        print("O valor da dívida deve ser positivo.")

parcelas_opcoes = [1, 3, 6, 9, 12]
juros_percentual = [0, 10, 15, 20, 25]

print("\n" + "=" * 75)
print(f"{'Valor da Dívida':<18} | {'Juros (R$)':<13} | {'Parcelas':<12} | {'Valor da Parcela':<20}")
print("=" * 75)

i = 0
while i < len(parcelas_opcoes):
    
    parcelas = parcelas_opcoes[i]
    percentual = juros_percentual[i] / 100.0
    
    valor_juros = valor_inicial * percentual
    valor_total = valor_inicial + valor_juros
    
    valor_parcela = valor_total / parcelas
    
    print(f"R$ {valor_total:<15.2f} | R$ {valor_juros:<10.2f} | {parcelas:<12} | R$ {valor_parcela:<15.2f}")
    
    i += 1

print("=" * 75)