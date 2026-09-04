#16. Divisão de Conta de Pizzaria: Leia o valor total de uma conta e a quantidade de amigos na mesa. Calcule e exiba quanto cada um deverá pagar.

valor_total = float(input('Qual o valor da pizza? R$'))
amigos = int(input('Quantos amigos estão na mesa? '))
divisao = valor_total / amigos
print(f'Cada um dos {amigos} amigos deverá pagar R${divisao:.2f}.')
