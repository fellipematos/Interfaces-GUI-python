#DESAFIO 22 OK
#listar alunos e sortear ordem de apresentacao sortida

import random

a1 = str(input('aluno 1 : '))
a2 = str(input('aluno 2 : '))
a3 = str(input('aluno 3 : '))

sorteio = random.sample([a1, a2, a3], k=3)

print(sorteio)
