# 28) Semáforo. Leia a cor do semáforo (verde, amarelo ou vermelho) e exiba a ação correspondente: Siga em frente, Atenção ou Pare.

try:
    semaforo = input('Qual a cor do semáforo (Verde/Amarelo/Vermelho)? ').lower().strip()

    if semaforo == 'verde':
        print('O sinal está verde: Siga em frente.')
    elif semaforo == 'amarelo':
        print('O sinal está amarelo: Atenção.')
    elif semaforo == 'vermelho':
        print('O sinal está vermelho: Pare.')
    else:
        print('Sinal inválido')

except ValueError:
    print('Valor inválido')