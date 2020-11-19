# REF:
# https://pypi.org/project/wolframalpha/
# https://pysimplegui.readthedocs.io/en/latest/

import wolframalpha
import PySimpleGUI as sg

client = wolframalpha.Client("YOUR-APPID-HERE")  # https://developer.wolframalpha.com/portal/myapps/

sg.theme('DarkBlue2')  # colours -> tinyurl.com/y2frr9sc
layout = [[sg.Text('WolframAlpha Search')],
          [sg.Text('Please enter a query:'), sg.InputText()],
          [sg.Button('Query'), sg.Button('Close'), sg.Button('Info')]]


window = sg.Window('Wolfram Search', layout, icon='favicon.ico')

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Close':
        break
    elif event == 'Info':
        sg.Popup("""
        WolframSearch
        Dev: Kale|AlbusNoir
        Github: github.com/AlbusNoir
        License: MIT""")
    else:
        try:
            wolfram_res = next(client.query(values[0]).results).text
            sg.Popup("Wolfram result: "+wolfram_res)
        except:
            sg.Popup("Could not find result")


window.close()
