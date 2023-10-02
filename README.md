# sdv602-assessment-2-part-1-kira-byrne
A repository for SDV602 assessment 1 part 1

The purpose of this project is to create a data exploration software using Python and supported by applicable Python libraries / modules. 
This application will be able to use raw data and provide visualsation through various graphs.

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

NOTE:
As of stage 1, the application is in a prototype mode and is a work in progress. This current form is merely a visual proposal of the finalised application.
Expect the following bugs:

    There will be a login screen that will not require input. 
    The buttons opening up MatPlotLib graphs will only show one at a time and will crash the application on closing. 


TO RUN THIS PROGRAM:
1. Download the repository from github https://github.com/KByz/sdv602-assessment-2-part-1-kira-byrne.
    1A. ZIP FOLDER METHOD - Download the zip folder of this repository under the download tab.
        Open and extrac the contents into a clean folder in your desired working space. 
        Open the folder in Visual Studio Code or another applicable coding platform. 
    1B. GIT CLONE METHOD - Copy the URL from the download tab in the repository. 
        Open your workspace folder in Visual Studio Code or other applicable coding platform. 
        In the bash terminal type "git clone [PASTE URL]" and hit enter. A foler containting the contents of the repository should
        be retrived and added to the local machine. 
2. Download the following libraries using the pip command in powershell 
    2A. PySimpleGUI
    2B. MatPlotLib
    2C. NumPy
    2D. Pandas
3. In the bash terminal type "python gui.py" and hit enter.
4. The window will display login input fields.
    STAGE 1: The input fields are dummies. They do not require any valid details. 
    STAGE 2: Valid user login will be required to use the app features.Enter the following: 
            Username: "User1", Password: "Password1"
5. Select a button to display the static mock data through either a pie chart, bar chart, or trend chart. 
    WIP: Each graph window will crash the application upon closing OR when attemping to open more than 1 graph window. 

