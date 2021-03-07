#DESAFIO 59 OK
'''
faca um programa que leia o sexo de uma pessoa
mas so aceite os valores M ou F caso esteja errado peça
para digitar novamente ate ter um valor correto
'''

print('QUAL SEU SEXO?')
print('[M] - MASCULINO')
print('[F] - FEMININO')

sexo = ['F', 'M']
while sexo != 'F' and sexo != 'M':
    sexo = str(input(': ')).strip().upper()
    print(sexo)
print('FIM')

