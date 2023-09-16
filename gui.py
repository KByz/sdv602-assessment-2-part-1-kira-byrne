import os.path
import PySimpleGUI as sg
import matplotlib.pyplot as plt


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
window = sg.Window('Data Exploration Prototype', layout, size=(800, 500))

while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
window.close()