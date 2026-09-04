# 25) Menu de lanchonete. Exiba um menu com 4 opções numeradas (lanche, suco, café, água) e
# seus preços. Leia a opção e exiba o item escolhido com o valor. Se a opção for inválida, avise o
# usuário.

try:
    print('----------MENU----------')
    print('[ 1 ] LANCHE -> R$6,00')
    print('[ 2 ] SUCO -> R$2,00')
    print('[ 3 ] CAFÉ -> R$0,99')
    print('[ 4 ] ÁGUA -> R$3,00')

    print('-=-'*8)

    escolha = int(input('Qual a sua escolha? '))
    if escolha < 1 or escolha > 4:
        print('Escolha invalida!')
    elif escolha == 1:
        print('Item escolhido: Lanche - O preço é de R$6,00')
    elif escolha == 2:
        print('Item escolhido: Suco - O preço é de R$2,00')
    elif escolha == 3:
        print('Item escolhido: Café - seu preço é de R$0,99')
    else:
        print('Item escolhido: agua - R$3,00')

except ValueError:
    print('Valor invalido! Não digite letras na sua escolha.')

