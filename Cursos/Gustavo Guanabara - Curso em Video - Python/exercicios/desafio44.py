#DESAFIO 44 OK
'''
refaca o desafio dos triangulos acrescentando o recurso de mostrar que tipo
de triangulo sera formado

- equilatero - todos lados iguais
- isosceles - doisa lados iguais
- escalena - todos lados diferente
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
    print('triangulo', end=' ')
else:
    print('NAO TRIANGULO')

# equilatero - todos lados iguais
if a == b == c:
    print('EQUILATERO')

# escalena - todos lados diferente
elif a != b and a != c and b != c:
    print('ESCALENA')

# isosceles - doisa lados iguais
else:
    print('ISOSCELES')
