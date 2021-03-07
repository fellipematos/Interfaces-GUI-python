#DESAFIO 47 OK
'''
faca um jogo computador jogar jokenpo com voce
pedra papel tesoura
'''

import random

print('\033[0;36;0m')
print(''' JO KEN PO - GAME''')
print('==-' * 15)
print('\033[m')

opc = ('PEDRA', 'TESOURA', 'PAPEL')
comp = random.randint(1,3)

print('\033[0;30;0m')
print('[1] PEDRA  -  [2] TESOURA  -  [3] PAPEL')
print('==-' * 15)
player = int(input('Sua vez - digite a opção para jogar: '))
print('==-' * 15)
print('\033[m')

if comp == 1: #pedra
    if player == 1: #1pedra 1pedra empate
        result = 'EMP'
    elif player == 2: #1pedra 2tesoura comp ganha
        result = 'COMP'
    elif player == 3: #1pedra 3papel player ganha
        result = 'PLAY'
    else:
        result = 'ERRO'

elif comp == 2: #2tesoura
    if player == 1: #2tesoura 1pedra Player  ganha
        result = 'PLAY'
    elif player == 2: #2tesoura 2tesoura empate
        result = 'EMP'
    elif player == 3:
        result = 'COMP' #2tesoura 3papel comp ganha
    else:
        result = 'ERRO'

elif comp == 3:
    if player == 1:#3papel 1pedra comp ganha
        result = 'COMP'
    elif player == 2:#3papel 2tesoura player ganha
        result = 'PLAY'
    elif player == 3:#3papel 3 papel empate
        result = 'EMP'
    else:
        result = 'ERRO'

#print(result)

apresenta = result

if comp == 1:
    verc = 'PEDRA'
elif comp == 2:
    verc = 'TESOURA'
elif comp == 3:
    verc = 'PAPEL'
else:
    verc = 'ERRO'

if player == 1:
    verp = 'PEDRA'
elif player == 2:
    verp = 'TESOURA'
elif player == 3:
    verp = 'PAPEL'
else:
    verp = 'ERRO'

if apresenta in 'PLAY':
    print('\033[0;32;0m')
    print(verc, 'X', verp)
    print('---' * 8)
    print('{:^}'.format('VOCE GANHOU'))
    print('==-' * 15)
    print('\033[m')
elif apresenta in 'COMP':
    print('\033[0;31;0m')
    print(verc, 'X', verp)
    print('---' * 8)
    print('{:^}'.format('VOCE PERDEU'))
    print('==-' * 15)
    print('\033[m')
elif apresenta in 'EMP':
    print('\033[0;34;0m')
    print(verc, 'X', verp)
    print('---' * 8)
    print('{:^}'.format('EMPATE'))
    print('==-' * 15)
    print('\033[m')
else:
    print('\033[0;35;0m')
    print('XXX' * 15)
    print('{:15}{:^3}{:^3}{:^3}{:^3}'.format('', 'E', 'R', 'R', 'O'))
    print('XXX' * 15)
    print('\033[m')




'''from random import randint

items = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0,2)
print('0 PEDRA - 1 PAPEL - 2 TESOURA')
jogador = int(input('QUAL SUA JOGADA: '))

print('COMPUTADOR = {}'.format(items[computador]))
print('JOGADOR = {}'.format(items[jogador]))

if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVALIDA')
elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVALIDA')

elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVALIDA')

else:
    print('ERRO')'''
    