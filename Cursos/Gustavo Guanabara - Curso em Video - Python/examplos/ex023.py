n = 1
par = impar = 0
while n != 0:
    n = int(input('DIGITE O VALOR'))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('voce digitou {} numero par e {} numero impar'.format(par, impar))



r = 'S'
while r == 'S':
    n = int(input(Digite um valor))
    r = str(input('QUUER CONTINUAR [S/N]')).upper()
print('fim')


n = 1
while n != 0:
    n = int(input(' digite numero '))
print('fim')


c = 1
while c < 10:
    print(c)
    c = c + 1
print('FIM')


'''
for c in range(1, 10):
    print(c)
print('fim')
'''
