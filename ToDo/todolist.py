# TODO: make uuuh prettier
# TODO: add a menubar - DO IT
# TODO: menubar: save, load, new?, change theme, about, etc


import PySimpleGUI as sg
import os
from datetime import date

layout = [
    [sg.T('', size=(8, 1), key='-DATE-'), sg.CalendarButton('Set Date'), sg.I(key='-TASK-', size=(30, 1))],
    [sg.B('Add Task', key='-ADD-')],
    [sg.B('Save', key='-SAVE-'), sg.B('Load', key='-LOAD-')],
    [sg.B('Exit', key='-EXIT-')]
]

window = sg.Window('Todo', layout)

def create_task(tasks):
    layout = [
        [sg.T('', size = (8, 1), key='-DATE-'), sg.CalendarButton('Set Date'), sg.I(key='-TASK-', size = (30, 1))]
    ]
    # dynamically add to layout: taskid, task, delete button for each task in tasks
    layout += [[sg.T(idx, size = (3, 1)), sg.T(t, size = (30, 1), key=f'-TX-{idx}'), sg.T('x', key=f'-DEL-{idx}',
                                                                                            enable_events = True)] for
               idx, t in enumerate(tasks, start = 1)]
    # add buttons
    layout += [
        [sg.B('Add Task', key = '-ADD-')],
        [sg.B('Save', key = '-SAVE-'), sg.B('Load', key = '-LOAD-')],
        [sg.B('Exit', key = '-EXIT-')]
    ]
    # make new window, close existing, make new window main window
    window1 = sg.Window('Todo', layout)
    
    return window1


def save_file(filename):
    if not os.path.exists(filename):
        if filename not in (None, ''):
            with open(filename, 'w') as f:
                for task in tasks:
                    f.write(task+'\n')
    else:
        file_save_as()


def file_save_as():
    filename = sg.popup_get_file('Save File', save_as=True, no_window=True, file_types=(('Text Files', '*.txt'),))
    if filename not in (None, '') and not isinstance(filename, tuple):
        with open(filename, 'w') as f:
            for task in tasks:
                f.write(task+'\n')
    return filename


def load_file():
    filename = sg.popup_get_file('Browse', file_types=(('Text Files', '*.txt'),))
    if filename not in (None, ''):
        with open(filename, 'r') as f:
            lines = f.readlines()
            for line in lines:
                line_stripped = line.rstrip('\n')
                tasks.append(line_stripped)

    return filename

tasks = []

today = date.today()
cur_date = today.strftime('%d%b%Y')

while True:
    event, values = window.read()
    if event in ['-EXIT-', sg.WIN_CLOSED]:
        break
    if event == '-ADD-':
        # get value in -TASK-, get value of -DATE-, split on space, grab index 0
        task = values['-TASK-'] + ' created on ' + window['-DATE-'].get().split(' ')[0]
        if task not in tasks:
            tasks.append(task)
        window1 = create_task(tasks)
        window.close()
        window = window1
    elif event.startswith('-DEL-'):
        # set idx equal to the last index of -DEL-{idx} after splitting on -DEL-
        idx = int(event.split('-DEL-')[-1]) - 1
        if tasks:
            del tasks[idx]

        window1 = create_task(tasks)
        window.close()
        window = window1

    elif event == '-SAVE-':
        filename = f'{cur_date}.txt'
        save_file(filename)
        sg.popup('File saved')
    elif event in ('Save As',):
        filename = file_save_as()
    elif event == '-LOAD-':
        filename = load_file()
        window1 = create_task(tasks)
        window.close()
        window = window1