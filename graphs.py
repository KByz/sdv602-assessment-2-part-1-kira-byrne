import matplotlib as mpl
import matplotlib.pyplot as plt
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

plt.show(bar_chart())