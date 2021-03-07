#DESAFIO 15 OK
'''
leia o preco do produto
pagamento a vista 10%
pagamento a prazo 5%
'''

preco = float(input('Digite o preco do produto: R$'))

vista = preco - (preco * 10 / 100)
prazo = preco + (preco * 5 / 100)

print('Preco {} \n Preco á Vista {} \n Preco á Prazo {}'.format(preco, vista, prazo))
