import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def bar_chart():
    data = {'SDV':20, 'HWD': 35,'ISYS': 15}
    majors = list(data.keys())
    values = list(data.values())

    plt.bar(majors, values, color='green', width=0.5)

    plt.xlabel("Majors")
    plt.ylabel("Number of Enrollments")
    plt.title("Uptake of IT Majors")
    plt.show()

def pie_chart():
    data = {'Personal Car': 26000, 'Bus': 14230, 'Train': 12140, 'Bicycle': 8014, 'Walk': 4410}
    modes = list(data.keys())
    values = list(data.values())

    plt.pie(values, labels=modes, autopct='%1.1f%%', shadow=True, startangle=140)
    plt.axis('equal')
    plt.title("Modes of Commute July 2023")
    plt.show()

def trend_chart():
    Bus = {
        "Bus_Passangers": [43191, 41042, 15293, 19183, 35193, 56180, 68113],
        "Year": [2018, 2019, 2020, 2021, 2022, 2023, 2024]
    }
    df = pd.DataFrame(Bus)
    print(df)

    df.plot(x="Year", y="Bus_Passangers", kind="line")
    plt.show()



