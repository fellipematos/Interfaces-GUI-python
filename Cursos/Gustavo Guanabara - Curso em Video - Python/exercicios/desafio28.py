#DESAFIO 28 OK
'''
faca um programa que leia uma frase pelo teclado e mostra
- quanas vezes aparece a letra 'a'
- em que posicao ela aparece a primeira vez
- em que posicao ela aparece a ultima vez
'''

#frase = str(input('Digite uma frase: ')).strip()
frase = str('O amor é paz, sucesso na vida.').strip().upper()

print('\nFrase:\n{}'.format(frase))
print('-' * 40)
print('A frase contem {} letra A.'.format(frase.count('A')))
print('total de caracteres: {}'.format(len(frase)))
print('Primeira letra A aparece na {} posição.'.format(frase.find('A') + 1))
print('Ultima letra A aparece na {} posição.'.format(frase.rfind('A') + 1))

print('\n' * 3)
