#29. Voto Obrigatório: A lei determina que o voto é obrigatório para pessoas que possuam entre 18 e 69 anos (inclusive). Leia a idade, valide os limites com a operação lógica E e exiba o resultado.

idade = int(input('Digite sua idade: '))
if idade >= 18 and idade <= 69:
    print('Voto Obrigatório!')
else:
    print('Voto não obrigatório!')
