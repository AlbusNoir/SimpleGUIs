# TODO: Add more operators like sqrt sq etc
# TODO: show the current stuff being done (like if you click 8 + 8 show 8+8)
# TODO: add parenthesis
# TODO: make less clunky (use fors and ifs etc)
# TODO: add backspace?
# TODO: honestly copy the dang windows calc

# noinspection PyPep8Naming
import PySimpleGUI as sg

# noinspection PyTypeChecker
col1 = [
        [sg.B('7', size=(4, 2)), sg.B('8', size=(4, 2)), sg.B('9', size=(4, 2))],
        [sg.B('4', size=(4, 2)), sg.B('5', size=(4, 2)), sg.B('6', size=(4, 2))],
        [sg.B('1', size=(4, 2)), sg.B('2', size=(4, 2)), sg.B('3', size=(4, 2))],
        [sg.B('/', size=(4, 2), key='-DIV-'), sg.B('0', size=(4, 2)), sg.B('', size=(4, 2))],
       ]

# noinspection PyTypeChecker
col2 = [
        [sg.B('x', size=(4, 2), key='-MUL-')],
        [sg.B('-', size=(4, 2), key='-SUB-')],
        [sg.B('+', size=(4, 2), key='-ADD-')],
        [sg.B('=', size=(4, 2), key='-EQL-')],
       ]

# noinspection PyTypeChecker
layout = [
          [sg.I(size=(10, 1), font=(None, 30), key='-DISP-')],
          [sg.Col(col1), sg.VSep(), sg.Col(col2)]
         ]

window = sg.Window('Calculator', layout)

# construct numbers
nums = [str(x) for x in list(range(0, 10))]
num = ''
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event in ['-MUL-', '-SUB-', '-ADD-', '-DIV-']:
        num1 = values['-DISP-']
        window['-DISP-'].update('')
        num = ''
        operation = event
    elif event in nums:
        if len(num) == 0 and event != '0':  # first num 0
            num += event
            window['-DISP-'].update(num)
        elif len(num) > 0:
            num += event
            window['-DISP-'].update(num)
    elif event == '-EQL-':
        num1 = float(num1)
        num2 = float(values['-DISP-'])
        if operation == '-ADD-':
            res = num1 + num2
        elif operation == '-SUB-':
            res = num1 - num2
        elif operation == '-MUL-':
            res = num1 * num2
        elif operation == '-DIV-':
            res = num1 / num2
        window['-DISP-'].update(int(res))
        num = ''
