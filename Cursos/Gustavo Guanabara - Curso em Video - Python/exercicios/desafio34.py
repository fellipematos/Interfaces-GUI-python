#DESAFIO 34 OK
#faça um programa que leia um ano qualquer e mostre se ele e BISSEXTO

from datetime import date

ano = int(input('DIGITE UM ANO! COLOQUE 0 PARA ANO ATUAL !'))

if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('BISSEXTO')
else:
    print('NAO E UM ANO BISSEXTO')
