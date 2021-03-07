#DESAFIO 7 OK
#leia um numero mostre seu dobro triplo e raiz quadrada

num = int(input('digite um numero: '))

print('numero digitado', num)
print('seu dobro é {}'.format(num*2))
print('seu tripo é {}'.format(num*3))
print('raiz quadrada {:.3f}'.format(num**(1/2)))
print('raiz quadrada de {} e {:.3f}'.format(num, pow(num, (1/2)))) #pow == potencia
