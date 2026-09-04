#28. Desconto na Compra: Uma loja oferece desconto se o valor da compra for maior que R$ 500,00 OU se o cliente for "VIP" (dado lógico). Leia o valor e o status VIP e exiba o direito ao desconto.

valor = float(input(f'Digite o valor de sua compra: R$'))
client_vip = input('Você é um cliente VIP? [S/N]').upper()
if valor >= 500.00 or client_vip == 'S':
    print('Você tem direito a desconto em seu produto!')
else:
    print('Você não tem direito a desconto em seu produto!')
