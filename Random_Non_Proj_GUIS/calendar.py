# calendar or something
import PySimpleGUI as sg

layout = [[sg.CalendarButton('Calendar', close_when_date_chosen=True,  target='-IN-', location=(0,0),
                            no_titlebar=False, )],
          [sg.Text('Date chosen:'), sg.Text(key='-IN-', size=(20,1))],
          [sg.Button('Date Popup'), sg.Exit()]]

window = sg.Window('Calendar', layout)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    elif event == 'Date Popup':
        sg.popup('You chose: ', sg.popup_get_date())

window.close()
