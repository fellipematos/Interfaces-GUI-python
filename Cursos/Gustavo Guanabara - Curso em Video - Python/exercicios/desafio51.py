#DESAFIO 51 OK
'''
refaca o desafio 009 mostrando a tabuada
de um numero que o usuario escolher
so que agora utilizando o for
'''

num = int(input('digite o numero que deseja saber sua tabuada: '))
#num = 10

for tab in range(1, 10 + 1):
    print('{} X {:2} = {}'.format(num, tab, num * tab))
    
print('\nFIM')
