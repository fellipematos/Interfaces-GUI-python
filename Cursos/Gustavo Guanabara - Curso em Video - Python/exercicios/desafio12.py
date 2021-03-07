#DESAFIO 12 OK
'''
leia a largura e altura de uma parede em metros
calcule sua atea e a quantidade de tinta para pintar
sabendo que cada litro de tinta pinta 2m²
'''

alt = float(input('altura '))
lar = float(input('largura '))
area = lar * alt
tinta = int(input('tinta rende '))

print('total {} Litros de Tinta'.format(area/2))

print(area, 'm²')
