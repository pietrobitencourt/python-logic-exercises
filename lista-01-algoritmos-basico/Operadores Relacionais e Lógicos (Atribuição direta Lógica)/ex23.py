#23. Verificação de Número Par: Leia um número inteiro. Utilize o operador de resto da divisão por 2 e o operador de igualdade para verificar e exibir se o número é par.

inteiro = int(input('Digite um número: '))
par = inteiro % 2
if par == 0:
    print('É um número par.')
else:
    print('É um número ímpar.')
