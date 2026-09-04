#27. Isenção de Taxa de Concurso: Um edital isenta a taxa para candidatos com 65 anos ou mais OU desempregados (dado lógico). Leia as variáveis e exiba a validação lógica.

print('--Concurso Público--')
print('Candidatos com mais de 65 anos ou mais OU desempregados são isentos de taxa.')
idade = int(input('Digite sua idade: '))
desempregado = input('Está desempregado? (s/n): ').lower()
if idade >= 65 and desempregado == 's':
    print('Você está isento da taxa!')
elif idade >= 65 and desempregado == 'n':
    print('Você está isento da taxa!')
elif idade <= 65 and desempregado == 's':
    print('Você está isento da taxa!')
else:
    print('Você não está isento da taxa!')
