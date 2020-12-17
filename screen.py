import PySimpleGUI as sg

class TelaPython:

    #construtor
    def __init__(self):
        sg.change_look_and_feel('DarkTeal12')
        itens = ['Item a', 'Item b', 'Item c']

        #layout
        layout = [
            [sg.Text('Nome', size=(5,0)), sg.Input(size=(15,0), key='nome')],
            [sg.Text('Idade', size=(5,0)), sg.Input(size=(15,0), key='idade')],
            [sg.Text('Quais emails voce utiliza?')],
            [sg.Checkbox('Gmail', key='Gmail'), sg.Checkbox('Outlook', key='Outlook'), sg.Checkbox('Yahoo',key='Yahoo')],
            [sg.Text('Aceita cartao?')],
            [sg.Radio('Sim', 'cartoes', key='aceitaCartao'), sg.Radio('Não', 'cartoes', key='naoAceitaCartao')],
            [sg.Text('Velocidade do Script:')],
            [sg.Slider(range=(0,100), default_value=0, orientation='h', size=(15,20), key='sliderVelocidade')],
            [sg.Text('Item:')],
            [sg.Combo(itens, size=(15,0), key='itens')],
            [sg.Button('Enviar dados')],
            [sg.Output(size=(30,20))]
        ]
        #janela
        self.janela = sg.Window("Exemplo PySimpleGUI").layout(layout)

    def Iniciar(self):
        while True:
            #Extrair dados
            self.button, self.values = self.janela.Read()
        
            nome=self.values['nome']
            idade=self.values['idade']
            aceitagmail=self.values['Gmail']
            aceitaoutlook=self.values['Outlook']
            aceitayahoo=self.values['Yahoo']
            aceitaCartao=self.values['aceitaCartao']
            naoAceitaCartao=self.values['naoAceitaCartao']
            itens=self.values['itens']
            velocidadeScript=self.values['sliderVelocidade']
            print(f'Nome:{nome}')
            print(f'Idade:{idade}')
            print(f'Gmail:{aceitagmail}')
            print(f'Outlook:{aceitaoutlook}')
            print(f'Yahoo:{aceitayahoo}')
            print(f'Aceita Cartão:{aceitaCartao}')
            print(f'Não Aceita Cartão:{naoAceitaCartao}')
            print(f'Item: {itens}')
            print(f'Velocidade do Script:{velocidadeScript}')

tela = TelaPython()
tela.Iniciar()
