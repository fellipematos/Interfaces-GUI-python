frase = 'Curso em Video'

print(frase[2])
print(frase[4:])
print(frase[:8])
print(frase[1:14:2])
print(frase[::2])

print(frase.count('o'))
print(frase.upper().count('o'))

print(len(frase))
print(len(frase.strip()))

print(frase.replace('Video', 'aulas'))
frase2 = frase.replace('Video', 'teste')
print(frase, 'frase sem replace')
print(frase2, 'frase2 com replace var para trocar str')

print('python' in frase)
print('teste' in frase)

print(frase.find('teste'))
print(frase.find('Video'))
print(frase.lower().find('Video'))
print(frase.upper().find('video'))
print(frase.capitalize().find('video'))

print(frase.split())


div = frase.split()
print(div[0])
print(div[2])
print(div[2][2])



frasess = ('   FRASE   ')
print(frasess)
print(frasess.strip())
print(frasess.rstrip())
print(frasess.lstrip())

