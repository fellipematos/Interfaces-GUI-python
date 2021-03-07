from random import randint

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
    print('ERRO')

