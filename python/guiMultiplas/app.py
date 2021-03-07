import PySimpleGUI as sg

def cliente():
        
    sg.theme('Topanga')
    layout = [
        [sg.Text('Nome para o Pedido:')],
        [sg.Input(key='nome', size=(20, 1))],
        [sg.Button('FAZER PEDIDO', key='fazerPedido')]
    ]
    return sg.Window('Cliente', layout=layout, finalize=True)

def cardapio():
    sg.theme('Topanga')
    layout = [
        [sg.Text('CARDAPIO')],
        [sg.Checkbox('Combo 1', key='combo1')],
        [sg.Checkbox('Combo 2', key='combo2')],
        [sg.Checkbox('Combo 3', key='combo3')],
        [sg.Text('\n Forma de Pagamento:')],
        [sg.Checkbox('Cartão', key='cartao'), sg.Checkbox('Dinheiro', key='dinheiro')],
        [sg.Button('Finalizar Pedido', key='finalizar')]

    ]
    return sg.Window('Cardapio', layout=layout, finalize=True)

def pedido():
    sg.theme('Topanga')
    layout = [
        [sg.Text('SEU PEDIDO NUMERO 001')]
    ]

    return sg.Window('Seu Pedido', layout=layout, finalize=True)

windowOne, windowTwo, windowTree = cliente(), None, None

while True:
    window,event,values = sg.read_all_windows()

    if window == windowOne and event == sg.WIN_CLOSED:
        break
    if window == windowOne and event == 'fazerPedido':
        windowTwo = cardapio()
        windowOne.hide()
    if window == windowTwo and event == 'finalizar':
        windowTree = pedido()
        windowTwo.hide()
