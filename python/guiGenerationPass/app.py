#programa interface grafica 
#armazenar site/software qual a senha foi gerado
#armazenar o usuario/email
#possibilitar a configurar tamanho da senha

import random
import PySimpleGUI as sg
import os

class PassGen:
    def __init__(self):
        #layout
        sg.theme('Black')
        layout = [
            [sg.Text('Site/Software', size=(10, 1)), sg.Input(key='site', size=(20, 1))],
            [sg.Text('Usuario/Email', size=(10, 1)), sg.Input(key='user', size=(20, 1))],
            [sg.Text('Quantidade de Caracteres:'), sg.Combo(values=list(range(30)), key='chars', default_value=1, size=(3, 1))],
            [sg.Output(size=(32, 5))],
            [sg.Button('Gerar Senha')]
        ]
        #window
        self.window = sg.Window('Password Generator', layout)
        
    def Iniciar(self):
        while True:
            evento, valores = self.window.read()
            if evento == sg.WINDOW_CLOSED:
                break
            if evento == 'Gerar Senha':
                nova_senha = self.gerar_senha(valores)
                print(nova_senha)
                self.salvar_senha(nova_senha, valores)
    
    def gerar_senha(self, valores):
        char_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789!@#$%&*'
        chars = random.choices(char_list, k=int(valores['chars']))
        new_pass = ''.join(chars)
        return new_pass

    def salvar_senha(self, nova_senha, valores):
        with open('senhas.txt','a',newline='') as arquivo:
            arquivo.write(f"site: {valores['site']}, usuario: {valores['user']}, senha: {nova_senha} \n")
        print('Arquivo Salvo ..')

gen = PassGen()
gen.Iniciar()
