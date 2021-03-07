#DESAFIO 37 OK
'''
desenvolva um programa que leia o comprimento de tres retas e dia ao usuario
se ele podem ou nao formar um triangulo
'''

a = int(input('RETA A = '))
b = int(input('RETA B = '))
c = int(input('RETA C = '))

print('RETAS A = {}  B = {}  C = {}'.format(a, b, c))

la = (b - c) < a < (b + c)
lb = (a - c) < b < (a + c)
lc = (a - b) < c < (a + b)

print('\nRETA A {} \nRETA B {} \nRETA C {}'.format(la, lb, lc))
print('\n')
print('-=' * 20)

if a < b + c and b < a + c and c < a + b:
    print('\033[0;32;0mtriangulo')
else:
    print('\033[0;31;0mNAO TRIANGULO')
