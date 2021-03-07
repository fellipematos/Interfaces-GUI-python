#DESAFIO 31 OK
'''
escreva um programa que leia a velocidade de uma carro
se ele ultrapassar 80km/h mostre uma mensagem que ele foi multado
ea multa vai custar 7,00 opor cada km acima do limite
'''

vel = float(input('Digite a Velocidade atingida: '))
#vel = int(120)

if vel > 80:
	print('EI PARE DE CORRER!\nVOCÊ ACABOU DE RECEBER UMA MULTA\n\nTOTAL A PAGAR R$ {},00'.format((vel - 80) * 7))
else:
	print('Continue assim. Respeitando o limite de velocidade')
	