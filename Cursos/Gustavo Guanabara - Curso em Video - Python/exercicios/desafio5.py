#DESAFIO 5 OK
#cria programa leia algo digitado tipo primitivo e informacoes possiveis

descr = input('Digite algo: ')

print('INFORMACOES SOBRE = ()'.format(descr))
print('Tipo Primitivo', type(descr))
print('E UMA PALAVRA', descr.isalpha())
print('E UM NUMERO', descr.isnumeric())
print('E ALPHANUMERICO', descr.isalnum())
