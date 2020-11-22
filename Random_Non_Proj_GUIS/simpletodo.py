# simple to-do list to practice pysimplegui
import PySimpleGUI as sg

rangenum = int(input('How many items should we create? '))

def todoitem(num):
    return [sg.Text(f'{num}. '), sg.CBox(''), sg.In()]


layout = [todoitem(x) for x in range(1, rangenum+1)] + [[sg.B('Save'), sg.B('Exit')]]

window = sg.Window('Simple ToDo', layout)
event, values = window.read()



# TODO add rangenum as a window
# TODO add menus for changing theme
# TODO add functionality to save
# TODO add functionality to the checkboxes

