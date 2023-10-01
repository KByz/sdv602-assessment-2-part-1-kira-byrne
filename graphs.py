"""
GRAPH PLOTTING TEST SCRIPTS

Create three graph types to be called by child windows in the main GUI.
The graphs will be created using MatPlotLib and displayed in the GUI using PySimpleGUI.
The following graphs will be:
    Pie chart
    Bar chart
    Trend chart
AT STAGE 1:
Each graph will have mock data in the form of a dictionary.
This data will return a graph when called by the child window.

AT STAGE 2: The graphs will import data from a csv file located on a webserver.

"""

import matplotlib as mpl #import matplotlib library
import matplotlib.pyplot as plt #import graph plotting library from matplotlib
import pandas as pd #import pandas data manipulation library
import numpy as np #import numpy library
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg #import canvas for graphs

mpl.use('TkAgg') #use tkinter backend for matplotlib
"""
Create bar chart with mock data displaying the uptake of IT majors at NMIT.

plt.x
plt.y
plt.title ("IT major enrollments 2023")
plt.show()

"""
def bar_chart(*args):
    data = {'SDV':20, 'HWD': 35,'ISYS': 15}
    majors = list(data.keys())
    values = list(data.values())
    plt.figure(1)

    plt.bar(majors, values, color='green', width=0.5)

    plt.xlabel("Majors")
    plt.ylabel("Number of Enrollments")
    plt.title("Uptake of IT Majors")
    plt.show()

"""
Create pie chart with mock data displaying the modes of commute in July 2023.

plt.pie
plt.title ("Modes of Commute July 2023")
dictionary (mode of commute, number of people)
plt.show()
"""
def pie_chart(*args):
    data = {'Personal Car': 26000, 'Bus': 14230, 'Train': 12140, 'Bicycle': 8014, 'Walk': 4410}
    modes = list(data.keys())
    values = list(data.values())

    plt.figure(2)
    plt.pie(values, labels=modes, autopct='%1.1f%%', shadow=True, startangle=140)

    plt.axis('equal')
    plt.title("Modes of Commute July 2023")
    plt.show()

"""
Create trend chart with mock data displaying the yearly number of bus passangers from 2018 to 2024.
plt.x axis
plty.y axis
plt.title ("Bus Passangers 2018-2024")
dictornary (year, bus passangers)
plt.show()
"""
def trend_chart(*args):
    Bus = {
        "Bus_Passangers": [43191, 41042, 15293, 19183, 35193, 56180, 68113],
        "Year": [2018, 2019, 2020, 2021, 2022, 2023, 2024]
    }
    
    df = pd.DataFrame(Bus)
    print(df)
    plt.figure(3)
    df.plot(x="Year", y="Bus_Passangers", kind="line")
    plt.show()

