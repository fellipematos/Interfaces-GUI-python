#DESAFIO 35 OK
#Faca um programa que leia tres numeros e mostre qual e o maio e qual e o menor

n1 = int(input('Numero 1: '))
n2 = int(input('Numero 2: '))
n3 = int(input('Numero 3: '))

lista = [n1, n2, n3]

print('{} -- {} -- {}'.format(n1, n2, n3))

print('\n')
print(max(n1,n2,n3))
print(min(lista))
print('\n')

print('-=-' * 20)
