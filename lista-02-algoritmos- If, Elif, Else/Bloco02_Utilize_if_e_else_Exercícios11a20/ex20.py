# 20) Triângulo válido. Leia três valores representando lados de um triângulo. Informe se eles podem ou não formar um triângulo (cada lado deve ser menor que a soma dos outros dois).

lado_a = float(input('Digite a medida do lado a do triângulo (em cm): '))
lado_b = float(input('Digite a medida do lado b do triângulo (em cm): '))
lado_c = float(input('Digite a medida do lado c do triângulo (em cm): '))
valido = (lado_a < lado_b + lado_c) and (lado_b < lado_a + lado_c) and (lado_c < lado_a + lado_b)
if valido:
    print('Eles formam um triângulo válido!')
else:
    print('Eles não formam um triângulo válido!')
