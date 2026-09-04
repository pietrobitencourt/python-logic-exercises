# 29) Pedra, papel e tesoura. Leia a jogada do jogador 1 e do jogador 2 (pedra, papel ou tesoura). Exiba quem venceu ou se houve empate.


jogador1 = input('Qual a jogada do player 1(pedra, papel ou tesoura)? ').lower().strip()
jogador2 = input('Qual a jogada do player 2 (pedra, papel ou tesoura)? ').lower().strip()

if jogador1 == 'pedra' and jogador2 == 'pedra' or jogador1 == 'papel' and jogador2 == 'papel' or jogador1 == 'tesoura' and jogador2 == 'tesoura':
    print('Houve um empate!')
elif jogador1 == 'pedra' and jogador2 == 'papel':
    print('Jogador 2 venceu!')
elif jogador1 == 'pedra' and jogador2 == 'tesoura':
    print('Jogador 1 venceu!')
elif jogador1 == 'papel' and jogador2 == 'pedra':
    print('Jogador 1 venceu!')
elif jogador1 == 'papel' and jogador2 == 'tesoura':
    print('Jogador 2 venceu!')
elif jogador1 == 'tesoura' and jogador2 == 'pedra':
    print('Jogador 2 venceu!')
elif jogador1 == 'tesoura' and jogador2 == 'papel':
    print('Jogaador 1 venceu!')
else:
    print('Jogada invalida!')
