#DESAFIO 48 OK
'''
faca um programa que mostre
na tela uma contagem regressiva
para o estouro de fogos de artificios
10 ate 0 com uma pausa de 1 segundo
'''

from time import sleep

for cont in range(10, 0, -1):
 print(cont)
 sleep(1)

print('''

 888888ba   .88888.   .88888.  8888ba.88ba  dP  dP
 88    `8b d8'   `8b d8'   `8b 88  `8b  `8b 88  88
a88aaaa8P' 88     88 88     88 88   88   88 88  88
 88   `8b. 88     88 88     88 88   88   88 dP  dP
 88    .88 Y8.   .8P Y8.   .8P 88   88   88       
 88888888P  `8888P'   `8888P'  dP   dP   dP oo  oo

''')
