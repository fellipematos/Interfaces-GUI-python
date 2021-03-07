#DESAFIO 45 OK
'''
desenvolva uma logica que leia o peso e altura de uma pessoa
calcule seu IMC e mostre seus status
de acordo com a tabela abaixo

- abaixo de 18.5 - abaixo do peso
- entre 18.5 e 25 peso ideal
- 25 ate 30 sobre peso
- 30 a 40 obesidade
- acima de 40 obesidade morbida


IMC = 80 ÷ 1,802
IMC = 80 ÷ 3,24
IMC = 24,69
'''

print('\033[1;32;0m')
print('#' * 50)
print('{:^50}'.format('CALCULE SEU IMC'))
print('#' * 50)
print('\033[m')

nome = 'Fellipe'
peso = 95
altura = 1.75
#nome = str('Digite seu NOME: ').strip()
#sexo = ('[1 - Mulher} ou {2 - Homem]')
#peso = float(input('Digite seu PESO: '))
#altura = float(input('Digite sua ALTURA: '))

print(nome, peso, altura)

imc = peso / (altura ** 2)

if imc <= 18.5:
    print('ABAIXO DO PESO')
elif imc > 18.5 and imc <= 25:
    print('PESO IDEAL')
elif imc > 25 and imc <= 30:
    print('SOBREPESO')
elif imc > 30 and imc < 40:
    print('OBESIDADE')
elif imc >= 40:
    print('OBESIDADE MORBIDA')

