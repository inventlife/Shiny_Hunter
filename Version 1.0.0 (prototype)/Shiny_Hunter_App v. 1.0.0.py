import paramiko
from tkinter import *
from tkinter import ttk
import numpy

# Create an instance of tkinter frame or window
win = Tk()
win.resizable(False, False)
win.configure(bg='#DBCDC6')
win.title("Shiny Hunter")

# Set the size of the window
win.geometry("800x780")
screen_width, screen_height = win.winfo_screenwidth(), win.winfo_screenheight()

Settings = Frame(win)
Settings.configure(bg = "#DBCDC6")

Settings.pack(fill='both', expand=1)

# Define a function for switching the frames and getting IP address
def AcceptIPAddress():
   global ShinyHunterIPAddress
   global IPAddress
   IPAddress = ShinyHunterIPAddress.get()
   print (IPAddress)
   IPLabel.configure(text="Hunter's IP Address: " + IPAddress)


# FUNCTIONS FOR PI MODS
def RouteRGBValuesSet():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect( IPAddress, username = Username, password = Password )

    stdin, stdout, stderr = ssh.exec_command("cp ~/Desktop/Shiny_Hunter/Database/"+Route+"RGBValues.py ~/Desktop/Shiny_Hunter/RGBValues.py")

    stdin, stdout, stderr = ssh.exec_command("sed -i 's/Sensitivity = .*/Sensitivity = "+Sensitivity+"/' ~/Desktop/Shiny_Hunter/Twenty.py")

    stdin, stdout, stderr = ssh.exec_command("python3 ~/Desktop/Shiny_Hunter/Twenty.py")

#/////

#Settings
SettingsTitle = Label(Settings, text="Shiny Hunter", bg ="#DBCDC6", foreground="#1E212B", font=("Courier 24 bold"))
SettingsTitle.pack(pady=10)

IPLabel=Label(Settings, text="Hunter's IP Address: ", bg ="#DBCDC6")
IPLabel.pack()
ShinyHunterIPAddress = Entry(Settings, fg='#1e212b', highlightthickness=0, relief='sunken', width = 23, bg = "white")
ShinyHunterIPAddress.pack()
IPAddressInputBtn = Button(Settings, text = "Save", highlightthickness=0, fg = "#1E212B", bg = '#fbffe7', width = 6, command = AcceptIPAddress)
IPAddressInputBtn.pack(pady=10)

def AcceptUsername():
    global UsernameInput
    global Username
    Username = UsernameInput.get()
    print (Username)
UsernameInputTitle = Label(Settings, text = "Input the Shiny Hunter Username (Default = pi):", bg = "#DBCDC6")
UsernameInputTitle.pack(pady=10)
UsernameInput = Entry(Settings, fg='#1e212b', highlightthickness=0, relief='sunken', width = 23, bg = "white")
UsernameInput.pack()
UsernameInputButton = Button(Settings, text= "Save", highlightthickness=0, fg ="#1E212B", bg = "#fbffe7", width= 6, command= AcceptUsername)
UsernameInputButton.pack(pady=10)

def AcceptPassword():
    global PasswordInput
    global Password
    Password = PasswordInput.get()
    print (Password)
PasswordInputTitle = Label(Settings, text = "Input the Shiny Hunter Password (Default = raspberry):", bg = "#DBCDC6")
PasswordInputTitle.pack(pady=10)
PasswordInput = Entry(Settings, fg='#1e212b', highlightthickness=0, relief='sunken', width = 23, bg = "white")
PasswordInput.pack()
PasswordInputButton = Button(Settings, text= "Save", highlightthickness=0, fg ="#1E212B", bg = "#fbffe7", width= 6, command= AcceptPassword)
PasswordInputButton.pack(pady=10)

def AcceptSensitivity():
    global SensitivityInput
    global Sensitivity
    Sensitivity = SensitivityInput.get()
    print (Sensitivity)
SensitivityInputTitle = Label(Settings, text = "Input the color detection sensitivity as a float. Number selection advice can be found in the Github repo. \n 1 >= high sensitivity and may miss shiny pokemon. 3 =< low sensitive and might get false positives:", bg = "#DBCDC6")
SensitivityInputTitle.pack(pady=10)
SensitivityInput = Entry(Settings, fg='#1e212b', highlightthickness=0, relief='sunken', width = 23, bg = "white")
SensitivityInput.pack()
SensitivityInputButton = Button(Settings, text= "Save", highlightthickness=0, fg ="#1E212B", bg = "#fbffe7", width= 6, command= AcceptSensitivity)
SensitivityInputButton.pack(pady=10)

def AcceptRoute():
    global RouteInput
    global Route
    Route = RouteInput.get()
    print (Route)
RouteInputTitle = Label(Settings, text = "Input the game and location you will be hunting in. Ex: Black2Route5 or DiamondLakeValor. Locations are in the repo", bg = "#DBCDC6")
RouteInputTitle.pack(pady = 10)
RouteInput = Entry(Settings, fg='#1e212b', highlightthickness=0, relief='sunken', width = 35, bg = "White")
RouteInput.pack()
RouteInputBtn = Button(Settings, text = "Save", highlightthickness=0, fg = "#1E212B", bg = "#fbffe7", width = 6, command = AcceptRoute)
RouteInputBtn.pack(pady = 10)

ConnectButton = Button(Settings, text = "Start Hunt", highlightthickness=0, fg = "#1E212B", bg = "#fbffe7", width =  20, command = RouteRGBValuesSet)
ConnectButton.pack(pady = 30)

#////////
Settings.mainloop()
