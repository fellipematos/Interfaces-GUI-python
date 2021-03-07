#DESAFIO 36 OK
'''
escreva um programa que pergunte o salario de um funcionario
Calcule o valor do seu aumento
Para salarios superiores a R$1250,00 calcule uma aumento de 10%
para inferiores oou igual aumento de 15%
'''

salario = float(input('Digite o Salario R$ '))

#if salario > 1250.00:
#    print('Salario atual R$ {:.2f}\n  Aumento de 10% = R$ {:.2f}'.format(salario, salario * 1.10))
#else:
#    print('Salario atual R$ {:.2f}\n  Aumento de 15% = R$ {:.2f}'.format(salario, salario * 1.15))

if salario > 1250.00:
    novosalario = salario * 1.10
else:
    novosalario = salario * 1.15

print('\n')
print('-=' * 20)
print('Salario Atual R$ \033[0;31;0m{:.2f}\033[m\nSalario Atualizado R$ \033[0;36;0m{:.2f}\033[m'.format(salario, novosalario))
print('-=' * 20)
