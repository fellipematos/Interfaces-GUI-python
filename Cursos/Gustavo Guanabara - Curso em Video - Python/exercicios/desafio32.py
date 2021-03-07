#DESAFIO 32 OK
#crie um programa que leia um numero inteiro e mostre na tela se ele e par ou impar

num = int(input('DIGITE UM NUMERO: '))
#num = int('100')
div = num % 2
#print(div)

if div == 0:
    print(num, 'resta', div, '= \033[0;32;0mPAR')
else:
    print(num, 'resta', div, '= \033[0;31;0mIMPAR')
