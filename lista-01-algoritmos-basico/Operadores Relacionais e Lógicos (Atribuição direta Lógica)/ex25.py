#25. Critério de Empréstimo: Um banco aprova empréstimos para clientes que tenham salário superior a R$ 2.500,00 E nome limpo. Leia o salário e um valor lógico (verdadeiro/falso) referente ao nome e exiba o resultado.

salario = float(input('Digite o seu salário: R$'))
nome_limpo = salario >= 0
nome_sujo = salario < 0
aprovado = salario >= 2500 and nome_limpo
if aprovado:
    print('Seu empréstimo foi aprovado!')
else:
    print('Seu empréstimo não foi aprovado!')
