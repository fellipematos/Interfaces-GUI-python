#DESAFIO 42 OK
'''
crie um programa que leia duas notas de um aluno e calcule sua media
mostrando uma mensgaem no final de acordo com o media atingida

- media abaixo de 5.0 REPROVADO
- media entre 5.0 e 6.9 RECUPERAÇAO
- media 7.0 ou superior APROVADO
'''

nota1 = float(input('Digite a nota do primeiro Semestre: '))
nota2 = float(input('Digite a nota do segundo Semestre: '))

nota = (nota1 + nota2) / 2

if nota < 5.0:
    print('\033[0;31;0m')
    print('REPROVADO')
elif nota >= 5.0 and nota <= 6.9:
    print('\033[0;33;0m')
    print('RECUPERAÇÃO')
elif nota >= 7.0 and nota <= 10:
    print('\033[0;32;0m')
    print('APROVADO')
