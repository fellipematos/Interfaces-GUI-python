#DESAFIO 39 OK
'''
Escreva um programa que leia um numero inteiro
e peça para o usuario escolher qual sera
a base de conversao
1 para binario
2 para octal
3 para hexadecimal
'''

num = int(input('digite um numero: '))

print('[1] binario\n[2] octal\n[3] hexadecimal')
conv = int(input('qual opçâo: '))

if conv == 1:
    print('binario = {}'.format(bin(num)[2:]))
elif conv == 2:
    print('octal = {}'.format(oct(num)[2:]))
elif conv == 3:
    print('hexadecima = {}'.format(hex(num)[2:]))
else:
    print('ERRO')
    