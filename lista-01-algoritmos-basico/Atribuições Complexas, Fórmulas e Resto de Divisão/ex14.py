# 14. Desconto Simples em Produto: O preço de um produto na vitrine sofreu uma redução de 10%. Leia o preço original, calcule o valor do desconto e mostre o preço final a pagar.

print('Mercadão do Tião')
produto = float(input('Quanto custa esse produto? '))
desconto = float(input('Quantos % de desconto tem esse produto? '))
novo_preço = produto - (produto * (desconto / 100))
print(f'O seu produto custa R${produto:.2f}. Com um desconto de {desconto:.0f}%, tera um preço de R${novo_preço:.2f}.')
