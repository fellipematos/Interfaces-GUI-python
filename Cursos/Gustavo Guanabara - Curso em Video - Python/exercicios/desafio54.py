#DESAFIO 54
'''
faca um programa que leia um numero inteiro
e diga se ele e ou nao um numero primo  divisivel por 1 e ele mesmo
'''

numero = int(input('DIGITE UM NUMERO: '))
c = 0

for primo in range(1, numero + 1):
    if numero % primo == 0:
        print('\033[34m', end=' ')
        c += 1
    else:
        print('\033[m', end=' ')
    print(primo, end=' ')

print('\033[m\n')

if c == 2:
    print('PRIMO')
else:
    print('NAO PRIMO')

