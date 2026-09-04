# 16) Febre ou normal. Leia a temperatura corporal (em °C) e informe se a pessoa está com febre (acima de 37,5 °C) ou com temperatura normal.

temperatura = float(input('Digite a sua temperatura (ºC): '))
if temperatura > 37.5:
    print('Você está com febre!')
else:
    print('Você está com a temperatura normal!')
