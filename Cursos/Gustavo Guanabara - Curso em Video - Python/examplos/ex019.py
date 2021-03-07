print('\033[1;36;0mTESTE\033[m')

nome = 'Teste'
cores = {'fim':'\033[m', 'azul':'\033[0;34;0m', 'vermelho':'\033[0;31;0m'}
print('teste {}{}{}'.format(cores['azul'], nome, cores['fim']))

