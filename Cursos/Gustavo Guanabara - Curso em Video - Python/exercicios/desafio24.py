#DESAFIO 24 OK 
## incluido algumas outras maneiras de escrever o codigo
## simplificando
'''
crie um programa leia o nome completo de uma pessoa e mostre
- nome com todas as letras maiusculas
- nome com todas as letras minuscula
- quantas ketras ao todos sem considerar espacos
- quantas letras tem o primeiro nome
'''

print('-' *20)
print('Insira seus Dados\n')
nome = str(input('Digite seu nome Completo: ')).strip()
print('-' *20)
print('Seu nome Completo é: {:^30}\n'.format(nome))
print('-' *20)

###########
print('-- ', nome.upper())
print('-- ', nome.lower())

print('-' *20)

print('{}'.format(nome.upper()))
print('{}'.format(nome.lower()))
##########

print('-' *20)

nome2 = nome.replace(' ', '')
print('Quantidades de Caracteres: {}.'.format(len(nome2)))
print('Quantidades de Caracteres: {}.'.format(len(nome) - nome.count(' ')))

print('-' * 20)

nome3 = nome.split()
print('Seu primeiro nome tem {} caracteres.'.format(len(nome3[0])))
print('Total de caracteres no primeiro nome {}'.format(nome.find(' ')))

print('-' * 20)

print('segunda forma\n{}\n{}'.format(nome3[0], len(nome3[0])))
