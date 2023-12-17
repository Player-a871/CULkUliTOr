import math

import Caaaal2
import PySimpleGUI as sg

MenuDef = [('S', 'Геометрия')]

layout = [[sg.Menu(MenuDef, pad=(20, 1))],
          [sg.Text('', font=(20, 20)), sg.Text('0', size=(20, 1), font=(20, 20), key='-OUTPUT-')],
          [sg.Button('x²', font=(20, 20), size=(2, 1)), sg.Button('1', font=(20, 20), size=(2, 1)), sg.Button('2', size=(2, 1), font=(20, 20)), sg.Button('3', size=(2, 1), font=(20, 20)), sg.Button('←', size=(8, 1), font=(20, 20)), sg.Button('🚪', size=(2, 1), font=(20, 20))],
          [sg.Button('√x', font=(20, 20), size=(2, 1)), sg.Button('4', size=(2, 1), font=(20, 20)), sg.Button('5', size=(2, 1), font=(20, 20)), sg.Button('6', size=(2, 1), font=(20, 20)), sg.Button('-', size=(11, 1), font=(20, 20))],
          [sg.Button('¹/ₓ', font=(20, 20), size=(2, 1)), sg.Button('7', size=(2, 1), font=(20, 20)), sg.Button('8', size=(2, 1), font=(20, 20)), sg.Button('9', size=(2, 1), font=(20, 20)), sg.Button('+', size=(11, 1), font=(20, 20))],
          [sg.Button('0', size=(2, 1), font=(20, 20)), sg.Button('÷', size=(5, 1), font=(20, 20)), sg.Button('×', size=(5, 1), font=(20, 20)), sg.Button('=', size=(8, 1), font=(20, 20))]]

window = sg.Window('⚝БУЛЬБА⚝', layout)

Plus = False
Minus = False
Div = False
Mul = False
Convert = False

x = 0
y = 0
z = 0

while True:
    event, values = window.read()
    sg.theme('Reds')
    if event in (None, ''):
        break
    text_elem = window['-OUTPUT-']

    if not Plus or not Minus or not Div or not Mul:

        if event == '←':
            x = x // 10
            text_elem.update("{}".format(x))

        if event == '1':
            x = x * 10 + 1
            text_elem.update("{}".format(x))

        if event == '2':
            x = x * 10 + 2
            text_elem.update("{}".format(x))

        if event == '3':
            x = x * 10 + 3
            text_elem.update("{}".format(x))

        if event == '4':
            x = x * 10 + 4
            text_elem.update("{}".format(x))

        if event == '5':
            x = x * 10 + 5
            text_elem.update("{}".format(x))

        if event == '6':
            x = x * 10 + 6
            text_elem.update("{}".format(x))

        if event == '7':
            x = x * 10 + 7
            text_elem.update("{}".format(x))

        if event == '8':
            x = x * 10 + 8
            text_elem.update("{}".format(x))

        if event == '9':
            x = x * 10 + 9
            text_elem.update("{}".format(x))

        if event == '0' and x > 0:
            x = x * 10 + 0
            text_elem.update("{}".format(x))

        if event == '+':
            Plus = True
            Minus = False
            Div = False
            Mul = False
            text_elem.update("{}".format(0))

        if event == '-':
            Minus = True
            Plus = False
            Div = False
            Mul = False
            text_elem.update("{}".format(0))

        if event == '÷':
            Div = True
            Minus = False
            Plus = False
            Mul = False
            text_elem.update("{}".format(0))

        if event == '×':
            Mul = True
            Div = False
            Minus = False
            Plus = False
            text_elem.update("{}".format(0))

        if event == 'x²':
            x = x * x
            text_elem.update("ОТВЕТ: {}".format(x))
            x = 0

        if event == '√x':
            x = math.sqrt(x)
            text_elem.update("ОТВЕТ: {}".format(x))
            x = 0

        if event == '¹/ₓ':
            x = 1 / x
            text_elem.update("ОТВЕТ: {}".format(x))
            x = 0

    # if event == '🚪':

    if event == 'Геометрия':
        Caaaal2.ff()

    if Plus or Minus or Div or Mul:

        if event == '<---':
            y = y // 10
            text_elem.update("{}".format(y))

        if event == '1':
            y = y * 10 + 1
            text_elem.update("{}".format(y))

        if event == '2':
            y = y * 10 + 2
            text_elem.update("{}".format(y))

        if event == '3':
            y = y * 10 + 3
            text_elem.update("{}".format(y))

        if event == '4':
            y = y * 10 + 4
            text_elem.update("{}".format(y))

        if event == '5':
            y = y * 10 + 5
            text_elem.update("{}".format(y))

        if event == '6':
            y = y * 10 + 6
            text_elem.update("{}".format(y))

        if event == '7':
            y = y * 10 + 7
            text_elem.update("{}".format(y))

        if event == '8':
            y = y * 10 + 8
            text_elem.update("{}".format(y))

        if event == '9':
            y = y * 100 // 10 + 9
            text_elem.update("{}".format(y))

        if event == '0' and y > 0:
            y = y * 10 + 0
            text_elem.update("{}".format(y))

    if event == '=' and x > 0 and y > 0:

        x = str(x)
        i = int(x.replace(str(y), "", 1))
        x = int(x)

        if Plus:
            z = i + y
            Plus = False
            text_elem.update("ОТВЕТ: {}".format(z))
            x = 0
            y = 0

        if Minus:
            z = i - y
            Minus = False
            text_elem.update("ОТВЕТ: {}".format(z))
            x = 0
            y = 0

        if Div:
            z = i / y
            Div = False
            text_elem.update("ОТВЕТ: {}".format(z))
            x = 0
            y = 0

        if Mul:
            z = i * y
            Mul = False
            text_elem.update("ОТВЕТ: {}".format(z))
            x = 0
            y = 0

window.close()
