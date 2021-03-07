#DESAFIO 29 OK
'''
faca um programa que leia o nome completo da pessoa
mostrando em seguida o primeiro e o ultimo nome separadamente

ex Ana Maria Souza
primeiro = Ana
segundo = Souza
'''

nome = str(input('Digite seu nome completo: ')).strip()
#nome = str('')
print(nome, '\n', '-' * 20)

primeironome = nome.split()
ultimonome = nome.split()[::-1]

print('Seu primeiro nome é {}'.format(primeironome[0]))
print('Ultimo nome é {}'.format(ultimonome[0]))

print('\n')

nomes = nome.split()
print('primeiro nome = {}'.format(nome.split()[0]))
print('ultimo nome = {}'.format(nomes[len(nomes)-1]))#tem que ter variavel
