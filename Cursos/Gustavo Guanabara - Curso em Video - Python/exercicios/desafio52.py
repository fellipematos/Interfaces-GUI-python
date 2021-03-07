#DESAFIO 52
'''
desenvolva um programa que leia
seis numero inteiros
es mostre a soma apenas daqueles que
forem pares
se o valor digitaro for impar
desconsidere
'''

soma = 0
for num in range(0, 6):
    num = int(input('Digite um valor: '))
    if num % 2 == 0:
        soma += num

print(soma)
print('FIM')
