# 24) Sensação térmica. Leia a temperatura (°C) e classifique: Gelado (≤ 0), Frio (1–15), Agradável (16–25), Quente (26–35) ou Muito quente (> 35).

try:
    temperatura = float(input('Digite a temperatura atual: '))

    if temperatura < 1:
        print('Gelado')
    elif temperatura <= 15:
        print('Frio')
    elif temperatura <= 25:
        print('Agradável')
    elif temperatura <= 35:
        print('Quente')
    else:
        print('Muito Quente!')

except ValueError:
    print('Valor invalido')
