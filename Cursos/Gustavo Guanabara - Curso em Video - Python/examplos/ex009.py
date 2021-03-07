num1 = int(input('digite um numero: '))
num2 = int(input('digite outro numero: '))

print('A soma e igual {}'.format(num1+num2))

s = num1 + num2
ss = num1 - num2
m = num1 * num2
d = num1 / num2
di = num1 // num2
e = num1 ** num2

print('numero 1 = {} numero 2 = {}'.format(num1, num2))
print('soma = {}'.format(s))
print('subtracao = {}'.format(ss))
print('multiplicacao = {}'.format(m))
print('divisao = {:.3f}'.format(d))
print('divisao inteira = {}'.format(di))
print('potencia = {:.3f}'.format(e)) #.3f = 3 casas apos o . float ex 1.333333 ajusta para 1.333

print('teste 2 print sem ', end='')#, end='' dois print mesma linha
print('quebra de linha')

print('teste 1 print \n 2 linha')#\n 1 print duas linhas
