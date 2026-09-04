# 19) Troco ou valor insuficiente. Leia o preço de um produto e o valor pago. Se o pagamento for suficiente, exiba o troco; caso contrário, informe quanto falta.

produto = 25
pagamento = float(input('Qual será o valor pago? R$'))
troco = pagamento - produto
valor_insuficiente = produto - pagamento
if pagamento > produto:
    print(f'Seu troco é de R${troco:.2f}.')
elif pagamento < produto:
    print(f'Ainda falta R${valor_insuficiente:.2f}.')
else:
    print('Tudo certo! Tenha um ótimo dia.')
