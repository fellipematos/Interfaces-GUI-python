#DESAFIO 40 OK
'''
Escreva um programa que leia dois numeros inteiros e compare mostrando na tela
- primeiro valor e maior
- segundo valor e maior
- nao existe valor maior os dois sao igual
'''

primeiro = int(input('Primeiro Valor = '))
segundo = int(input('Segundo valor = '))

print('\n')

if primeiro > segundo:
    print('Primeiro Valor e Maior')
elif primeiro < segundo:
    print('Segundo Valor e Maior')
else:
    print('Os Valores são Iguais')
