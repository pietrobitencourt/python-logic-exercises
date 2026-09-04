# 22) Classificação de IMC. Leia peso (kg) e altura (m), calcule o IMC e classifique: Abaixo do peso (< 18,5), Normal (18,5–24,9), Sobrepeso (25–29,9) ou Obesidade (≥ 30).

peso = float(input('Digite o seu peso (em kg): '))
altura = float(input('Digite a sua altura (em metros): '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print('Abaixo do peso')
elif 18.5 <= imc <= 24.9:
    print('Peso ideal')
elif 25 <= imc <= 29.9:
    print('Sobrepeso')
else:
    print('Obesidade')
