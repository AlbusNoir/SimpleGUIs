import PySimpleGUI as sg
from os import path, remove
from datetime import date
import shutil
import webbrowser


# vars
tool_menu = [
    ['File',['Save', 'Load']],
    ['Options',['Settings']],
    ['About/Contact',['Help', 'About', 'Contact',['Github', 'License Info', 'Website']]]   # help tells what things do
]

tasks = []

today = date.today().strftime('%d%b%Y')

github = 'https://github.com/AlbusNoir'
license = 'https://https://choosealicense.com/licenses/mit/'
site = 'https://kalebsego.com'

# main window
def create_main_window():
    sg.theme(sg.user_settings_get_entry('theme', None))

    layout = [
        [sg.Menu(tool_menu,)],
        [sg.T('', size=(8, 1), key='-DATE-'), sg.CalendarButton('Set Date'), sg.I(key='-TASK-', size=(30, 1))],
        [sg.B('Add Task', key='-ADD-')],
        [sg.HSep()],
        [sg.T('TASKS')],
        [sg.HSep()],
        [sg.B('Exit', key='-EXIT-')]
    ]

    return sg.Window('Todo',  layout)


# task layout and index assignment
def create_task(tasks):
    layout = [
        [sg.Menu(tool_menu)],
        [sg.T('', size=(8, 1), key='-DATE-'), sg.CalendarButton('Set Date'), sg.I(key='-TASK-', size=(30, 1))],
        [sg.B('Add Task', key='-ADD-')],
        [sg.HSep()],
        [sg.T('TASKS')],
    ]

    layout += [[sg.T(idx, size=(3,1)), sg.T(t, size=(30, 1), key=f'-TX-{idx}'), sg.T('x', key=f'-DEL-{idx}',
                                                                                     enable_events=True)] for idx,
                                                                                                              t in enumerate(tasks, start=1)]

    layout += [
        [sg.HSep()],
        [sg.B('Exit', key='-EXIT-')]
    ]

    window = sg.Window('Todo', layout)

    return window


# theme window from clicking settings
def make_theme_window():
    sg.theme(sg.user_settings_get_entry('theme', None))

    layout = [
        [sg.T('Current Theme')],
        [sg.Ok(), sg.B('Theme', key='-THEME-'), sg.B('Exit')]
    ]

    return sg.Window('Current Theme', layout)


# standard save
def save_file(filename):
    if not path.exists(filename):
        if filename not in (None, ''):
            with open(filename, 'w') as f:
                for task in tasks:
                    f.write(task+'\n')
    else:
        save_file_as()


# sep function for temp file handling because we don't need save_file_as for this
def save_temp_file(filename):
    if filename not in (None, ''):
        with open(filename, 'w') as f:
            for task in tasks:
                f.write(task+'\n')


# if file exists when in save_file, do this
def save_file_as():
    filename = sg.popup_get_file('Save File', save_as=True, file_types=(('Text Files', '*.txt'),))
    if filename not in (None, '') and not isinstance(filename, tuple):
        with open(filename, 'w') as f:
            for task in tasks:
                f.write(task+'\n')
    return filename


# standard load
def load_file():
    filename = sg.popup_get_file('Browse', file_types=(('Text Files', '*.txt'),))
    if filename not in (None, ''):
        with open(filename, 'r') as f:
            lines = f.readlines()
            for line in lines:
                line_stripped = line.rstrip('\n')
                tasks.append(line_stripped)
    return filename


# the magic behind making the theme change and not losing tasks
def do_magic(window):
    try:
        save_temp_file('temp.txt')
    except FileExistsError:     # if exists, overwrite it
        shutil.move('temp.txt', 'temp.txt')
    window.close()
    create_main_window()
    window1 = create_task(tasks)
    remove('temp.txt')  # this handles the issue with temp.txt existing, but leaving it in just in case

    return window1


def save_on_exit(filename):
    if filename not in (None, ''):
        if not path.exists(filename):
            with open(filename, 'w') as f:
                for task in tasks:
                    f.write(task + '\n')
        else:
            filename_soe = f'{today}-soe.txt'
            filename = filename_soe
            try:
                with open(filename, 'w') as f:
                    for task in tasks:
                        f.write(task + '\n')
            except FileExistsError:
                shutil.move(filename, filename)




# driver function
def main():
    window = None

    while True:
        if window is None:
            window = create_main_window()
        event, values = window.read()

        if event in ['-EXIT-', sg.WIN_CLOSED]:
            filename = f'{today}.txt'
            save_on_exit(filename)
            break
        if event == '-ADD-':
            task = values['-TASK-'] + ' created on ' + window['-DATE-'].get().split(' ')[0]
            if task not in tasks:
                tasks.append(task)
            window1 = create_task(tasks)
            window.close()
            window = window1
        if event.startswith('-DEL-'):
            idx = int(event.split('-DEL-')[-1])-1
            if tasks:
                del tasks[idx]

            window1 = create_task(tasks)
            window.close()
            window = window1
        if event == 'Save':
            filename = f'{today}.txt'
            save_file(filename)
            sg.popup('File Saved')
        if event in ('Save As',):
            filename = save_file_as()
        if event == 'Load':
            filename = load_file()
            window1 = create_task(tasks)
            window.close()
            window = window1
        if event == 'Settings':
            make_theme_window()

            event, values = sg.Window('Choose Theme', [[sg.Combo(sg.theme_list(), key='-THEME LIST-'), sg.Ok(),
                                                        sg.Cancel()]]).read(close=True)
            if event == 'Ok':
                sg.user_settings_set_entry('theme', values['-THEME LIST-'])

                window = do_magic(window)
        if event == 'Help':
            help_info = '''
            Save - save a copy of your tasks
            Load - load in tasks
            Options>Settings - change the theme
            To use: 
            1)set the date
            2)enter the name for your task
            3)press add task
            
            Program will save your tasks on exit
            '''
            sg.popup_ok(f'{help_info}', title='Help window', )

        if event == 'About':
            about_info = '''
            This is a simple little ToDo list GUI.
            
            Click License menu action for license info
            
            Click Contact menu action for contact info
            '''
            sg.popup_ok(f'{about_info}', title='About window')

        if event == 'Github':
            webbrowser.open(github)

        if event == 'License Info':
            webbrowser.open(license)

        if event == 'Website':
            webbrowser.open(site)



# do the thing
if __name__ == '__main__':
    main()
