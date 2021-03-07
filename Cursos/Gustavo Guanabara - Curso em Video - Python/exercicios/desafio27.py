#DESAFIO 27 OK
'''
Crie um programa que leia o nome de uma pessoa e diga se ela tem 'silva' no nome
true ou false
'''

print('\n')
print('TEM SILVA NO SEU NOME')

valor= str(input('DIGITE SEU NOME COMPLETO: \n> ')).strip()
nome = valor.upper()

print('-' * 30)
print(nome)
print('-' * 20)

print('NOME CONTEM SILVA: {}'.format('SILVA' in nome))
print('segunda opção de escrita {}'.format('silva' in valor.lower()))
