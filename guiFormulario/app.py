import PySimpleGUI as sg

class TelaPython:
    def __init__(self):
        #layout
        layout = [
            [sg.Text('Nome', size=(5, 0)), sg.Input(size=(15, 0), key='nome')],
            [sg.Text('Idade', size=(5, 0)), sg.Input(size=(15, 0), key='idade')],
            [sg.Text('Quais Provedores de e-mail:')],
            [sg.Checkbox('Gmail', key='gmail'),sg.Checkbox('Hotmail', key='hotmail'),sg.Checkbox('Outros', key='outros')],
            [sg.Text('Aceita Cartão')],
            [sg.Radio('Sim', 'cartao', key='sim'), sg.Radio('Não', 'cartao', key='nao')],
            [sg.Slider(range=(0,100), default_value=0, orientation='h', size=(15,20), key='velocidade')],
            [sg.Button('Enviar dados')],
            [sg.Output(size=(30,15))]
        ]

        #window
        self.window = sg.Window('Dados', layout)

        
    def iniciar(self):
        while True:
            #event
            self.button, self.values = self.window.read()

            #print(self.values)
            nome = self.values['nome']
            idade = self.values['idade']
            aceita_gmail = self.values['gmail']
            aceita_hotmail = self.values['hotmail']
            aceita_outros = self.values['outros']
            aceita_cartao = self.values['sim']
            naoaceita_cartao = self.values['nao']
            velocidade_script = self.values['velocidade']

            print(f'nome: {nome}')
            print(f'idade: {idade}')
            print(f'gmail: {aceita_gmail}')
            print(f'hotmail: {aceita_hotmail}')
            print(f'outros: {aceita_outros}')
            print(f'aceita cartao: {aceita_cartao}')
            print(f'nao aceita cartao: {naoaceita_cartao}')
            print(f'velocidade: {velocidade_script}')
            print('-------------- \n')


tela = TelaPython()
tela.iniciar()
