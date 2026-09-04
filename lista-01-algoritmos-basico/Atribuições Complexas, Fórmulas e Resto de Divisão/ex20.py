#20. Conversão de Minutos: Leia uma quantidade de tempo inteira expressa apenas em minutos. Transforme e exiba esse valor convertido para Horas e Minutos restantes (Ex: 130 min = 2h e 10min).

tempo = int(input('Qual a quantidade de minutos gastos? '))
hora = tempo // 60
minuto = tempo % 60
print(f'{tempo}min: {hora} horas e {minuto} minutos')
