#DESAFIO 55
'''
crie um programa que leia uma frase
qualquer e diga se ela e uma palindroma
desconsiderando os espacos

apos a sopa
a sacada da casa
a torre da derrota
o lobo ama o bolo
anotaram a data da maratona
'''

frase = str('a sacada da casa').strip().upper()
frasepalavras = frase.split()
frasej = ''.join(frasepalavras)

inverso = ''

print(frase)
print(frasepalavras)
print('{}'.format(frasej))

for verifica in range(len(frasej) - 1, - 1, - 1):
    inverso += frasej[verifica]
print(inverso)

if frasej == frasej[::-1]:
    print('SIM')
else:
    print('NAO')
