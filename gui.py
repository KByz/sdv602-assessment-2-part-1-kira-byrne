import os.path
import PySimpleGUI as sg
import matplotlib as matplotlib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

fig = matplotlib.figure.Figure(figsize=(5, 4), dpi=100)
t = np.arange(0, 3, .01)
fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))

matplotlib.use('TkAgg')

def draw_graph(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg

data_select_column = [
    [sg.Text('Select Data to Display')],
    sg.In(size=(25, 1), enable_events=True, key='-FILE-'),
    sg.FileBrowse(),
],

[
        sg.Listbox(
             values=[], enable_events=True, size=(40, 20), key='-FILE LIST-'
        )
]

graph_canvas = [
    [sg.Text('Select a graph to display')],
    [sg.Text(size=(40, 1), key='-TOUT-')],
    [sg.Image(key='-IMAGE-')],
]

#layout 2
layout = [
    [sg.Text("Graphing Prototype")],
    [sg.Canvas(key='-CANVAS-')],
    [sg.Button('Pie Chart'), sg.Button('Bar Chart'), sg.Button('Trend Chart'), sg.Exit()]
]
"""
LAYOUT 1

layout = [
    [
     sg.Column(data_select_column),
     sg.VSeperator(),
    sg.Column(graph_canvas),
    ],
    [sg.Text('Data Exploration Prototype')],
    [sg.Button('Pie Chart')],
    [sg.Button('Bar Chart')],
    [sg.Button('Trend Chart')]
    
    ]
"""
#draw new window
window = sg.Window(
     'Data Exploration Prototype', 
     layout, 
     size=(800, 500),
     location=(0, 0),
     finalize=True,
     element_justification='center',
     font='Helvetica 18',
    )

# Add graph to the window
draw_graph(window['-CANVAS-'].TKCanvas, fig)

event, values = window.read()

window.close()
"""
while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
window.close()
"""