#19. Formação de Grupos: Um professor quer dividir sua turma em grupos de 4 alunos. Leia o total de alunos na turma, calcule e mostre quantos grupos completos serão formados (divisão inteira \) e quantos alunos ficarão de fora (resto da divisão %).

total_alunos = int(input('Qual o número total de alunos? '))
grupos = total_alunos // 4
restante = total_alunos % 4
print(f'Dos {total_alunos}, foram feitos {grupos} grupos e {restante} alunos ficaram de fora.')
