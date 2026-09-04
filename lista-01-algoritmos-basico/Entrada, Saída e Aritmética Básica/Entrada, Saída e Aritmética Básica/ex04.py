# 4.  Média de Três Notas: Escreva um algoritmo que leia três notas de um aluno, calcule e exiba a média aritmética simples entre elas.

print('Qual a média de suas três notas nesse ano?')
nota1 = float(input('Digite a sua primeira nota: '))
nota2 = float(input('Digite a sua segunda nota: '))
nota3 = float(input('Digite a sua terceira nota: '))
media = (nota1 + nota2 + nota3) / 3
print('A média aritmética de suas três notas é de: {}.'.format(media))
