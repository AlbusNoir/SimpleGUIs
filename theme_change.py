# dynamic theme change in PySimpleGUI
import PySimpleGUI as sg

# main window
def main_window():
    sg.theme(sg.user_settings_get_entry('theme', None))  # this will get the current user theme

    # layout
    layout = [
        [sg.T('Dynamically Change Theme')],
        [sg.T('Theme will update based on user selection')],
        [sg.B('Change Theme', key='-CHANGE_THEME-')],
        [sg.Ok(), sg.Cancel()]
    ]

    return sg.Window('Dynamic Theme', layout)


def theme_window():
    sg.theme(sg.user_settings_get_entry('theme', None))

    layout = [
        [sg.T('Current Theme')],
        [sg.Ok(), sg.B('Theme', key='-THEME-'), sg.B('Exit')]
    ]

    return sg.Window('Current Theme', layout)


def change_theme(window):
    window.close()
    main_window()


def main():
    window = None

    while True:
        if window is None:
            window = main_window()
        event, values = window.read()

        if event in ['Ok', 'Cancel', sg.WIN_CLOSED]:
            break

        if event == '-CHANGE_THEME-':
            theme_window()
            event, values = sg.Window('Choose Theme', [[sg.Combo(sg.theme_list(), key='-THEME LIST-'), sg.Ok(),
                                                        sg.Cancel()]]).read(close=True)
            if event == 'Ok':
                sg.user_settings_set_entry('theme', values['-THEME LIST-'])

                window = change_theme(window)


if __name__ == '__main__':
    main()
