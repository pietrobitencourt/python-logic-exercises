# 12. Idade em Dias: Crie um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias (considere que um ano tem 365 dias e um mês 30 dias). Exiba a idade convertida totalmente em dias.

print('-Calculador de dias de vida_')

dia = int(input('Digite o dia do seu aniversário: '))
mes = int(input('Digite o mês de seu aniversário: '))
ano = int(input('Digite o ano de seu aniversário: '))
total_nascimento = (ano * 365) + (mes * 30) + dia
dia_hoje = int(input('Qual o dia de hoje? '))
mes_hoje = int(input('Em que mês estamos? '))
ano_hoje = int(input('Em qual ano estamos? '))
total_hoje = (ano_hoje * 365) + (mes_hoje * 30) + dia_hoje
total_dias =  int(total_hoje - total_nascimento)
print('Você viveu aproximadamente: {} dias!'.format(total_dias))
