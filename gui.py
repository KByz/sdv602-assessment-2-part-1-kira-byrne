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
import PySimpleGUI as sg #import GUI library
import matplotlib as mpl #import matplotlib library
import matplotlib.pyplot as plt #import graph plotting library from matplotlib
import numpy as np #import numpy library
import graphs as grph #import graphs.py file
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg #import canvas for graphs

#use TkAgg backend for matplotlib
mpl.use('TkAgg')

"""
Create layout for main window.
sg.Text - define title
sg. Canvas - draw canvas for elements
sg.Input - define input field for username and password
sg.Button - define buttons for each graph type
"""
layout = [
    [sg.Text("Graphing Prototype")],
    [sg.Canvas(key='-CANVAS-')],
    [sg.Text ("Enter Username: "), sg.Input(key="-USERNAME-", do_not_clear=False, size=(30, 1),)],
    [sg.Text ("Enter Password: "), sg.InputText('', key="-PASSWORD-", password_char='*', size=(15, 1))],
    [sg.Button('Pie Chart'), sg.Button('Bar Chart'), sg.Button('Trend Chart'), sg.Exit(button_color='red')]
]

#create child window class for graph buttons
child_window = sg.Window("Graph Window", modal=True)



#draw main parent window
main = sg.Window(
     'Data Exploration Prototype', 
     layout, 
     size=(800, 700),
     location=(0, 0),
     finalize=True,
     element_justification='center',
     font='Helvetica 18',
    )


"""
Event loop for the main window.
Each button opens child window.
Child window returns graph from graphs.gui.py
"""
while True:
        event, values = main.read()
        if event == 'Pie Chart': #button event opens child window
            child_window = sg.Window("Pie Chart", modal=True) #matplotlib draws graph on child window
            plt.show(grph.pie_chart())
            child_window.read()
            child_window.close()
            
        elif event == 'Bar Chart': #button event opens child window
            child_window = sg.Window("Bar Chart", modal=True) #matplotlib draws graph on child window
            plt.show(grph.bar_chart())
            child_window.read()
            child_window.close()
            
        elif event == 'Trend Chart': #button event opens child window
            child_window = sg.Window("Trend Chart", modal=True) #matplotlib draws graph on child window
            plt.show(grph.trend_chart())
            child_window.read()
            child_window.close()
            
        elif event == sg.WIN_CLOSED or event == 'Exit': #break loop and close window
            break


"""
Run main window and close on exit.
"""
if __name__=="__main__": 
     main()

main.close()
