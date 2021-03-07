#DESAFIO 16 OK
'''
leia temperatura em graus e transforma em fahrehamt
FORMULA (10 °C × 9/5) + 32 = 50 °F
'''
c = float(input('Qual a temperatura C\n> '))
f = float((c * 9 / 5) + 32)

print('{} Graus Celsius = {} Graus Fahrenheit'.format(c, f))
