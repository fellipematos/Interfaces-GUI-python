#DESAFIO 17 OK
'''
programa pergunta a quantidade de km percorrido
quantidade de dias alugado
resultado do preco a pagar
diaria = 60R$ e 0,15R$ por km rodado
'''

dia = int(input('Quantos dias: '))
km = float(input('Qual a kilometragem: '))

vdia = dia * 60
vkm = km * 0.15

total = (dia * 60) + (km * 0.15)#2met

print('Total a pagar {:.2f}'.format(vdia + vkm))
print(total)#result 2met
