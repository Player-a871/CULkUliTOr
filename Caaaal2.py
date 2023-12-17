import math

import PySimpleGUI as sg


def ff():
    t = 0
    x1 = 0

    x = 0
    k = 0

    max = 1000

    maxX = 0
    maxK = 0

    Shag = 0.1

    layout = [[sg.Graph(canvas_size=(400, 400), graph_bottom_left=(0, 0), graph_top_right=(400, 400), background_color='red', enable_events=True, key='graph')], [[sg.Button('y = kx'), sg.Button('y = x2')]],
              [sg.Text(''), sg.Input('0')]]

    window = sg.Window('Graph test', layout, finalize=True)

    graph = window['graph']

    rectangle1 = graph.draw_line((0, 200), (400, 200), 'White')
    rectangle2 = graph.draw_line((200, 0), (200, 400), 'White')

    while True:

        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED:
            break

        k = float((values[0]))
        if event == 'Shag':
            k -= 3
        if event == 'y = kx':
            while max > 0:

                x1 += Shag
                y1 = x1 * k
                x -= Shag
                y = x * k

                rectangle = graph.draw_point((x + 200, y + 200), 2, 'white')
                rectangle = graph.draw_point((x1 + 200, y1 + 200), 2, 'white')
                max -= 1
        if event == 'y = x2':
            while max > 0:

                x1 += Shag
                y1 = x1**k
                x -= Shag
                y = x**k

                rectangle = graph.draw_point((x + 200, y + 200), 2, 'white')
                rectangle = graph.draw_point((x1 + 200, y1 + 200), 2, 'white')
                max -= 1
    window.close()
