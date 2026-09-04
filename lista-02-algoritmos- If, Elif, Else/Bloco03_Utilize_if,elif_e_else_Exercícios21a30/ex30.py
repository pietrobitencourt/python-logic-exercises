# 30) Classificação de triângulo por lados. Leia três valores. Primeiro verifique se formam um
# triângulo válido. Se formarem, classifique-o como Equilátero (3 lados iguais), Isósceles (2 lados
# iguais) ou Escaleno (todos diferentes).

try:
    lado_a = int(input('Digite o valor do lado A (em cm): '))
    lado_b = int(input('Digite o valor do lado B (em cm): '))
    lado_c = int(input('Digite o valor do lado (em cm): '))

    valido = (lado_a < lado_b + lado_c) and (lado_b < lado_a + lado_c) and (lado_c < lado_a + lado_b)
    if valido:
        if lado_a == lado_b == lado_c:
            print('Triângulo Equilátero')
        elif lado_a == lado_b or lado_a == lado_c or lado_b == lado_c:
            print('Triângulo Isósceles')
        else:
            print('Triângulo Escaleno')
    else:
        print('Triângulo inválido!')

except ValueError:
    print('Valor invalido')