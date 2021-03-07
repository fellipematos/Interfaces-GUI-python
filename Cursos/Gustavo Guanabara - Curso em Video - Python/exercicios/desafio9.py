#DESAFIO 9 OK
#insira o valor em metro - converta em centimetros e milimetros

metro = float(input('Qual a metragem: '))
cm = metro * 100
mm = metro * 1000

print('Sua Metragem inicial', metro)
print(metro, 'em centrimetros = {}'.format(metro*100))
print(metro, 'em milimetros = {}'.format(metro*1000))
print(metro,'m\n',cm,'cm\n',mm,'mm')
