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
#Import matplot lib and numpy libraries to plot graphs and manipulate data with math functions.
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import numpy as np
import matplotlib.pyplot as plt

#Draw window
import PySimpleGUI as sg
layout = [[sg.Text('Data Exploration Prototype')], [sg.Button('Pie Chart')], [sg.Button('Bar Chart')], [sg.Button('Trend Chart')]]
window = sg.Window('Data Exploration Prototype', layout, size=(800, 500))
sg.theme('Red2')   # Add a touch of color
while True:
        event, values = window.read()
        if event == 'Pie Chart':
            pie_chart()
        if event == 'Bar Chart':
            bar_chart()
        if event == 'Trend Chart':
            trend_chart()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
window.close()

data_select_column = [
     [sg.Text('Select Data to Display')],
     sg.In(size=(25, 1), enable_events=True, key='-IN-'),
        sg.FileBrowse(),
],
[
        sg.Listbox(
             values=[], enable_events=True, size=(40, 20), key='-FILE LIST-'
        )
]
"""
def pie_chart():
     
     #Import raw data to form pie chart.
     

def bar_cart():
     
def trend_chart():
     
"""
def draw_graph (canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg

def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg


def delete_graph_agg(graph_agg):
    graph_agg.get_tk_widget().forget()
    plt.close('all')



def pie_graph():
     plt.title('Pie Chart')
     plt.tight_layout()
     plt.show()

    #colours
        #Yellow, Blue, Red, Green, Pink

def pie_chart1(**kwargs):
    """
    Pie chart, where the slices will be ordered and plotted counter-clockwise.

    Args 
          **kwargs lets you pass arguments into this function
    """
    labels = 'C', 'Python', 'Java', 'C++', 'C#'
    sizes = [13.38, 11.87, 11.74, 7.81, 4.41]
    explode = (0, 0.1, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Python')

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=0)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.title('TIOBE Index for May 2021')
    #plt.show()
    return plt.gcf()