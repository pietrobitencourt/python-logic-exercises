# 5.  Velocidade Média: Um carro viajou entre duas cidades. Leia a distância percorrida (em km) e o tempo gasto (em horas). Calcule e exiba a velocidade média do veículo.

print('Medidor de velocidade média:')
distancia_percorrida = float(input('Qual a distância percorrida em Km? '))
tempo_gasto = float(input('Qual o tempo gasto nessa viagem em horas? '))
velocidade_media = float(distancia_percorrida / tempo_gasto)

print('A velocidade média percorrida em uma viagem de {} Km, com um tempo gasto de {}h é de: Vm = {} km/h.'.format(distancia_percorrida, tempo_gasto, velocidade_media))
