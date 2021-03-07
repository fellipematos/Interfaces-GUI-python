#DESAFIO 53
'''
desenvolva um programa que leia o primeiro termo
e a razao de uma Progressao Aritmetica no final mostre os 10 primeiro termos dessa progressao
'''

termo = int(input('Primeiro Termo: '))
razao = int(input('Razao: '))
decimo = termo + (10 - 1) * razao

for r in range(termo, decimo, razao):
    print('{}'.format(r), end=' -> ')

print('FIM')
