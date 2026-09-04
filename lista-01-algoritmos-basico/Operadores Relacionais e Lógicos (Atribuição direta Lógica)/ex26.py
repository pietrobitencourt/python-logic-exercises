#26. Acesso a Parque de Diversões: Para entrar num brinquedo radical, a pessoa deve ter idade superior a 12 anos E altura de pelo menos 1.50 metros. Leia os valores e exiba a permissão de acesso.

print('---Montanha Russa---')
idade = int(input('Qual sua idade? '))
altura = float(input('Qual sua altura? '))
if idade > 12 and altura >= 1.50:
    print('Você tem permissão para acessar o brinquedo!')
else:
    print('Você nõa tem permissão para acessar o brinquedo!')
