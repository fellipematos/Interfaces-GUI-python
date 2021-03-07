#DESAFIO 46 OK
'''
elabore um programa que calcule o valor a ser pago por um produto
considerando o seu preco normal e condições de pagamento

a vista dinheiro 10% de desconto
a vista no cartao 5% de desconto
em ate 2x cartao preco normal
3 x ou mais no cartao 20% de juros
'''

#CABECALHO
print('\033[1;32;0m')
print('#' * 50)
print('{:#^50}'.format(' VERIFICAR DESCONTOS '))
print('#' * 50)
print('\033[m')

#PRECO DO PRODUTO
valor = float(input('QUAL O VALOR DO PRODUTO: '))
print('-' * 50)

#MOSTRAR E PERGUNTAR FORMAS DE PAGAMENTO
print('\033[1;32;0m')
print('[1] - A VISTA DINHEIRO')
print('[2] - A VISTA CARTAO')
print('[3] - EM ATE 2X CARTAO')
print('[4] - 3X OU MAIS CARTAO')
print('\033[m')
formpag = int(input('QUAL A FORMA DE PAGAMENTO: '))
print('-' * 50)

#PRECO FINAL
if formpag == 1:
    valorfinal = valor - (valor * 10 / 100)
    print('\033[1;32;0m')
    print('DESCONTO 10%')
    print('VALOR DO PRODUTO R$ {:.2f} {:>20}'.format(valor, '- 10%'))
    print('- ' * 25)
    print('VALOR TOTAL R$ {:.2f}'.format(valorfinal))
    print('\033[m')

elif formpag == 2:
    valorfinal = valor (valor * 5 / 100)
    print('\033[1;32;0m')
    print('DESCONTO 5%')
    print('VALOR DO PRODUTO R$ {:.2f} {:>20}'.format(valor, '- 5%'))
    print('- ' * 25)
    print('VALOR TOTAL R$ {:.2f}'.format(valorfinal))
    print('\033[m')

elif formpag == 3:
    valorfinal = valor
    print('\033[1;36;0m')
    print('SEM DESCONTO PARA PAGAMENTO EM 2X\n')
    print('VALOR DO PRODUTO R$ {:.2f}'.format(valor))
    valorparcela2 = valor / 2
    print('VALOR DA PARCELA 2x DE R$ {:.2f}'.format(valorparcela2))
    print('- ' * 25)
    print('VALOR TOTAL R$ {:.2f}'.format(valorfinal))
    print('\033[m')

elif formpag == 4:
    valorfinal = valor + (valor * 20 / 100)
    print('\033[1;33;0m')
    print('JUROS 20%\n')
    print('VALOR DO PRODUTO R$ {:.2f} {:>20}'.format(valor, '+ 20%'))
    parcela = int(input('QUANTAS PARCELAS: '))
    print('VALOR DA PARCELA {} DE R$ {:.2f}'.format(parcela, valorfinal / parcela))
    print('- ' * 25)
    print('VALOR TOTAL R$ {:.2f}'.format(valorfinal))
    print('\033[m')

else:
    print('\033[1;31;0m')
    print('! E R R O ')
    print('- ' * 25)
    print('!! REFACA  A  OPERACAO')
    print('\033[m')
