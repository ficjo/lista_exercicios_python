def soma_imposto(taxa_imposto, custo):
    taxa_decimal = taxa_imposto / 100
    valor_imposto = custo * taxa_decimal
    custo_com_imposto = custo + valor_imposto
    return custo_com_imposto

custo_original = 100.00
imposto_aplicado = 15.0 

novo_custo = soma_imposto(imposto_aplicado, custo_original)

print("\nCálculo de Imposto sobre Vendas")
print(f"Custo original do item: R$ {custo_original:.2f}")
print(f"Taxa de imposto aplicada: {imposto_aplicado:.2f}%")
print(f"O custo final, incluindo o imposto, é: R$ {novo_custo:.2f}\n")