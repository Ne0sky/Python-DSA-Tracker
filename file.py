import PySimpleGUI as sg
import pandas as pd

sg.theme('DarkBlack')

EXCEL_FILE= 'Book1.xlsx'
df = pd.read_excel(EXCEL_FILE)

layout=[
    [sg.Text('Enter DSA details ans track your progress')],
    [sg.Text('Date',size=(10,1)), sg.InputText(key='Date')],
    [sg.Text('Topic',size=(10,1)), sg.InputText(key='Topic')],
    [sg.Text('Name',size=(10,1)), sg.InputText(key='Name')],
    [sg.Text('Level',size=(10,1)), 
                                sg.Checkbox('Easy',key='Easy'),
                                sg.Checkbox('Medium',key='Medium'),
                                sg.Checkbox('Hard',key='Hard'),

                                ],

    [sg.Text('Logic',size=(10,1)), sg.InputText(key='Logic')],
    [sg.Submit(),sg.Exit()]
]

window=sg.Window('DSA Tracker',layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Submit':
        df=df.append(values,ignore_index=True)
        df.to_excel(EXCEL_FILE,index=False)
        sg.popup('Data saved!')

window.close()