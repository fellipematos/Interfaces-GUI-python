#DESAFIO 41 OK
'''
Faca um programa que leia o ano de nascimento de uma jovem
informe de acordo com sua idade

calcular idade

- se ele ainda vai se alistar ao servico militar
- se e a hora de se alistar
- se ja passou do tempo do alistamento

seu programa tambem devera mostrar o tempo que falta ou que passou do tempo
'''

from datetime import date

nome = str(input('Digite seu Nome completo: ')).strip()
dia = int(input('Dia em que nasceu: '))
mes = int(input('Mes em que nasceu: '))
ano = int(input('Ano em que nasceu: '))

anoatual = date.today().year
result = anoatual - 18

print('-=-' * 15)
print('{}, {} anos.'.format(nome, (anoatual - ano)))

if ano == result:
    print('\033[1;32;0m')
    print('-x-' * 15)
    print('VOCÊ PRECISA SE APRESENTAR, NA JUNTA MILITAR')
    print('-x-' * 15)
    print('\033[m')

elif ano > result:
    falta = ano - result
    print('\033[1;36;0m')
    print('---' * 15)
    print('VOCÊ AINDA NÃO TEM IDADE')
    print('FALTA {} PARA VOCÊ SE ALISTAR'.format(falta))
    print('---' * 15)
    print('\033[m')

else:
    falta = result - ano
    print('\033[1;31;0m')
    print('-X-' * 15)
    print('JÁ PASSARAM {} DA SUA FASE DE ALISTAMENTO'.format(falta))
    print('-X-' * 15)
    print('\033[m')

print('-=-' * 15)
print('\033[m')
