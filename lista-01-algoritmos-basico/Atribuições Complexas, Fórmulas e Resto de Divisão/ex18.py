#18. Troca de Valores: Escreva um algoritmo que leia dois valores numéricos para as variáveis A e B. Em seguida, troque os valores entre elas utilizando uma variável auxiliar e mostre os valores finais.

print('---Troca de Valores---')

a = int(input('Digite o valor de A: '))
b = int(input('Digite o valor de B: '))
temp = a
a = b
b = temp
print(f'A passou a valer {a} e B passou a valer {b}.')
