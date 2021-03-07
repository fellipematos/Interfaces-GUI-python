#DESAFIO 13 OK
#eia o preco do produto e mostre com um novo preço com 5% de desconto

preco = float(input('Valor do Produto R$ '))
desconto = float(0.95) #5%

print('de - R$',preco,'\n por - R$ {:.2f}'.format(preco*desconto))
print('desconto de R$ {:.2f}'.format(preco*5/100))

desconto2 = preco - (preco * 5 / 100)

print('\n desconto 2 R${:.2f}'.format(desconto2))
