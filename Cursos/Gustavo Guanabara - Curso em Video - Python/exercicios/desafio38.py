#DESAFIO 38 OK
'''
escreva um programa para aprovar o emprestimo
bancario para comprar uma casa
perguntar valor da casa
salario do comprador
em quantos anos ele vai pagar

calcule o valor da prestacao mensal
sabendo que ela nao pode exceder 30%
do salario ou entao o emprestimo sera negado
'''


#importanto tempo de carregamento
import time

#header
print('\033[1;33;0m-' * 50)
print('{:^50}'.format('Imobiliaria - Sistema de Aprovação'))
print('-' * 50, '\033[m')

#formulario
nomecliente = str(input('Nome do Cliente: '))
valorimovel = float(input('Qual o Valor do Imovel: R$ '))
renda = float(input('Qual sua Renda Mensal: R$ '))
ano = int(input('Em quantos anos pretende pagar: '))
parcela = valorimovel / (ano * 12)

'''#formulario versao teste
nomecliente = 'Fellipe Matos'
valorimovel = 120000
renda = 50000
ano = 10
parcela = valorimovel / (ano * 12)'''

#calcular porcentagem do salario
minimo = renda * 30 / 100
#print("{}".format(renda30))

#carregando dados
print('\033[7;32;30m {:^48} \033[m'.format('AGUARDE PROCESSANDO'))
time.sleep(1)

#listar dados
print('-' * 50)
print('Cliente: {}'.format(nomecliente))
print('Renda Mensal: R$ {:.2f}'.format(renda))
print('Valor do Imovel: R$ {:.2f}'.format(valorimovel))
print('-' * 50)
print('Anos para Pagar: {}'.format(ano))
print('Numeros de Parcelas: {}'.format(ano * 12))
print('Prestação: R$ {:.2f}'.format(parcela))
print('-' * 50)

#aprovar
if parcela <= minimo:
    print('\033[1;32;0m-' * 50)
    print('{:^40}'.format('PARABÉNS - SEU CREDITO FOI APROVADO'))
    print('-' * 50)
    print('Seu Sonho acaba de se realizar,\nvoce está pronto para comprar seu imovel')
    print('Precisamos dos seguinte Documento:')
    print('-' * 50, ' \033[m')
else:
    print('\033[1;31;0m-' * 50)
    print('{:^40}'.format('NÃO FOI DESSA VEZ - CREDITO REPROVADO'))
    print('-' * 50)
    print('Seu Sonho AINDA não foi realizado,\nnão fique assim encontrara coisa melhor!')
    print('-' * 50, ' \033[m')
