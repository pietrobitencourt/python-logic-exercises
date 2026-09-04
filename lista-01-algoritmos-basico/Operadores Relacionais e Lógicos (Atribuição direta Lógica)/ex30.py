#30. Validação de Triângulo: Para existir um triângulo, qualquer lado deve ser sempre menor que a soma dos outros dois. Leia 3 lados (A, B e C) e construa uma expressão (A < B+C E B < A+C E C < A+B) para exibir se formam um triângulo válido.

a = int(input('Digite o lado A: '))
b = int(input('Digite o lado B: '))
c = int(input('Digite o lado C: '))
valido = (a < b + c) and (b < a + c) and (c < a + b)
if valido:
    print('Triângulo válido.')
else:
    print('Triângulo inválido.')
