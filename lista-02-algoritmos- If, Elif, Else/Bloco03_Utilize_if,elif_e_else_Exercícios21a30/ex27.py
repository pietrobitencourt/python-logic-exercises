# 27) Estação do ano pelo mês. Leia o número do mês (1–12) e exiba a estação do ano aproximada
# no hemisfério sul: Verão (dez–fev), Outono (mar–mai), Inverno (jun–ago), Primavera (set–nov).

try:
    print('----------Estações do Ano----------')
    print('[ 1 ] [ 2 ] [ 3 ] [ 4 ] [ 5 ] [ 6 ] [ 7 ] [ 8 ] [ 9 ] [ 10 ] [ 11 ] [ 12 ]')
    print('[ Janeiro ], [ Fevereiro ], [ Março ], [ Abril ], [ Junho ], [ Julho ]')
    print('[ Agosto ], [ Setembro ], [ Outubro], [ Novembro], [ Dezembro ]')
    print('-=-'*8)

    mes = int(input('Digite o mês (1-12): '))

    if mes == 12 or mes == 1 or mes == 2:
        print('Estamos na estação de Verâo!')
    elif mes == 3 or mes == 4 or mes == 5:
        print('Estamos na estação de Outono!')
    elif mes == 6 or mes == 7 or mes == 8:
        print('Estamos na estação de Inverno!')
    elif mes == 9 or mes == 10 or mes == 11:
        print('Estamos na estação de Primavera!')
    else:
        print('Mês inválido!')

except ValueError:
    print('Valor invalido!')