# TODO: how the heck do save - find out and add save button
# TODO: make uuuh prettier
# TODO: add a menubar?


import PySimpleGUI as sg

layout = [
    [sg.T('', size=(8, 1), key='-DATE-'), sg.CalendarButton('Set Date'), sg.I(key='-TASK-', size=(30, 1))],
    [sg.B('Add', key='-ADD-'), sg.Cancel()],
]

window = sg.Window('Todo', layout)

def create_task(tasks):
    layout = [
        [sg.T('', size = (8, 1), key = '-DATE-'), sg.CalendarButton('Set Date'), sg.I(key = '-TASK-', size = (30, 1))]
    ]
    # dynamically add to layout: taskid, task, delete button for each task in tasks
    layout += [[sg.T(idx, size = (3, 1)), sg.T(t, size = (30, 1), key = f'-TX-{idx}'), sg.T('x', key = f'-DEL-{idx}',
                                                                                            enable_events = True)] for
               idx, t in enumerate(tasks, start = 1)]
    # add buttons
    layout += [[sg.B('Add', key = '-ADD-'), sg.Cancel()]]
    # make new window, close existing, make new window main window
    window1 = sg.Window('Todo', layout)
    
    return window1


tasks = []

while True:
    event, values = window.read()
    if event in ['Cancel', sg.WIN_CLOSED]:
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
