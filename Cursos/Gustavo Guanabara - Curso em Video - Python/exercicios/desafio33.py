#DESAFIO 33 OK
'''
desenvolva um programa que pergunte a distancia de uma viagem em km
calcule o preco de passagem, cobrando R$0,50 por km para viagem de ate
200km e R$0,45 para viagens mais longe
'''

dist = float(input('Digite a distancia de sua viagem: '))
#dist = float(1000)

#if dist <= 200:
#    print('O Preço da sua Passagem R${:.2f}'.format(dist * 0.50))
#else:
#    print('O Preço da sua Passagem R${:.2f}'.format(dist * 0.70))

#simplificando

if dist <= 200:
    preco = dist * 0.50
else:
    preco = dist * 0.45

print('O Preço da sua Passagem R${:.2f}'.format(preco))
