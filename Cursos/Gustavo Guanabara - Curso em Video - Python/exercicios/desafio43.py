#DESAFIO 43 OK
'''
A confederacao nacional de natacao
precisa de um programa que leia o ano de nascimento
de um atleta e mostre sua categoria de acordo com sua idade

- ate 4 anos = MIRIM
- ate 14 anos = INFANTIL
- ate 19 anos = JUNIOR
- ate 20 anos = SENIOR
- Acima = MASTER
'''

from datetime import date

anoatual = date.today().year

print('\033[1;34;0m')
print('~' * 50)
print('{:^50}'.format('CONFEDERAÇÃO DE NATAÇÃO NACIONAL'))
print('~' * 50)
print('\033[m')

nome = str(input('Digite o nome do Atleta: '))
idade = int(input('Digite a idade do Atleta: '))

if idade <= 4:
    cat = 'MIRIM'
elif idade >= 5  and idade <= 14:
    cat = 'INFANTIL'
elif idade >= 15 and idade <= 17:
    cat = 'JUNIOR'
elif idade >= 18 and idade <= 25:
    cat = 'ROFISSIONAL'
else:
    cat = 'MASTER'

print('\033[1;34;0m')
print('{:<15}{:<4}Anos{:>20}'.format(nome, idade, cat).upper())
print('~' * 50)
print('\033[m')
