#DESAFIO 20 OK FALTOU COLOCAR RADIANS
'''
leia o angulo qualquer
mostre valor seno cosseno tangente

circulo eixo vertical no meio sen
eixo horizontal cos
eixo
radiando
'''

import math

ang = float(input('Digite o angulo = '))

cos = math.cos(math.radians(ang))
sen = math.sin(math.radians(ang))
tan = math.tan(math.radians(ang))

print('Angulo = {}'.format(ang))
print('Cossseno = {:.2f} \nSeno = {:.2f} \nTangente = {:.2f}'.format(cos, sen, tan))

