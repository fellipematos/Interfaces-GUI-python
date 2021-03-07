#DESAFIO 19 OK ERREI A FORMULA PARA CALCULAR
'''
leia comprimento do cateto oposto
e do cateto adjacente de um triangulo retangulo
calcule e mostre o comprimento da hipotenusa

A² = B² + C²
A= hipotenusa

| - cateto oposto

_ - cateto adjacente

\ - hipotenusa
'''

import math

copo = float(input('Cateto Oposto = '))
cadj = float(input('Cateto Adjacente = '))

#hip = (copo ** 2 + cadj ** 2) ** (1/2)

hip = math.hypot(copo, cadj)

print(' \n Cateto Oposto = {} \n Cateto Adjacente = {}'.format(copo, cadj))
print('o valor da hipotenusa e {:.2f}'.format(hip))
