import PySimpleGUI as sg

#layout
sg.theme('Topanga') #https://media.geeksforgeeks.org/wp-content/uploads/20200511200254/f19.jpg
layout = [
    [sg.Text('Nome'), sg.Input(key='nome', size=(20, 1))],
    [sg.Text('Senha'), sg.Input(key='senha', password_char='*', size=(20, 1))],
    [sg.Checkbox('Salvar o Login?')],
    [sg.Button('SALVAR')]
]

#janela
janela = sg.Window('LOGIN', layout)

#eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'SALVAR':
        if valores['nome'] == 'teste' and valores['senha'] == '123456':
            print('Seja bem vindo!')
