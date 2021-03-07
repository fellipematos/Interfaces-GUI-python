#corrigir erro de notas

nota1 = float(input('Nota Primeira PROVA: '))
nota2 = float(input('Nota Segunda PROVA: '))

media = (nota1 + nota2) / 2

print('Media Final = {:.1f}'.format(media))
if media >= 8.0:
    print('PARABENS, Vocè foi aprovado')
else:
    print('NÃO FOI DESSA VEZ TENTE NOVAMENTE')

print('\n PARABENS' if media >= 8 else 'TENTE DE NOVO')
