#DESAFIO 61
'''
crie um programa que leia dois valores e mostre um menu na tela
1 somar
2 multiplicar
3 maior
4 novos numeros
5 sair do programs

seu programa devera realizar a operacao solicitada em cada caso
''''

cond = [1, 2, 3, 4, 5]

while True:
    num1 = int(input('Digite primeiro numero: '))
    num2 = int(input('Digite segundo numero: '))

    print('''
        O que deseja fazer:
        [1] Soma
        [2] Multiplicar
        [3] Maior
        [4] Novos Numeros
        [5] Sair
    ''')

    opc = int(input(': '))

    if opc == 1:
        print('A soma de {} e {} e igual a {}'.format(num1, num2, num1 + num2))
    elif opc == 2:
        print('A multiplicação de {} e {} e igual a {}'.format(num1, num2, num1 * num2))
    elif opc == 3:
        print('{} e {} '.format(num1, num2), end='')
        if num1 > num2:
            print('o maior e {}'.format(num1))
        elif num2 > num1:
            print('o maior e {}'.format(num2))
        else:
            print('sao iguais')
    elif opc == 4:
        print('Insira novos dados.')
    elif opc == 5:
        print('ENCERRANDO')
        break
    else:
        print('Opção Invalida
