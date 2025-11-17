soma = 0
jovens = 0
adultos = 0
idosos = 0
str_resultado = ""
# if 0 <= num <= 1000:   
num_pessoas = int(input("\nDigite o número de pessoas: "))

for i in range(num_pessoas):
    idade = int(input(f"Digite a idade da {i + 1}ª pessoa: "))
    soma += idade
    if 0 <= idade <= 25:
        jovens += 1
    elif 25 < idade <= 60:
        adultos += 1
    else:
        idosos += 1
        
media = soma / num_pessoas

if 0 <= media <= 25:
    str_resultado = "JOVEM"
elif 25 < idade <= 60:
    str_resultado = "ADULTA"
else:
    str_resultado = "IDOSA"

print("\n* * * RESULTADOS * * *")
print(f"Soma das idades     : {soma}")
print(f"Média das idades    : {media:.2f}")
print(f"Total de jovens     : {jovens}")
print(f"Total de adultos    : {adultos}")
print(f"Todal de idosos     : {idosos}")
print(f"A turma é           : {str_resultado}\n")