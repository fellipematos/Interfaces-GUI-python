#DESAFIO 26 OK
#crie um programa que leia o nome de uma cidade e diga se ela comeca ou nao com o nome ''SANTO''

local = str(input('Qual o nome da sua cidade: '))
cidade = local.upper()

print('\n {}'.format(cidade))
print('-' * 20)

#cidadeX = str.upper('SANTOS')
#verifica = cidade == cidadeX

#print('Vocè esta em SANTOS: {}'.format(verifica))
print('Comeca com Santo {}'.format('SANTO'in cidade))

cidade2 = str('Santo Antonio').strip()
print('cidade 2 = 'cidade2[:5].upper() == 'SANTO')
