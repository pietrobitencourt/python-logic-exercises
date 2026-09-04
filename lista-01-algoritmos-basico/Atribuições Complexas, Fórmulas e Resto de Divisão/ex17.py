#17. Juros Simples: Leia um valor de capital, uma taxa de juros mensal (em porcentagem) e o tempo em meses. Calcule os juros rendidos e o valor final (Capital + Juros).

capital = float(input('Qual o valor do capital? R$'))
taxa = float(input('Qual a taxa de juros (% ao mês): '))
tempo = float(input('Qual será o total de meses? '))
taxa_decimal = taxa / 100
juros = capital * taxa_decimal * tempo
montante = capital + juros
print(f'Os juros rendidos foram de R${juros:.2f} e o valor final de R${montante:.2f}.')

