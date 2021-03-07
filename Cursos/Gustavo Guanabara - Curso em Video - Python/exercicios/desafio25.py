#DESAFIO 25 OK
'''
faca um programa que leia um numero de 0 a 9999 e mostre na tela um dos digitos separados
ex numero 1834
unidade = 4
dezema = 3
centena = 8
milhar = 1

string e matematica¹¹
'''

import random

num = int(input('digite um numero de 0 a 9999: '))

pn = num // 1 % 10
sn = num // 10 % 10
tn = num // 100 % 10
qn = num // 1000 % 10

print('Numero digitado = {}'.format(num))
print('PRIMEIRO DIGITO = {}'.format(pn))
print('SEGUNDO DIGITO = {}'.format(sn))
print('TERCEIRO DIGITO = {}'.format(tn))
print('QUARTO DIGITO = {}'.format(qn))


print('\n\n\n')
n = str(random.randrange(0000, 9999))
print('#### AUTOMATICO ####\n')
print(n)
print('-' * 20)
print(' 1 = {}\n 2 = {}\n 3 = {}\n 4 = {}'.format(n[0], n[1], n[2], n[3]))
