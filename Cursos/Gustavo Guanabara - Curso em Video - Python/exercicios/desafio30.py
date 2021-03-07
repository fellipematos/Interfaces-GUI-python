#DESAFIO 30 OK
'''
programa que faca o computador pensar um numero inteiro
entre 0 e 5 e peça para i usuarui tentar descobrir qual foi o numero escolhido
o programa devera escrever na tela se o usuario ganhou ou perdeu
'''

import random

print('\nBEM VINDO, ao JOGO')
print('Tente descobrir qual numero o computador pensou de 0 a 5\n')

comp = random.randint(0,5)
#print(comp)

print('Iniciando...')
print('PRONTO.. Já pensei em um numero, sua vez.')
print('-' * 20)

user = int(input('Qual numero o computador pensou? \n'))
print('-' * 20)

if comp == user:
    print('PARABENS, VOCÊ ACERTOU')
else:
    print('ERROU ..... \n TENTE NOVAMENTE')
    