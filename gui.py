"""""
Create a GUI that can explore a set of data through three graph types.
Using MatPlotLib to create the graphs, import data file and create a GUI.

The proposed raw data will be a csv file imported from a webpage. 
The data is a census recording of commute methods in a slection of New Zealand regions from 2017 to 2023.
Available graphs inluce:
    1. Pie
    2. Bar
    3. Trend

The app must also contain a login screen that will connect to a database to verify the user.

The exploration features of the app will allow users to zoom and pan the graphs, and open a chat window
to message other collegues who are logged in. 

AT STAGE ONE the repository will contain a prototype to propose the design of the app.
This will include 
    1. A non-functional login page
    2. Three data exploration screens (DES) containing the graphs

AT STAGE 2 the repository will contain a functional prototype of the app.
This will include:
    1. A functional login page
    2. Three DES containing the graphs with data that can be manipulated in-app
    3. Viewing features zoom and pan
    4. A live chat function

"""""
import os.path
import PySimpleGUI as sg
import matplotlib as matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import graphs as grph
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
    [sg.Text ("Enter Username: "), sg.Input(key="-USERNAME-", do_not_clear=False, size=(30, 1))],
    [sg.Text ("Enter Password: "), sg.InputText('', key="-PASSWORD-", password_char='*', size=(15, 1))],
    [sg.Button('Pie Chart'), sg.Button('Bar Chart'), sg.Button('Trend Chart'), sg.Exit(button_color='red')]
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
     size=(800, 700),
     location=(0, 0),
     finalize=True,
     element_justification='center',
     font='Helvetica 18',
    )

# Add graph to the window
draw_graph(window['-CANVAS-'].TKCanvas, fig)

event, values = window.read()


while True:
        event, values = window.read()
        if event == 'Pie Chart':
             plt.show(grph.pie_chart()),
        elif event == 'Bar Chart':
             plt.show(grph.bar_chart()),
        elif event == 'Trend Chart':
             plt.show(grph.trend_chart()),
        elif  event == sg.WIN_CLOSED or event == 'Exit':
            break

window.close()
