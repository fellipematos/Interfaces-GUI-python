#DESAFIO 14 OK
#leia o salario de um funcionario e mostre um aumento de 15%

func = str(input('Nome do Funcionario: '))
cashfunc = float(input('Salario Atual: R$'))
aucash = float(1.15) #15%

print(func, 'Salario Atual: R$ {:.2f}'.format(cashfunc))
print('Aumento Salarial: R$ {:.2f}'.format(cashfunc*aucash))

aucash2 = cashfunc + (cashfunc * 15 / 100)

print('R${:.2f}'.format(aucash2))
