#24. Operadores Lógicos (Aprovação): Uma escola exige média igual ou superior a 7.0 E frequência igual ou superior a 75%. Leia os dois dados e exiba o status lógico de aprovação.

nota1 = float(input("Digite a sua primeira nota: "))
nota2 = float(input("Digite a sua segunda nota: "))
nota3 = float(input("Digite a sua terceira nota: "))
media = (nota1 + nota2 + nota3) / 3
total_aulas = int(input('Digite o total de aulas que você teve: '))
faltas = int(input('Digite o total de faltas que você teve: '))
frequencia = ((total_aulas - faltas) / total_aulas) * 100

if media >= 7.0 and frequencia >= 75:
    print(f'Você está aprovado! Média {media:.2f} e Frequência {frequencia:.2f}%.')
elif media >= 5 and frequencia >= 70:
    print(f'Você está de recuperação! Média {media:.2f} e Frequência {frequencia:.2f}%.')
else:
    print(f'Você está reprovado! Média {media:.2f} e Frequência {frequencia:.2f}%.')
