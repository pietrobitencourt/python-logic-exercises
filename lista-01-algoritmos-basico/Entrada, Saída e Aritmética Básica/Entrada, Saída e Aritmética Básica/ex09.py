# 9. Conversão de Moeda: Leia um valor financeiro em Reais (R$) e a cotação atual do Dólar (US$). Calcule e mostre a quantia equivalente em dólares.

print('-Conversor de Real para Dólar-')

real = float(input('Quantos reais (R$) você quer converter? '))
cotacao_atual = float(input('Qual a cotação atual do dólar (1 USD $) para Real(BRL R$)? '))
cotacao = float(1 / cotacao_atual)
dolares = float(real * cotacao)
print('A conversão de R${} para Dólares(USD $) dá uma quantia equivalente de:USD ${}'.format(real, dolares))
