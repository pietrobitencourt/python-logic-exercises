# 4) Detectar febre. Leia a temperatura corporal (em °C) e exiba "Atenção: você está com febre!" se for superior a 37,5 °C.

temperatura = float(input('Digite a sua temperatura corporal (ºC): '))
if temperatura > 37.5:
    print('Você está com febre.')
else:
    print('Você não está com febre.')
