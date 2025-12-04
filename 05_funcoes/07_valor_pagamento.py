def valor_pagamento(valor_prestacao, dias_atraso):
    if dias_atraso > 0:
        multa = valor_prestacao * 0.03
        juros_diario = valor_prestacao * 0.001
        juros_total = juros_diario * dias_atraso
        valor_a_pagar = valor_prestacao + multa + juros_total
    else:
        valor_a_pagar = valor_prestacao
        
    return valor_a_pagar

total_prestacoes = 0
valor_total_pago = 0.0

print("Cálculo de Prestação em Atraso")

while True:
    valor = float(input("\nValor da prestação (ou 0 para encerrar): "))

    if valor == 0:
        break

    dias = int(input("Número de dias em atraso: "))
    
    if dias < 0:
        print("O número de dias em atraso não pode ser negativo.")
        continue

    valor_final = valor_pagamento(valor, dias)
    
    print(f"Valor a ser pago: R$ {valor_final:.2f}")

    total_prestacoes += 1
    valor_total_pago += valor_final

    print("\n------------------------------")
    print("## Relatório do Dia")
    print(f"Total de prestações pagas: {total_prestacoes}")
    print(f"Valor total arrecadado: R$ {valor_total_pago:.2f}")
