#DESAFIO 21 OK 
'''
Sortear um de seus quatro alunos para apagar o quadro e mostrar o nome
++ adicionou modo de list e criou uma var para sorteio
'''

import random

aluno1 = str(input('Digite o nome do aluno 1 : '))
aluno2 = str(input('Digite o nome do aluno 2 : '))
aluno3 = str(input('Digite o nome do aluno 3 : '))
aluno4 = str(input('Digite o nome do aluno 4 : '))

#lista = [aluno1, aluno2, aluno3, aluno4]
#sorteio = random.choice(lista)

print(random.choice([aluno1, aluno2, aluno3, aluno4]))
#print(sorteio)

