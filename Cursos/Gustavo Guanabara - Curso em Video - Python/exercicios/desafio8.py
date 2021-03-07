#DESAFIO 8 OK
#leia duas notas do aluno e mostre a media

aluno = input('Nome do Aluno:')
nt1s = float(input('Nota final 1 semestre:'))
nt2s = float(input('Nota final 2 semestre:'))
media = (nt1s+nt2s)
media2 = (nt1s+nt2s) / 2

print('Aluno {:^20}'.format(aluno))
print('Primeiro semestre: ', nt1s)
print('Segundo semestre: ', nt2s)
print('Nota final: {:.1f}'.format(media/2))
print('\n \n', media2)
