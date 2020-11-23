# simple to-do list to practice pysimplegui
import PySimpleGUI as sg


items = []

run = True
while run:
    print('Enter item or Q to quit\n')
    item = input('Enter item for todo list: ')
    if item not in ['q', 'Q']:
        items.append(item)
    else:
        run = False


total = len(items)


def todoitem(item):
    for x in range(1, total):
        return [sg.CBox(''), sg.In(item)]
        

layout = [todoitem(item) for item in items] + [[sg.B('Save'), sg.B('Exit')]]

window = sg.Window('Simple ToDo', layout)
event, values = window.read()



# TODO add input as window
# TODO add menus for changing theme
# TODO add functionality to save
# TODO add functionality to the checkboxes

