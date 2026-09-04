# 6.  Consumo Médio de Combustível: Leia a distância total percorrida por um automóvel (km) e o total de combustível consumido (litros). Calcule e exiba o consumo médio (km/l).

print('Medidor de consumo médio de combustível em km/l:')

distancia_total = float(input('Qual a distância total percorrida pelo seu veículo em Km? '))
total_consumido = float(input('Qual a quantidade total de combustível consumido pelo seu veículo em lítros? '))
consumo_medio = float(distancia_total / total_consumido)
print('O consumo médio feito por um veículo que percorreu uma distância de {} Km com um consumo de {} l é de: {} Km/l.'.format(distancia_total, total_consumido, consumo_medio))