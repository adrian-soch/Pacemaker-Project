#Imports
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3

import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

from matplotlib import style
style.use('ggplot')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure


#Creating sqlite3 database
db = sqlite3.connect("DCM.sqlite", detect_types= sqlite3.PARSE_DECLTYPES)

#Create seperate table for each state within database
db.execute("CREATE TABLE IF NOT EXISTS users (user TEXT NOT NULL, password TEXT NOT NULL, codename TEXT NOT NULL)")

#Current User
currentuser = ''

#Initializing all global variables with "0"
userlog = ''
#AOO
aoo_lowerRateLimitEntry,aoo_upperRateLimitEntry,aoo_atrialAmplitudeEntry,aoo_atrialPulseWidthEntry = "0","0","0","0"

#VOO
voo_lowerRateLimitEntry,voo_upperRateLimitEntry,voo_ventricularAmplitudeEntry,voo_ventricularPulseWidthEntry = "0","0","0","0"

#AAI
aai_lowerRateLimitEntry,aai_upperRateLimitEntry,aai_atrialAmplitudeEntry,aai_atrialPulseWidthEntry,aai_atrialSensitivityEntry,aai_ARPEntry,aai_PVARPEntry,aai_hysteresisEntry,aai_rateSmoothingEntry = "0","0","0","0","0","0","0","0","0"

#VVI
vvi_lowerRateLimitEntry,vvi_upperRateLimitEntry,vvi_ventricularAmplitudeEntry,vvi_ventricularPulseWidthEntry,vvi_ventricularSensitivityEntry,vvi_VRPEntry,vvi_hysteresisEntry,vvi_rateSmoothingEntry = "0","0","0","0","0","0","0","0"

#DOO
doo_lowerRateLimitEntry, doo_upperRateLimitEntry, doo_atrialAmplitudeEntry, doo_atrialPulseWidthEntry, doo_ventricularAmplitudeEntry, doo_ventricularPulseWidthEntry, doo_fixedAVDelayEntry = "0","0","0","0","0","0","0"

#AOOR
aoor_lowerRateLimitEntry, aoor_upperRateLimitEntry, aoor_atrialAmplitudeEntry, aoor_atrialPulseWidthEntry, aoor_maximumSensorRateEntry, aoor_activityThresholdEntry, aoor_reactionTimeEntry, aoor_responseFactorEntry, aoor_recoveryTimeEntry = "0","0","0","0","0","","0","0","0"

#VOOR
voor_lowerRateLimitEntry, voor_upperRateLimitEntry, voor_ventricularAmplitudeEntry, voor_ventricularPulseWidthEntry, voor_maximumSensorRateEntry, voor_activityThresholdEntry, voor_reactionTimeEntry, voor_responseFactorEntry, voor_recoveryTimeEntry = "0","0","0","0","0","","0","0","0"

#AAIR
aair_lowerRateLimitEntry, aair_upperRateLimitEntry, aair_atrialAmplitudeEntry, aair_atrialPulseWidthEntry, aair_atrialSensitivityEntry, aair_ARPEntry, aair_PVARPEntry, aair_hysteresisEntry, aair_rateSmoothingEntry, aair_maximumSensorRateEntry, aair_activityThresholdEntry, aair_reactionTimeEntry, aair_responseFactorEntry, aair_recoveryTimeEntry = "0","0","0","0","0","0","0","0","0","0","","0","0","0"

#VVIR
vvir_lowerRateLimitEntry, vvir_upperRateLimitEntry, vvir_ventricularAmplitudeEntry, vvir_ventricularPulseWidthEntry, vvir_ventricularSensitivityEntry, vvir_VRPEntry, vvir_hysteresisEntry, vvir_rateSmoothingEntry, vvir_maximumSensorRateEntry, vvir_activityThresholdEntry, vvir_reactionTimeEntry, vvir_responseFactorEntry, vvir_recoveryTimeEntry = "0","0","0","0","0","0","0","0","0","","0","0","0"

#DOOR
door_lowerRateLimitEntry, door_upperRateLimitEntry, door_atrialAmplitudeEntry, door_atrialPulseWidthEntry, door_ventricularAmplitudeEntry, door_ventricularPulseWidthEntry, door_maximumSensorRateEntry, door_fixedAVDelayEntry, door_activityThresholdEntry, door_reactionTimeEntry, door_responseFactorEntry, door_recoveryTimeEntry = "0","0","0","0","0","0","0","0","0","0","0","0"

#Creating Initial Welcome Frame
class WelcomeFrame:
    def __init__(self, master):
        #General paramters
        self.master = master
        self.master.title("WELCOME to DCM")
        self.master.configure(background='grey')
        self.frame = tk.Frame(self.master)
        self.master.resizable(width=False, height=False)

        #Label details
        self.label_welcome = tk.Label(self.master, text="Welcome")
        self.label_welcome.config(font=("Helvetica",34))
        self.label_welcome.configure(background='grey')
        self.label_welcome.grid(row=1,column=2,columnspan =1,padx = 200, pady = 20)

        #Next window button
        self.nxtbtn = tk.Button(self.master, text="Next", width=12, command=self._nxt_btn_clicked)
        self.nxtbtn.grid(row=3,column=2,columnspan =1,padx = 200, pady = 20)
        self.nxtbtn.focus()

        #Return button binding
        self.master.bind('<Return>', self.return_bind)
    
    #Return Button method
    def return_bind(self, event):
        self._nxt_btn_clicked()

    #Method to create new window
    def new_window(self,window):
        self.newWindow = tk.Toplevel(self.master)
        self.app = window(self.newWindow)

    #Method to transition to loginframe
    def _nxt_btn_clicked(self):
        self.master.withdraw()
        self.new_window(LoginFrame)     
    
    #Method to cleanup closing window
    def on_exit(self):
        exit()

#Login Frame window
class LoginFrame:
    def __init__(self, master):
        #General parameters
        self.master = master
        self.master.title("USER LOGIN")
        self.master.configure(background='grey')
        self.frame = tk.Frame(self.master)
        self.master.resizable(width=False, height=False)

        #Label details
        self.label_username = tk.Label(self.master, text="Username")
        self.label_username.configure(background='grey')
        self.label_password = tk.Label(self.master, text="Password")
        self.label_password.configure(background='grey')

        #Window positioning
        self.master.rowconfigure(0, pad=3)
        self.master.rowconfigure(1, pad=3)
        self.master.rowconfigure(2, pad=3)
        self.master.rowconfigure(3, pad=3)
        self.master.rowconfigure(4, pad=3)
        self.master.rowconfigure(5, pad=3)

        #Enter username/password details
        self.entry_username = tk.Entry(self.master)
        self.entry_password = tk.Entry(self.master, show="*")
        self.entry_username.focus()
        self.label_username.grid(row=0, sticky='e', pady=5)
        self.label_password.grid(row=1, sticky='e', pady=10)
        self.entry_username.grid(row=0, column=1, columnspan = 1,sticky='w')
        self.entry_password.grid(row=1, column=1, columnspan = 1,sticky='w')

        #Add user and login button details
        self.logbtn = tk.Button(self.master, text="Login", width=12, command=self._login_btn_clicked)
        self.logbtn.grid(columnspan=2, padx = 80, pady = 0)
        self.add_userbtn = tk.Button(self.master, text="Add user",width =12, command=self._add_user_btn_clicked)
        self.add_userbtn.grid(columnspan =2,padx = 80, pady = 10)
        self.login_successful = False
        self.master.protocol("WM_DELETE_WINDOW", self.on_exit)

        #Return button bind
        self.master.bind('<Return>', self.return_bind)

    #Return button method  
    def return_bind(self, event):
        self._login_btn_clicked()

    #Method to cleanup closing application
    def on_exit(self):
        if messagebox.askyesno("EXIT", "Do you want to quit the application?"):
            exit()

    #Method to create new window
    def new_window(self,window):
        self.newWindow = tk.Toplevel(self.master)
        self.app = window(self.newWindow)

    #Method to add transition to add new user screen
    def _add_user_btn_clicked(self):
        self.entry_username.delete(0, 'end')
        self.entry_password.delete(0, 'end')
        self.new_window(AddUserWindow)

    #Method to for login button
    def _login_btn_clicked(self):
        global currentuser, uNAME
        username = self.entry_username.get()
        password = self.entry_password.get()
        self.entry_username.delete(0, 'end')
        self.entry_password.delete(0, 'end')

        #Query Database to find username and password
        cursor = db.execute("SELECT * FROM users WHERE (user = ?) and (password = ?)", (username,password,))
        row = cursor.fetchall()

        if row:
            #If username is found then they become the current user
            uNAME = str(row[0][1])
            currentuser = str(row[0][2])
            self.master.withdraw()
            self.new_window(MainWindow)
        else:
            #Otherwise the username/password is wrong
            messagebox.showerror("ERROR", "Username/Password is Incorrect")

#Add new user class window
class AddUserWindow:
    def __init__(self, master):
        #Setting default window parameters
        self.master = master
        self.master.title("ADD USER")
        self.master.geometry('300x200')
        self.quitButton = tk.Button(self.master, text = 'Quit', width = 12, command = self.close_windows)
        self.label_username = tk.Label(self.master, text="Enter New Username")
        self.label_password = tk.Label(self.master, text="Enter New Password")
        self.label_password2 = tk.Label(self.master, text="Confirm Password")
        self.entry_username = tk.Entry(self.master)
        self.entry_password = tk.Entry(self.master, show="*")
        self.entry_password2 = tk.Entry(self.master, show="*")
        self.entry_username.focus()

        #Adjusting window and button spacing
        self.label_username.grid(row=0, sticky='e', pady=5)
        self.label_password.grid(row=1, sticky='e', pady=10)
        self.label_password2.grid(row=2, sticky='w', pady=10)
        self.entry_username.grid(row=0, column=1, columnspan = 1,sticky='w')
        self.entry_password.grid(row=1, column=1, columnspan = 1,sticky='w')
        self.entry_password2.grid(row=2, column=1, columnspan = 1,sticky='w')
        self.add_userbtn = tk.Button(self.master, text="Add user",width =12, command=self._add_user_btn_clicked)
        self.add_userbtn.grid(row=3,column=1,pady=10)
        self.quitButton = tk.Button(self.master, text = 'Back', width = 12, command = self.close_windows)
        self.quitButton.grid(row=4,column=1,pady=5)
        self.master.protocol("WM_DELETE_WINDOW", self.on_exit)

    #Method for clean exit 
    def on_exit(self):
        self.master.destroy()

    #Method for clicking add user
    def _add_user_btn_clicked(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        password2 = self.entry_password2.get()
        self.entry_username.delete(0, 'end')
        self.entry_password.delete(0, 'end')
        self.entry_password2.delete(0, 'end')

        #Password verification
        if(password == password2):
            valid = 0
            cursor = db.execute("SELECT user FROM users WHERE (user=?)", (username,))
            row = cursor.fetchone()
            if row:
                valid = 0
                messagebox.showerror("ERROR", "User exists")
            else:
                checker = db.execute("SELECT * FROM sqlite_master WHERE type = 'table' AND name != 'android_metadata' AND name != 'sqlite_sequence';")
                counter = len(checker.fetchall())
                counters = "user"+str(counter+1)
                valid = 1

            if valid == 1:
                try:
                    checker = db.execute("SELECT * FROM sqlite_master WHERE type = 'table' AND name != 'android_metadata' AND name != 'sqlite_sequence';")
                    counter2 = len(checker.fetchall())

                    #Verify there are no errors    
                    if (len(username) < 1 or len(password) < 1):
                        messagebox.showerror("ERROR", "Missing Username and/or Password")
                    elif (counter2 > 10):
                        messagebox.showerror("ERROR", "Maximum allowed user limit reached")
                    else:
                        db.execute("CREATE TABLE "+counters+" (userlog TEXT NOT NULL, "
                            "aoo_lowerRateLimitEntry INTEGER NOT NULL, aoo_upperRateLimitEntry INTEGER NOT NULL, aoo_atrialAmplitudeEntry REAL NOT NULL, aoo_atrialPulseWidthEntry INTEGER NOT NULL, "
                            "voo_lowerRateLimitEntry INTEGER NOT NULL, voo_upperRateLimitEntry INTEGER NOT NULL, voo_ventricularAmplitudeEntry REAL NOT NULL, voo_ventricularPulseWidthEntry INTEGER NOT NULL, "
                            "aai_lowerRateLimitEntry INTEGER NOT NULL, aai_upperRateLimitEntry INTEGER NOT NULL, aai_atrialAmplitudeEntry REAL NOT NULL, aai_atrialPulseWidthEntry INTEGER NOT NULL, aai_atrialSensitivityEntry REAL NOT NULL, aai_ARPEntry INTEGER NOT NULL, aai_PVARPEntry INTEGER NOT NULL, aai_hysteresisEntry INTEGER NOT NULL, aai_rateSmoothingEntry INTEGER NOT NULL, "
                            "vvi_lowerRateLimitEntry INTEGER NOT NULL, vvi_upperRateLimitEntry INTEGER NOT NULL, vvi_ventricularAmplitudeEntry REAL NOT NULL, vvi_ventricularPulseWidthEntry INTEGER NOT NULL, vvi_ventricularSensitivityEntry REAL NOT NULL, vvi_VRPEntry INTEGER NOT NULL, vvi_hysteresisEntry INTEGER NOT NULL, vvi_rateSmoothingEntry INTEGER NOT NULL, "
                            "doo_lowerRateLimitEntry INTEGER NOT NULL, doo_upperRateLimitEntry INTEGER NOT NULL, doo_atrialAmplitudeEntry REAL NOT NULL, doo_atrialPulseWidthEntry INTEGER NOT NULL, doo_ventricularAmplitudeEntry REAL NOT NULL, doo_ventricularPulseWidthEntry INTEGER NOT NULL, doo_fixedAVDelayEntry INTEGER NOT NULL, "
                            "aoor_lowerRateLimitEntry INTEGER NOT NULL, aoor_upperRateLimitEntry INTEGER NOT NULL, aoor_atrialAmplitudeEntry REAL NOT NULL, aoor_atrialPulseWidthEntry INTEGER NOT NULL, aoor_maximumSensorRateEntry INTEGER NOT NULL, aoor_activityThresholdEntry TEXT NOT NULL, aoor_reactionTimeEntry INTEGER NOT NULL, aoor_responseFactorEntry INTEGER NOT NULL, aoor_recoveryTimeEntry INTEGER NOT NULL, "
                            "voor_lowerRateLimitEntry INTEGER NOT NULL, voor_upperRateLimitEntry INTEGER NOT NULL, voor_ventricularAmplitudeEntry REAL NOT NULL, voor_ventricularPulseWidthEntry INTEGER NOT NULL, voor_maximumSensorRateEntry INTEGER NOT NULL, voor_activityThresholdEntry TEXT NOT NULL, voor_reactionTimeEntry INTEGER NOT NULL, voor_responseFactorEntry INTEGER NOT NULL, voor_recoveryTimeEntry INTEGER NOT NULL, "
                            "aair_lowerRateLimitEntry INTEGER NOT NULL, aair_upperRateLimitEntry INTEGER NOT NULL, aair_atriaAmplitudeEntry REAL NOT NULL, aair_atrialPulseWidthEntry INTEGER NOT NULL, aair_atrialSensitivityEntry REAL NOT NULL, aair_ARPEntry INTEGER NOT NULL, aair_PVARPEntry INTEGER NOT NULL, aair_hysteresisEntry INTEGER NOT NULL, aair_rateSmoothingEntry INTEGER NOT NULL, aair_maximumSensorRateEntry INTEGER NOT NULL, aair_activityThresholdEntry TEXT NOT NULL, aair_reactionTimeEntry INTEGER NOT NULL, aair_responseFactorEntry INTEGER NOT NULL, aair_recoveryTimeEntry INTEGER NOT NULL, "
                            "vvir_lowerRateLimitEntry INTEGER NOT NULL, vvir_upperRateLimitEntry INTEGER NOT NULL, vvir_ventricularAmplitudeEntry REAL NOT NULL, vvir_ventricularPulseWidthEntry INTEGER NOT NULL, vvir_ventricularSensitivityEntry REAL NOT NULL, vvir_VRPEntry INTEGER NOT NULL, vvir_hysteresisEntry INTEGER NOT NULL, vvir_rateSmoothingEntry INTEGER NOT NULL, vvir_maximumSensorRateEntry INTEGER NOT NULL, vvir_activityThresholdEntry TEXT NOT NULL, vvir_reactionTimeEntry INTEGER NOT NULL, vvir_responseFactorEntry INTEGER NOT NULL, vvir_recoveryTimeEntry INTEGER NOT NULL, "
                            "door_lowerRateLimitEntry INTEGER NOT NULL, door_upperRateLimitEntry INTEGER NOT NULL, door_atrialAmplitudeEntry REAL NOT NULL, door_atrialPulseWidthEntry INTEGER NOT NULL, door_ventricularAmplitudeEntry REAL NOT NULL, door_ventricularPulseWidthEntry INTEGER NOT NULL, door_maximumSensorRateEntry INTEGER NOT NULL, door_fixedAVDelayEntry INTEGER NOT NULL, door_activityThresholdEntry TEXT NOT NULL, door_reactionTimeEntry INTEGER NOT NULL, door_responseFactorEntry INTEGER NOT NULL, door_recoveryTimeEntry INTEGER NOT NULL)")
                        db.execute("INSERT INTO users VALUES(?, ?, ?)", (username, password, counters))
                        db.execute("INSERT INTO "+counters+" VALUES(?, " #log
                            "?,?,?,?, " #aoo
                            "?,?,?,?, " #voo
                            "?,?,?,?,?,?,?,?,?, " #aai
                            "?,?,?,?,?,?,?,?, " #vvi
                            "?,?,?,?,?,?,?, " #doo
                            "?,?,?,?,?,?,?,?,?, " #aoor
                            "?,?,?,?,?,?,?,?,?, " #voor
                            "?,?,?,?,?,?,?,?,?,?,?,?,?,?, " #aair
                            "?,?,?,?,?,?,?,?,?,?,?,?,?, " #vvir
                            "?,?,?,?,?,?,?,?,?,?,?,?)", #door
                            ("No Mode Set", #log
                            60, 120, 3.5, 0.4, #aoo
                            60, 120, 3.5, 0.4, #voo
                            60, 120, 3.5, 0.4, 0.75, 250, 250, 0, 0, #aai
                            60, 120, 3.5, 0.4, 2.5, 320, 0, 0, #vvi
                            60, 120, 3.5, 0.4, 3.5, 0.4 ,150, #doo
                            60, 120, 3.5, 0.4, 120,"Med",30,8,5, #aoor
                            60, 120, 3.5, 0.4, 120,"Med",30,8,5, #voor
                            60, 120, 3.5, 0.4, 3.3, 250, 250, 0, 0, 120,"Med",30,8,5, #aair
                            60, 120, 3.5, 0.4, 3.3, 320, 0, 0, 120,"Med",30,8,5, #vvir
                            60, 120, 3.5, 0.4, 3.5, 0.4 ,150 ,120,"Med",30,8,5)) #door
                        messagebox.showinfo("SUCCESS", "User Added")
                        self.quitButton.focus()

                except Exception as e:
                    messagebox.showerror("ERROR", "User exists")
                
                db.commit()

        #Passwords don't match
        else:
            messagebox.showerror("ERROR", "Passwords do not match")

    #Method for closing window
    def close_windows(self):
        self.master.destroy()

#Class for main window
class MainWindow:
    def __init__(self, master):
        #General window setup
        self.master = master
        self.master.title(uNAME + "'s DCM")
        self.master.geometry('1920x1080')
        self.master.protocol("WM_DELETE_WINDOW", self.on_exit)
        self.menubar = tk.Menu(self.master)
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.master.config(menu=self.menubar)
        self.frame = tk.Frame(self.master)
        self.content = tk.Entry()
        
        # Tabs created for AOO, VOO, AAI, VVI, and DOO
        # Also AOOR, VOOR, AAIR, VVIR, and DOOR 
        self.tab_parent = ttk.Notebook(self.master)
        self.aoo = ttk.Frame(self.tab_parent)
        self.voo = ttk.Frame(self.tab_parent)
        self.aai = ttk.Frame(self.tab_parent)
        self.vvi = ttk.Frame(self.tab_parent)
        self.doo = ttk.Frame(self.tab_parent)
        self.aoor = ttk.Frame(self.tab_parent)
        self.voor = ttk.Frame(self.tab_parent)
        self.aair = ttk.Frame(self.tab_parent)
        self.vvir = ttk.Frame(self.tab_parent)
        self.door = ttk.Frame(self.tab_parent)
        self.tab_parent.add(self.aoo, text = "AOO")
        self.tab_parent.add(self.voo, text = "VOO")
        self.tab_parent.add(self.aai, text = "AAI")
        self.tab_parent.add(self.vvi, text = "VVI")
        self.tab_parent.add(self.doo, text = "DOO")
        self.tab_parent.add(self.aoor, text = "AOOR")
        self.tab_parent.add(self.voor, text = "VOOR")
        self.tab_parent.add(self.aair, text = "AAIR")
        self.tab_parent.add(self.vvir, text = "VVIR")
        self.tab_parent.add(self.door, text = "DOOR")

        #Position tabs properly
        self.tab_parent.pack(expand = 1, fill='both')

        #Retrieve all relevant data from tables for currentuser
        global currentuser
        cursor = db.execute("SELECT * FROM "+currentuser); row = cursor.fetchall()
        
        #Current Mode
        global userlog
        userlog                           = str(row[0][0])

        #Global Variables setup with current user parameters
        #AOO
        global aoo_lowerRateLimitEntry,aoo_upperRateLimitEntry,aoo_atrialAmplitudeEntry,aoo_atrialPulseWidthEntry 
        aoo_lowerRateLimitEntry           = str(row[0][1])
        aoo_upperRateLimitEntry           = str(row[0][2])
        aoo_atrialAmplitudeEntry          = str(row[0][3])
        aoo_atrialPulseWidthEntry         = str(row[0][4])
        
        #VOO
        global voo_lowerRateLimitEntry,voo_upperRateLimitEntry,voo_ventricularAmplitudeEntry,voo_ventricularPulseWidthEntry
        voo_lowerRateLimitEntry           = str(row[0][5])
        voo_upperRateLimitEntry           = str(row[0][6])
        voo_ventricularAmplitudeEntry     = str(row[0][7])
        voo_ventricularPulseWidthEntry    = str(row[0][8])

        #AAI
        global aai_lowerRateLimitEntry,aai_upperRateLimitEntry,aai_atrialAmplitudeEntry,aai_atrialPulseWidthEntry,aai_atrialSensitivityEntry,aai_ARPEntry,aai_PVARPEntry,aai_hysteresisEntry,aai_rateSmoothingEntry
        aai_lowerRateLimitEntry           = str(row[0][9])
        aai_upperRateLimitEntry           = str(row[0][10])
        aai_atrialAmplitudeEntry          = str(row[0][11])
        aai_atrialPulseWidthEntry         = str(row[0][12])
        aai_atrialSensitivityEntry        = str(row[0][13])
        aai_ARPEntry                      = str(row[0][14])
        aai_PVARPEntry                    = str(row[0][15])
        aai_hysteresisEntry               = str(row[0][16])
        aai_rateSmoothingEntry            = str(row[0][17])

        #VVI
        global vvi_lowerRateLimitEntry,vvi_upperRateLimitEntry,vvi_ventricularAmplitudeEntry,vvi_ventricularPulseWidthEntry,vvi_ventricularSensitivityEntry,vvi_VRPEntry,vvi_hysteresisEntry,vvi_rateSmoothingEntry
        vvi_lowerRateLimitEntry           = str(row[0][18])
        vvi_upperRateLimitEntry           = str(row[0][19])
        vvi_ventricularAmplitudeEntry     = str(row[0][20])
        vvi_ventricularPulseWidthEntry    = str(row[0][21])
        vvi_ventricularSensitivityEntry   = str(row[0][22])
        vvi_VRPEntry                      = str(row[0][23])
        vvi_hysteresisEntry               = str(row[0][24])
        vvi_rateSmoothingEntry            = str(row[0][25])
        
        #DOO
        global doo_lowerRateLimitEntry, doo_upperRateLimitEntry, doo_atrialAmplitudeEntry, doo_atrialPulseWidthEntry, doo_ventricularAmplitudeEntry, doo_ventricularPulseWidthEntry, doo_fixedAVDelayEntry
        doo_lowerRateLimitEntry           = str(row[0][26])
        doo_upperRateLimitEntry           = str(row[0][27])
        doo_atrialAmplitudeEntry          = str(row[0][28])
        doo_atrialPulseWidthEntry         = str(row[0][29])
        doo_ventricularAmplitudeEntry     = str(row[0][30])
        doo_ventricularPulseWidthEntry    = str(row[0][31])
        doo_fixedAVDelayEntry             = str(row[0][32])

        #AOOR
        global aoor_lowerRateLimitEntry, aoor_upperRateLimitEntry, aoor_atrialAmplitudeEntry, aoor_atrialPulseWidthEntry, aoor_maximumSensorRateEntry, aoor_activityThresholdEntry, aoor_reactionTimeEntry, aoor_responseFactorEntry, aoor_recoveryTimeEntry
        aoor_lowerRateLimitEntry          = str(row[0][33])
        aoor_upperRateLimitEntry          = str(row[0][34])
        aoor_atrialAmplitudeEntry         = str(row[0][35])
        aoor_atrialPulseWidthEntry        = str(row[0][36])
        aoor_maximumSensorRateEntry       = str(row[0][37])
        aoor_activityThresholdEntry       = str(row[0][38])
        aoor_reactionTimeEntry            = str(row[0][39])
        aoor_responseFactorEntry          = str(row[0][40])
        aoor_recoveryTimeEntry            = str(row[0][41])

        #VOOR
        global voor_lowerRateLimitEntry, voor_upperRateLimitEntry, voor_ventricularAmplitudeEntry, voor_ventricularPulseWidthEntry, voor_maximumSensorRateEntry, voor_activityThresholdEntry, voor_reactionTimeEntry, voor_responseFactorEntry, voor_recoveryTimeEntry
        voor_lowerRateLimitEntry          = str(row[0][42])
        voor_upperRateLimitEntry          = str(row[0][43])
        voor_ventricularAmplitudeEntry    = str(row[0][44])
        voor_ventricularPulseWidthEntry   = str(row[0][45])
        voor_maximumSensorRateEntry       = str(row[0][46])
        voor_activityThresholdEntry       = str(row[0][47])
        voor_reactionTimeEntry            = str(row[0][48])
        voor_responseFactorEntry          = str(row[0][49])
        voor_recoveryTimeEntry            = str(row[0][50])

        #AAIR
        global aair_lowerRateLimitEntry, aair_upperRateLimitEntry, aair_atrialAmplitudeEntry, aair_atrialPulseWidthEntry, aair_atrialSensitivityEntry, aair_ARPEntry, aair_PVARPEntry, aair_hysteresisEntry, aair_rateSmoothingEntry, aair_maximumSensorRateEntry, aair_activityThresholdEntry, aair_reactionTimeEntry, aair_responseFactorEntry, aair_recoveryTimeEntry
        aair_lowerRateLimitEntry          = str(row[0][51])
        aair_upperRateLimitEntry          = str(row[0][52])
        aair_atrialAmplitudeEntry         = str(row[0][53])
        aair_atrialPulseWidthEntry        = str(row[0][54])
        aair_atrialSensitivityEntry       = str(row[0][55])
        aair_ARPEntry                     = str(row[0][56])
        aair_PVARPEntry                   = str(row[0][57])
        aair_hysteresisEntry              = str(row[0][58])
        aair_rateSmoothingEntry           = str(row[0][59])
        aair_maximumSensorRateEntry       = str(row[0][60])
        aair_activityThresholdEntry       = str(row[0][61])
        aair_reactionTimeEntry            = str(row[0][62])
        aair_responseFactorEntry          = str(row[0][63])
        aair_recoveryTimeEntry            = str(row[0][64])
        
        #VVIR
        global vvir_lowerRateLimitEntry, vvir_upperRateLimitEntry, vvir_ventricularAmplitudeEntry, vvir_ventricularPulseWidthEntry, vvir_ventricularSensitivityEntry, vvir_VRPEntry, vvir_hysteresisEntry, vvir_rateSmoothingEntry, vvir_maximumSensorRateEntry, vvir_activityThresholdEntry, vvir_reactionTimeEntry, vvir_responseFactorEntry, vvir_recoveryTimeEntry
        vvir_lowerRateLimitEntry          = str(row[0][65])
        vvir_upperRateLimitEntry          = str(row[0][66])
        vvir_ventricularAmplitudeEntry    = str(row[0][67])
        vvir_ventricularPulseWidthEntry   = str(row[0][68])
        vvir_ventricularSensitivityEntry  = str(row[0][69])
        vvir_VRPEntry                     = str(row[0][70])
        vvir_hysteresisEntry              = str(row[0][71])
        vvir_rateSmoothingEntry           = str(row[0][72])
        vvir_maximumSensorRateEntry       = str(row[0][73])
        vvir_activityThresholdEntry       = str(row[0][74])
        vvir_reactionTimeEntry            = str(row[0][75])
        vvir_responseFactorEntry          = str(row[0][76])
        vvir_recoveryTimeEntry            = str(row[0][77])

        #DOOR
        global door_lowerRateLimitEntry, door_upperRateLimitEntry, door_atrialAmplitudeEntry, door_atrialPulseWidthEntry, door_ventricularAmplitudeEntry, door_ventricularPulseWidthEntry, door_maximumSensorRateEntry, door_fixedAVDelayEntry, door_activityThresholdEntry, door_reactionTimeEntry, door_responseFactorEntry, door_recoveryTimeEntry
        door_lowerRateLimitEntry          = str(row[0][78])
        door_upperRateLimitEntry          = str(row[0][79])
        door_atrialAmplitudeEntry         = str(row[0][80])
        door_atrialPulseWidthEntry        = str(row[0][81])
        door_ventricularAmplitudeEntry    = str(row[0][82])
        door_ventricularPulseWidthEntry   = str(row[0][83])
        door_maximumSensorRateEntry       = str(row[0][84])
        door_fixedAVDelayEntry            = str(row[0][85])
        door_activityThresholdEntry       = str(row[0][86])
        door_reactionTimeEntry            = str(row[0][87])
        door_responseFactorEntry          = str(row[0][88])
        door_recoveryTimeEntry            = str(row[0][89])

        #AOO BEGIN-----------------------------------------------------------------------------------------------------------------------------
        #Setup labels for inputs
        self.aooLowerRateLimitLabel = tk.Label(self.aoo, text = "Lower Rate Limit")
        self.aooUpperRateLimitLabel = tk.Label(self.aoo, text = "Upper Rate Limit")
        self.aooAtrialAmplitudeLabel = tk.Label(self.aoo, text = "Atrial Amplitude")
        self.aooAtrialPulseWidthLabel = tk.Label(self.aoo, text = "Atrial Pulse Width")
        
        #Spinbox for setup
        self.aooLowerRateLimitEntry = tk.Spinbox(self.aoo,from_=30,to=175,increment=5)
        self.aooUpperRateLimitEntry = tk.Spinbox(self.aoo,from_=50,to=175,increment=5)
        self.aooAtrialAmplitudeEntry = tk.Spinbox(self.aoo,from_=0.0,to=7.0,format="%.1f",increment=0.1)
        self.aooAtrialPulseWidthEntry = tk.Spinbox(self.aoo,from_=0.05,to=1.9,format="%.2f",increment=0.1)

        #Setup buttons
        self.aooLowerRateLimitButton = tk.Button(self.aoo, text = "Set", command= lambda: self.setValue("aooLowerRateLimit"))
        self.aooUpperRateLimitButton = tk.Button(self.aoo, text = "Set", command= lambda: self.setValue("aooUpperRateLimit"))
        self.aooAtrialAmplitudeButton = tk.Button(self.aoo, text = "Set", command= lambda: self.setValue("aooAtrialAmplitude"))
        self.aooAtrialPulseWidthButton = tk.Button(self.aoo, text = "Set", command= lambda: self.setValue("aooAtrialPulseWidth"))
        
        #Setup  labels to display values
        self.aooLowerRateLimitValue = tk.Label(self.aoo, text = "Current Value: " + aoo_lowerRateLimitEntry)
        self.aooUpperRateLimitValue = tk.Label(self.aoo, text = "Current Value: " + aoo_upperRateLimitEntry)
        self.aooAtrialAmplitudeValue = tk.Label(self.aoo, text = "Current Value: " + aoo_atrialAmplitudeEntry)
        self.aooAtrialPulseWidthValue = tk.Label(self.aoo, text = "Current Value: " + aoo_atrialPulseWidthEntry)

        #Adjust positioning
        self.aooLowerRateLimitLabel.grid(row=0, column=0, padx=15, pady=15)
        self.aooLowerRateLimitEntry.grid(row=0, column=1, padx=15, pady=15)
        self.aooLowerRateLimitButton.grid(row=0, column=2, padx=15, pady=15)
        self.aooLowerRateLimitValue.grid(row=0, column=3, padx=15, pady=15)

        self.aooUpperRateLimitLabel.grid(row=1, column=0, padx=15, pady=15)
        self.aooUpperRateLimitEntry.grid(row=1, column=1, padx=15, pady=15)
        self.aooUpperRateLimitButton.grid(row=1, column=2, padx=15, pady=15)
        self.aooUpperRateLimitValue.grid(row=1, column=3, padx=15, pady=15)

        self.aooAtrialAmplitudeLabel.grid(row=2, column=0, padx=15, pady=15)
        self.aooAtrialAmplitudeEntry.grid(row=2, column=1, padx=15, pady=15)
        self.aooAtrialAmplitudeButton.grid(row=2, column=2, padx=15, pady=15)
        self.aooAtrialAmplitudeValue.grid(row=2, column=3, padx=15, pady=15)

        self.aooAtrialPulseWidthLabel.grid(row=3, column=0, padx=15, pady=15)
        self.aooAtrialPulseWidthEntry.grid(row=3, column=1, padx=15, pady=15)
        self.aooAtrialPulseWidthButton.grid(row=3, column=2, padx=15, pady=15)
        self.aooAtrialPulseWidthValue.grid(row=3, column=3, padx=15, pady=15)
        #AOO END-------------------------------------------------------------------------------------------------------------------------------

        #VOO BEGIN----------------------------------------------------------------------------------------------------------------------------- 
        #Setup labels for inputs
        self.vooLowerRateLimitLabel = tk.Label(self.voo, text = "Lower Rate Limit")
        self.vooUpperRateLimitLabel = tk.Label(self.voo, text = "Upper Rate Limit ")
        self.vooVentricularAmplitudeLabel = tk.Label(self.voo, text = "Ventricular Amplitude")
        self.vooVentricularPulseWidthLabel = tk.Label(self.voo, text = "Ventricular Pulse Width")
        
        #Spinbox for setup
        self.vooLowerRateLimitEntry = tk.Spinbox(self.voo,from_=30,to=175,increment=5)
        self.vooUpperRateLimitEntry = tk.Spinbox(self.voo,from_=50,to=175,increment=5)
        self.vooVentricularAmplitudeEntry = tk.Spinbox(self.voo,from_=0.0,to=7.0,format="%.1f",increment=0.1)
        self.vooVentricularPulseWidthEntry = tk.Spinbox(self.voo,from_=0.05,to=1.9,format="%.2f",increment=0.1)
        
        #Setup buttons
        self.vooLowerRateLimitButton = tk.Button(self.voo, text = "Set", command= lambda: self.setValue("vooLowerRateLimit"))
        self.vooUpperRateLimitButton = tk.Button(self.voo, text = "Set", command= lambda: self.setValue("vooUpperRateLimit"))
        self.vooVentricularAmplitudeButton = tk.Button(self.voo, text = "Set", command= lambda: self.setValue("vooVentricularAmplitude"))
        self.vooVentricularPulseWidthButton = tk.Button(self.voo, text = "Set", command= lambda: self.setValue("vooVentricularPulseWidth"))
        
        #Setup  labels to display values
        self.vooLowerRateLimitValue = tk.Label(self.voo, text = "Current Value: "+ voo_lowerRateLimitEntry)
        self.vooUpperRateLimitValue = tk.Label(self.voo, text = "Current Value: "+ voo_upperRateLimitEntry)
        self.vooVentricularAmplitudeValue = tk.Label(self.voo, text = "Current Value: "+ voo_ventricularAmplitudeEntry)
        self.vooVentricularPulseWidthValue = tk.Label(self.voo, text = "Current Value: "+ voo_ventricularPulseWidthEntry)

        #Adjust positioning
        self.vooLowerRateLimitLabel.grid(row=0, column=0, padx=15, pady=15)
        self.vooLowerRateLimitEntry.grid(row=0, column=1, padx=15, pady=15)
        self.vooLowerRateLimitButton.grid(row=0, column=2, padx=15, pady=15)
        self.vooLowerRateLimitValue.grid(row=0, column=3, padx=15, pady=15)

        self.vooUpperRateLimitLabel.grid(row=1, column=0, padx=15, pady=15)
        self.vooUpperRateLimitEntry.grid(row=1, column=1, padx=15, pady=15)
        self.vooUpperRateLimitButton.grid(row=1, column=2, padx=15, pady=15)
        self.vooUpperRateLimitValue.grid(row=1, column=3, padx=15, pady=15)

        self.vooVentricularAmplitudeLabel.grid(row=2, column=0, padx=15, pady=15)
        self.vooVentricularAmplitudeEntry.grid(row=2, column=1, padx=15, pady=15)
        self.vooVentricularAmplitudeButton.grid(row=2, column=2, padx=15, pady=15)
        self.vooVentricularAmplitudeValue.grid(row=2, column=3, padx=15, pady=15)

        self.vooVentricularPulseWidthLabel.grid(row=3, column=0, padx=15, pady=15)
        self.vooVentricularPulseWidthEntry.grid(row=3, column=1, padx=15, pady=15)
        self.vooVentricularPulseWidthButton.grid(row=3, column=2, padx=15, pady=15)
        self.vooVentricularPulseWidthValue.grid(row=3, column=3, padx=15, pady=15)
        #VOO END-------------------------------------------------------------------------------------------------------------------------------

        #AAI BEGIN-----------------------------------------------------------------------------------------------------------------------------
        #Setup labels for inputs
        self.aaiLowerRateLimitLabel = tk.Label(self.aai, text = "Lower Rate Limit")
        self.aaiUpperRateLimitLabel = tk.Label(self.aai, text = "Upper Rate Limit ")
        self.aaiAtrialAmplitudeLabel = tk.Label(self.aai, text = "Atrial Amplitude")
        self.aaiAtrialPulseWidthLabel = tk.Label(self.aai, text = "Atrial Pulse Width")
        self.aaiAtrialSensitivityLabel = tk.Label(self.aai, text = "Atrial Sensitivity")
        self.aaiARPLabel = tk.Label(self.aai, text = "ARP")
        self.aaiPVARPLabel = tk.Label(self.aai, text = "APVARP")
        self.aaiHysteresisLabel = tk.Label(self.aai, text = "Hysteresis")
        self.aaiRateSmoothingLabel = tk.Label(self.aai, text = "Rate Smoothing")

        #Spinbox for setup
        self.aaiLowerRateLimitEntry = tk.Spinbox(self.aai,from_=30,to=175,increment=5)
        self.aaiUpperRateLimitEntry = tk.Spinbox(self.aai,from_=50,to=175,increment=5)
        self.aaiAtrialAmplitudeEntry = tk.Spinbox(self.aai,from_=0.0,to=7.0,format="%.1f",increment=0.1)
        self.aaiAtrialPulseWidthEntry = tk.Spinbox(self.aai,from_=0.05,to=1.9,format="%.2f",increment=0.1)
        self.aaiAtrialSensitivityEntry = tk.Spinbox(self.aai,from_=0.25,to=10.0,format="%.2f",increment=0.25)
        self.aaiARPEntry = tk.Spinbox(self.aai,from_=150,to=500,increment=10)
        self.aaiPVARPEntry = tk.Spinbox(self.aai,from_=150,to=500,increment=10)
        self.aaiHysteresisEntry = tk.Spinbox(self.aai,from_=0,to=25,increment=5)
        self.aaiRateSmoothingEntry = tk.Spinbox(self.aai,from_=0,to=25,increment=3)

        #Setup buttons
        self.aaiLowerRateLimitButton = tk.Button(self.aai, text = "Set", command= lambda: self.setValue("aaiLowerRateLimit"))
        self.aaiUpperRateLimitButton = tk.Button(self.aai, text = "Set", command= lambda: self.setValue("aaiUpperRateLimit"))
        self.aaiAtrialAmplitudeButton = tk.Button(self.aai, text = "Set", command= lambda: self.setValue("aaiAtrialAmplitude"))
        self.aaiAtrialPulseWidthButton = tk.Button(self.aai, text = "Set", command= lambda: self.setValue("aaiAtrialPulseWidth"))
        self.aaiAtrialSensitivityButton = tk.Button(self.aai, text = "Set", command= lambda: self.setValue("aaiAtrialSensitivity"))
        self.aaiARPButton = tk.Button(self.aai, text = "Set", command= lambda: self.setValue("aaiARP"))
        self.aaiPVARPButton = tk.Button(self.aai, text = "Set", command= lambda: self.setValue("aaiPVARP"))
        self.aaiHysteresisButton = tk.Button(self.aai, text = "Set", command= lambda: self.setValue("aaiHysteresis"))
        self.aaiRateSmoothingButton = tk.Button(self.aai, text = "Set", command= lambda: self.setValue("aaiRateSmoothing"))
        
        #Setup  labels to display values
        self.aaiLowerRateLimitValue = tk.Label(self.aai, text = "Current Value: "+ aai_lowerRateLimitEntry)
        self.aaiUpperRateLimitValue = tk.Label(self.aai, text = "Current Value: "+ aai_upperRateLimitEntry)
        self.aaiAtrialAmplitudeValue = tk.Label(self.aai, text = "Current Value: "+ aai_atrialAmplitudeEntry)
        self.aaiAtrialPulseWidthValue = tk.Label(self.aai, text = "Current Value: "+ aai_atrialPulseWidthEntry)
        self.aaiAtrialSensitivityValue = tk.Label(self.aai, text = "Current Value: "+ aai_atrialSensitivityEntry)
        self.aaiARPValue = tk.Label(self.aai, text = "Current Value: "+ aai_ARPEntry)
        self.aaiPVARPValue = tk.Label(self.aai, text = "Current Value: "+ aai_PVARPEntry)
        self.aaiHysteresisValue = tk.Label(self.aai, text = "Current Value: "+ aai_hysteresisEntry)
        self.aaiRateSmoothingValue = tk.Label(self.aai, text = "Current Value: "+ aai_rateSmoothingEntry)
        
        #Adjust positioning
        self.aaiLowerRateLimitLabel.grid(row=0, column=0, padx=15, pady=15)
        self.aaiLowerRateLimitEntry.grid(row=0, column=1, padx=15, pady=15)
        self.aaiLowerRateLimitButton.grid(row=0, column=2, padx=15, pady=15)
        self.aaiLowerRateLimitValue.grid(row=0, column=3, padx=15, pady=15)
        
        self.aaiUpperRateLimitLabel.grid(row=1, column=0, padx=15, pady=15)
        self.aaiUpperRateLimitEntry.grid(row=1, column=1, padx=15, pady=15)
        self.aaiUpperRateLimitButton.grid(row=1, column=2, padx=15, pady=15)
        self.aaiUpperRateLimitValue.grid(row=1, column=3, padx=15, pady=15)       

        self.aaiAtrialAmplitudeLabel.grid(row=2, column=0, padx=15, pady=15)
        self.aaiAtrialAmplitudeEntry.grid(row=2, column=1, padx=15, pady=15)
        self.aaiAtrialAmplitudeButton.grid(row=2, column=2, padx=15, pady=15)
        self.aaiAtrialAmplitudeValue.grid(row=2, column=3, padx=15, pady=15)
        
        self.aaiAtrialPulseWidthLabel.grid(row=3, column=0, padx=15, pady=15)
        self.aaiAtrialPulseWidthEntry.grid(row=3, column=1, padx=15, pady=15)
        self.aaiAtrialPulseWidthButton.grid(row=3, column=2, padx=15, pady=15)
        self.aaiAtrialPulseWidthValue.grid(row=3, column=3, padx=15, pady=15)
        
        self.aaiAtrialSensitivityLabel.grid(row=4, column=0, padx=15, pady=15)
        self.aaiAtrialSensitivityEntry.grid(row=4, column=1, padx=15, pady=15)
        self.aaiAtrialSensitivityButton.grid(row=4, column=2, padx=15, pady=15)
        self.aaiAtrialSensitivityValue.grid(row=4, column=3, padx=15, pady=15)       

        self.aaiARPLabel.grid(row=5, column=0, padx=15, pady=15)
        self.aaiARPEntry.grid(row=5, column=1, padx=15, pady=15)
        self.aaiARPButton.grid(row=5, column=2, padx=15, pady=15)
        self.aaiARPValue.grid(row=5, column=3, padx=15, pady=15)
        
        self.aaiPVARPLabel.grid(row=6, column=0, padx=15, pady=15)
        self.aaiPVARPEntry.grid(row=6, column=1, padx=15, pady=15)
        self.aaiPVARPButton.grid(row=6, column=2, padx=15, pady=15)
        self.aaiPVARPValue.grid(row=6, column=3, padx=15, pady=15)
        
        self.aaiHysteresisLabel.grid(row=7, column=0, padx=15, pady=15)
        self.aaiHysteresisEntry.grid(row=7, column=1, padx=15, pady=15)
        self.aaiHysteresisButton.grid(row=7, column=2, padx=15, pady=15)
        self.aaiHysteresisValue.grid(row=7, column=3, padx=15, pady=15)
        
        self.aaiRateSmoothingLabel.grid(row=8, column=0, padx=15, pady=15)
        self.aaiRateSmoothingEntry.grid(row=8, column=1, padx=15, pady=15)
        self.aaiRateSmoothingButton.grid(row=8, column=2, padx=15, pady=15)
        self.aaiRateSmoothingValue.grid(row=8, column=3, padx=15, pady=15)
        #AAI END-------------------------------------------------------------------------------------------------------------------------------

        #VVI BEGIN-----------------------------------------------------------------------------------------------------------------------------
        #Setup labels for inputs
        self.vviLowerRateLimitLabel = tk.Label(self.vvi, text = "Lower Rate Limit")
        self.vviUpperRateLimitLabel = tk.Label(self.vvi, text = "Upper Rate Limit ")
        self.vviVentricularAmplitudeLabel = tk.Label(self.vvi, text = "Ventricular Amplitude")
        self.vviVentricularPulseWidthLabel = tk.Label(self.vvi, text = "Ventricular Pulse Width")
        self.vviVentricularSensitivityLabel = tk.Label(self.vvi, text = "Ventricular Sensitivity")
        self.vviVRPLabel = tk.Label(self.vvi, text = "VRP")
        self.vviHysteresisLabel = tk.Label(self.vvi, text = "Hysteresis")
        self.vviRateSmoothingLabel = tk.Label(self.vvi, text = "Rate Smoothing")

        #Spinbox for setup
        self.vviLowerRateLimitEntry = tk.Spinbox(self.vvi,from_=30,to=175,increment=5)
        self.vviUpperRateLimitEntry = tk.Spinbox(self.vvi,from_=50,to=175,increment=5)
        self.vviVentricularAmplitudeEntry = tk.Spinbox(self.vvi,from_=0.0,to=7.0,format="%.1f",increment=0.1)
        self.vviVentricularPulseWidthEntry = tk.Spinbox(self.vvi,from_=0.05,to=1.9,format="%.2f",increment=0.1)
        self.vviVentricularSensitivityEntry = tk.Spinbox(self.vvi,from_=0.25,to=10.0,format="%.2f",increment=0.25)
        self.vviVRPEntry = tk.Spinbox(self.vvi,from_=150,to=500,increment=10)
        self.vviHysteresisEntry = tk.Spinbox(self.vvi,from_=0,to=25,increment=5)
        self.vviRateSmoothingEntry = tk.Spinbox(self.vvi,from_=0,to=25,increment=3)
        
        #Setup buttons
        self.vviLowerRateLimitButton = tk.Button(self.vvi, text = "Set", command= lambda: self.setValue("vviLowerRateLimit"))
        self.vviUpperRateLimitButton = tk.Button(self.vvi, text = "Set", command= lambda: self.setValue("vviUpperRateLimit"))
        self.vviVentricularAmplitudeButton = tk.Button(self.vvi, text = "Set", command= lambda: self.setValue("vviVentricularAmplitude"))
        self.vviVentricularPulseWidthButton = tk.Button(self.vvi, text = "Set", command= lambda: self.setValue("vviVentricularPulseWidth"))
        self.vviVentricularSensitivityButton = tk.Button(self.vvi, text = "Set", command= lambda: self.setValue("vviVentricularSensitivity"))
        self.vviVRPButton = tk.Button(self.vvi, text = "Set", command= lambda: self.setValue("vviVRP"))
        self.vviHysteresisButton = tk.Button(self.vvi, text = "Set", command= lambda: self.setValue("vviHysteresis"))
        self.vviRateSmoothingButton = tk.Button(self.vvi, text = "Set", command= lambda: self.setValue("vviRateSmoothing"))
        
        #Setup  labels to display values
        self.vviLowerRateLimitValue = tk.Label(self.vvi, text = "Current Value: "+ vvi_lowerRateLimitEntry)
        self.vviUpperRateLimitValue = tk.Label(self.vvi, text = "Current Value: "+ vvi_upperRateLimitEntry)
        self.vviVentricularAmplitudeValue = tk.Label(self.vvi, text = "Current Value: "+ vvi_ventricularAmplitudeEntry)
        self.vviVentricularPulseWidthValue = tk.Label(self.vvi, text = "Current Value: "+ vvi_ventricularPulseWidthEntry)
        self.vviVentricularSensitivityValue = tk.Label(self.vvi, text = "Current Value: "+ vvi_ventricularSensitivityEntry)
        self.vviVRPValue = tk.Label(self.vvi, text = "Current Value: "+ vvi_VRPEntry)
        self.vviHysteresisValue = tk.Label(self.vvi, text = "Current Value: "+ vvi_hysteresisEntry)
        self.vviRateSmoothingValue = tk.Label(self.vvi, text = "Current Value: "+ vvi_rateSmoothingEntry)

        #Adjust positioning
        self.vviLowerRateLimitLabel.grid(row=0, column=0, padx=15, pady=15)
        self.vviLowerRateLimitEntry.grid(row=0, column=1, padx=15, pady=15)
        self.vviLowerRateLimitButton.grid(row=0, column=2, padx=15, pady=15)
        self.vviLowerRateLimitValue.grid(row=0, column=3, padx=15, pady=15)
        
        self.vviUpperRateLimitLabel.grid(row=1, column=0, padx=15, pady=15)
        self.vviUpperRateLimitEntry.grid(row=1, column=1, padx=15, pady=15)
        self.vviUpperRateLimitButton.grid(row=1, column=2, padx=15, pady=15)
        self.vviUpperRateLimitValue.grid(row=1, column=3, padx=15, pady=15)
        
        self.vviVentricularAmplitudeLabel.grid(row=2, column=0, padx=15, pady=15)
        self.vviVentricularAmplitudeEntry.grid(row=2, column=1, padx=15, pady=15)
        self.vviVentricularAmplitudeButton.grid(row=2, column=2, padx=15, pady=15)
        self.vviVentricularAmplitudeValue.grid(row=2, column=3, padx=15, pady=15)
        
        self.vviVentricularPulseWidthLabel.grid(row=3, column=0, padx=15, pady=15)
        self.vviVentricularPulseWidthEntry.grid(row=3, column=1, padx=15, pady=15)
        self.vviVentricularPulseWidthButton.grid(row=3, column=2, padx=15, pady=15)
        self.vviVentricularPulseWidthValue.grid(row=3, column=3, padx=15, pady=15)
        
        self.vviVentricularSensitivityLabel.grid(row=4, column=0, padx=15, pady=15)
        self.vviVentricularSensitivityEntry.grid(row=4, column=1, padx=15, pady=15)
        self.vviVentricularSensitivityButton.grid(row=4, column=2, padx=15, pady=15)
        self.vviVentricularSensitivityValue.grid(row=4, column=3, padx=15, pady=15)
        
        self.vviVRPLabel.grid(row=5, column=0, padx=15, pady=15)
        self.vviVRPEntry.grid(row=5, column=1, padx=15, pady=15)
        self.vviVRPButton.grid(row=5, column=2, padx=15, pady=15)
        self.vviVRPValue.grid(row=5, column=3, padx=15, pady=15)
        
        self.vviHysteresisLabel.grid(row=6, column=0, padx=15, pady=15)
        self.vviHysteresisEntry.grid(row=6, column=1, padx=15, pady=15)
        self.vviHysteresisButton.grid(row=6, column=2, padx=15, pady=15)
        self.vviHysteresisValue.grid(row=6, column=3, padx=15, pady=15)
        
        self.vviRateSmoothingLabel.grid(row=7, column=0, padx=15, pady=15)
        self.vviRateSmoothingEntry.grid(row=7, column=1, padx=15, pady=15)
        self.vviRateSmoothingButton.grid(row=7, column=2, padx=15, pady=15)
        self.vviRateSmoothingValue.grid(row=7, column=3, padx=15, pady=15)   
        #VVI END-------------------------------------------------------------------------------------------------------------------------------
        
        #DOO BEGIN-----------------------------------------------------------------------------------------------------------------------------
        #Setup labels for inputs
        self.dooLowerRateLimitLabel = tk.Label(self.doo, text = "Lower Rate Limit")
        self.dooUpperRateLimitLabel = tk.Label(self.doo, text = "Upper Rate Limit")
        self.dooAtrialAmplitudeLabel = tk.Label(self.doo, text = "Atrial Amplitude")
        self.dooAtrialPulseWidthLabel = tk.Label(self.doo, text = "Atrial Pulse Width")
        self.dooVentricularAmplitudeLabel = tk.Label(self.doo, text = "Ventricular Amplitude")
        self.dooVentricularPulseWidthLabel = tk.Label(self.doo, text = "Ventricular Pulse Width")
        self.dooFixedAVDelayLabel = tk.Label(self.doo, text = "Fixed AV Delay")

        #Spinbox for setup
        self.dooLowerRateLimitEntry = tk.Spinbox(self.doo,from_=30,to=175,increment=5)
        self.dooUpperRateLimitEntry = tk.Spinbox(self.doo,from_=50,to=175,increment=5)
        self.dooAtrialAmplitudeEntry = tk.Spinbox(self.doo,from_=0.0,to=7.0,format="%.1f",increment=0.1)
        self.dooAtrialPulseWidthEntry = tk.Spinbox(self.doo,from_=0.05,to=1.9,format="%.2f",increment=0.1)
        self.dooVentricularAmplitudeEntry = tk.Spinbox(self.doo,from_=0.0,to=7.0,format="%.1f",increment=0.1)
        self.dooVentricularPulseWidthEntry = tk.Spinbox(self.doo,from_=0.05,to=1.9,format="%.2f",increment=0.1)
        self.dooFixedAVDelayEntry = tk.Spinbox(self.doo,from_=70,to=300,increment=10)

        #Setup buttons
        self.dooLowerRateLimitButton = tk.Button(self.doo, text = "Set", command= lambda: self.setValue("dooLowerRateLimit"))
        self.dooUpperRateLimitButton = tk.Button(self.doo, text = "Set", command= lambda: self.setValue("dooUpperRateLimit"))
        self.dooAtrialAmplitudeButton = tk.Button(self.doo, text = "Set", command= lambda: self.setValue("dooAtrialAmplitude"))
        self.dooAtrialPulseWidthButton = tk.Button(self.doo, text = "Set", command= lambda: self.setValue("dooAtrialPulseWidth"))
        self.dooVentricularAmplitudeButton = tk.Button(self.doo, text = "Set", command= lambda: self.setValue("dooVentricularAmplitude"))
        self.dooVentricularPulseWidthButton = tk.Button(self.doo, text = "Set", command= lambda: self.setValue("dooVentricularPulseWidth"))
        self.dooFixedAVDelayButton = tk.Button(self.doo, text = "Set", command= lambda: self.setValue("dooFixedAVDelay"))

        #Setup labels to display values
        self.dooLowerRateLimitValue = tk.Label(self.doo, text = "Current Value: " + doo_lowerRateLimitEntry)
        self.dooUpperRateLimitValue = tk.Label(self.doo, text = "Current Value: " + doo_upperRateLimitEntry)
        self.dooAtrialAmplitudeValue = tk.Label(self.doo, text = "Current Value: " + doo_atrialAmplitudeEntry)
        self.dooAtrialPulseWidthValue = tk.Label(self.doo, text = "Current Value: " + doo_atrialPulseWidthEntry)
        self.dooVentricularAmplitudeValue = tk.Label(self.doo, text = "Current Value: "+ doo_ventricularAmplitudeEntry)
        self.dooVentricularPulseWidthValue = tk.Label(self.doo, text = "Current Value: "+ doo_ventricularPulseWidthEntry)
        self.dooFixedAVDelayValue = tk.Label(self.doo, text = "Current Value: "+ doo_fixedAVDelayEntry)

        #Adjust positioning
        self.dooLowerRateLimitLabel.grid(row=0, column=0, padx=15, pady=15)
        self.dooLowerRateLimitEntry.grid(row=0, column=1, padx=15, pady=15)
        self.dooLowerRateLimitButton.grid(row=0, column=2, padx=15, pady=15)
        self.dooLowerRateLimitValue.grid(row=0, column=3, padx=15, pady=15)

        self.dooUpperRateLimitLabel.grid(row=1, column=0, padx=15, pady=15)
        self.dooUpperRateLimitEntry.grid(row=1, column=1, padx=15, pady=15)
        self.dooUpperRateLimitButton.grid(row=1, column=2, padx=15, pady=15)
        self.dooUpperRateLimitValue.grid(row=1, column=3, padx=15, pady=15)

        self.dooAtrialAmplitudeLabel.grid(row=2, column=0, padx=15, pady=15)
        self.dooAtrialAmplitudeEntry.grid(row=2, column=1, padx=15, pady=15)
        self.dooAtrialAmplitudeButton.grid(row=2, column=2, padx=15, pady=15)
        self.dooAtrialAmplitudeValue.grid(row=2, column=3, padx=15, pady=15)

        self.dooAtrialPulseWidthLabel.grid(row=3, column=0, padx=15, pady=15)
        self.dooAtrialPulseWidthEntry.grid(row=3, column=1, padx=15, pady=15)
        self.dooAtrialPulseWidthButton.grid(row=3, column=2, padx=15, pady=15)
        self.dooAtrialPulseWidthValue.grid(row=3, column=3, padx=15, pady=15)

        self.dooVentricularAmplitudeLabel.grid(row=4, column=0, padx=15, pady=15)
        self.dooVentricularAmplitudeEntry.grid(row=4, column=1, padx=15, pady=15)
        self.dooVentricularAmplitudeButton.grid(row=4, column=2, padx=15, pady=15)
        self.dooVentricularAmplitudeValue.grid(row=4, column=3, padx=15, pady=15)
        
        self.dooVentricularPulseWidthLabel.grid(row=5, column=0, padx=15, pady=15)
        self.dooVentricularPulseWidthEntry.grid(row=5, column=1, padx=15, pady=15)
        self.dooVentricularPulseWidthButton.grid(row=5, column=2, padx=15, pady=15)
        self.dooVentricularPulseWidthValue.grid(row=5, column=3, padx=15, pady=15)

        self.dooFixedAVDelayLabel.grid(row=6, column=0, padx=15, pady=15)
        self.dooFixedAVDelayEntry.grid(row=6, column=1, padx=15, pady=15)
        self.dooFixedAVDelayButton.grid(row=6, column=2, padx=15, pady=15)
        self.dooFixedAVDelayValue.grid(row=6, column=3, padx=15, pady=15)
        #DOO END-------------------------------------------------------------------------------------------------------------------------------
        
        #AOOR BEGIN----------------------------------------------------------------------------------------------------------------------------
        #Setup labels for inputs
        self.aoorLowerRateLimitLabel = tk.Label(self.aoor, text = "Lower Rate Limit")
        self.aoorUpperRateLimitLabel = tk.Label(self.aoor, text = "Upper Rate Limit")
        self.aoorAtrialAmplitudeLabel = tk.Label(self.aoor, text = "Atrial Amplitude")
        self.aoorAtrialPulseWidthLabel = tk.Label(self.aoor, text = "Atrial Pulse Width")
        self.aoorMaximumSensorRateLabel = tk.Label(self.aoor, text = "Maximum Sensor Rate")
        self.aoorActivityThresholdLabel = tk.Label(self.aoor, text = "Activity Threshold")
        self.aoorReactionTimeLabel = tk.Label(self.aoor, text = "Reaction Time")
        self.aoorResponseFactorLabel = tk.Label(self.aoor, text = "Response Factor")
        self.aoorRecoveryTimeLabel = tk.Label(self.aoor, text = "Recovery Time")

        #Spinbox for setup
        self.aoorLowerRateLimitEntry = tk.Spinbox(self.aoor,from_=30,to=175,increment=5)
        self.aoorUpperRateLimitEntry = tk.Spinbox(self.aoor,from_=50,to=175,increment=5)
        self.aoorAtrialAmplitudeEntry = tk.Spinbox(self.aoor,from_=0.0,to=7.0,format="%.1f",increment=0.1)
        self.aoorAtrialPulseWidthEntry = tk.Spinbox(self.aoor,from_=0.05,to=1.9,format="%.2f",increment=0.1)
        self.aoorMaximumSensorRateEntry = tk.Spinbox(self.aoor,from_=50,to=175,increment=5)
        self.aoorActivityThresholdEntry = ttk.Combobox(self.aoor)
        self.aoorActivityThresholdEntry['values']= ("V-Low", "Low", "Med-Low", "Med", "Med-High", "High","V-High")
        self.aoorActivityThresholdEntry.current(3)
        self.aoorReactionTimeEntry = tk.Spinbox(self.aoor,from_=10,to=50,increment=10)
        self.aoorResponseFactorEntry = tk.Spinbox(self.aoor,from_=1,to=16,increment=1)
        self.aoorRecoveryTimeEntry = tk.Spinbox(self.aoor,from_=2,to=16,increment=1)

        #Setup buttons
        self.aoorLowerRateLimitButton = tk.Button(self.aoor, text = "Set", command= lambda: self.setValue("aoorLowerRateLimit"))
        self.aoorUpperRateLimitButton = tk.Button(self.aoor, text = "Set", command= lambda: self.setValue("aoorUpperRateLimit"))
        self.aoorAtrialAmplitudeButton = tk.Button(self.aoor, text = "Set", command= lambda: self.setValue("aoorAtrialAmplitude"))
        self.aoorAtrialPulseWidthButton = tk.Button(self.aoor, text = "Set", command= lambda: self.setValue("aoorAtrialPulseWidth"))
        self.aoorMaximumSensorRateButton = tk.Button(self.aoor, text = "Set", command= lambda: self.setValue("aoorMaximumSensorRate"))
        self.aoorActivityThresholdButton = tk.Button(self.aoor, text = "Set", command= lambda: self.setValue("aoorActivityThreshold"))
        self.aoorReactionTimeButton = tk.Button(self.aoor, text = "Set", command= lambda: self.setValue("aoorReactionTime"))
        self.aoorResponseFactorButton = tk.Button(self.aoor, text = "Set", command= lambda: self.setValue("aoorResponseFactor"))
        self.aoorRecoveryTimeButton = tk.Button(self.aoor, text = "Set", command= lambda: self.setValue("aoorRecoveryTime"))

        #Setup  labels to display values
        self.aoorLowerRateLimitValue = tk.Label(self.aoor, text = "Current Value: " + aoor_lowerRateLimitEntry)
        self.aoorUpperRateLimitValue = tk.Label(self.aoor, text = "Current Value: " + aoor_upperRateLimitEntry)
        self.aoorAtrialAmplitudeValue = tk.Label(self.aoor, text = "Current Value: " + aoor_atrialAmplitudeEntry)
        self.aoorAtrialPulseWidthValue = tk.Label(self.aoor, text = "Current Value: " + aoor_atrialPulseWidthEntry)
        self.aoorMaximumSensorRateValue = tk.Label(self.aoor, text = "Current Value: " + aoor_maximumSensorRateEntry)
        self.aoorActivityThresholdValue = tk.Label(self.aoor, text = "Current Value: " + aoor_activityThresholdEntry)
        self.aoorReactionTimeValue = tk.Label(self.aoor, text = "Current Value: " + aoor_reactionTimeEntry)
        self.aoorResponseFactorValue = tk.Label(self.aoor, text = "Current Value: " + aoor_responseFactorEntry)
        self.aoorRecoveryTimeValue = tk.Label(self.aoor, text = "Current Value: " + aoor_recoveryTimeEntry)

        #Adjust positioning
        self.aoorLowerRateLimitLabel.grid(row=0, column=0, padx=15, pady=15)
        self.aoorLowerRateLimitEntry.grid(row=0, column=1, padx=15, pady=15)
        self.aoorLowerRateLimitButton.grid(row=0, column=2, padx=15, pady=15)
        self.aoorLowerRateLimitValue.grid(row=0, column=3, padx=15, pady=15)

        self.aoorUpperRateLimitLabel.grid(row=1, column=0, padx=15, pady=15)
        self.aoorUpperRateLimitEntry.grid(row=1, column=1, padx=15, pady=15)
        self.aoorUpperRateLimitButton.grid(row=1, column=2, padx=15, pady=15)
        self.aoorUpperRateLimitValue.grid(row=1, column=3, padx=15, pady=15)

        self.aoorAtrialAmplitudeLabel.grid(row=2, column=0, padx=15, pady=15)
        self.aoorAtrialAmplitudeEntry.grid(row=2, column=1, padx=15, pady=15)
        self.aoorAtrialAmplitudeButton.grid(row=2, column=2, padx=15, pady=15)
        self.aoorAtrialAmplitudeValue.grid(row=2, column=3, padx=15, pady=15)

        self.aoorAtrialPulseWidthLabel.grid(row=3, column=0, padx=15, pady=15)
        self.aoorAtrialPulseWidthEntry.grid(row=3, column=1, padx=15, pady=15)
        self.aoorAtrialPulseWidthButton.grid(row=3, column=2, padx=15, pady=15)
        self.aoorAtrialPulseWidthValue.grid(row=3, column=3, padx=15, pady=15)
        
        self.aoorMaximumSensorRateLabel.grid(row=0, column=5, padx=15, pady=15)
        self.aoorMaximumSensorRateEntry.grid(row=0, column=6, padx=15, pady=15)
        self.aoorMaximumSensorRateButton.grid(row=0, column=7, padx=15, pady=15)
        self.aoorMaximumSensorRateValue.grid(row=0, column=8, padx=15, pady=15)

        self.aoorActivityThresholdLabel.grid(row=1, column=5, padx=15, pady=15)
        self.aoorActivityThresholdEntry.grid(row=1, column=6, padx=15, pady=15)
        self.aoorActivityThresholdButton.grid(row=1, column=7, padx=15, pady=15)
        self.aoorActivityThresholdValue.grid(row=1, column=8, padx=15, pady=15)

        self.aoorReactionTimeLabel.grid(row=2, column=5, padx=15, pady=15)
        self.aoorReactionTimeEntry.grid(row=2, column=6, padx=15, pady=15)
        self.aoorReactionTimeButton.grid(row=2, column=7, padx=15, pady=15)
        self.aoorReactionTimeValue.grid(row=2, column=8, padx=15, pady=15)

        self.aoorResponseFactorLabel.grid(row=3, column=5, padx=15, pady=15)
        self.aoorResponseFactorEntry.grid(row=3, column=6, padx=15, pady=15)
        self.aoorResponseFactorButton.grid(row=3, column=7, padx=15, pady=15)
        self.aoorResponseFactorValue.grid(row=3, column=8, padx=15, pady=15)

        self.aoorRecoveryTimeLabel.grid(row=4, column=5, padx=15, pady=15)
        self.aoorRecoveryTimeEntry.grid(row=4, column=6, padx=15, pady=15)
        self.aoorRecoveryTimeButton.grid(row=4, column=7, padx=15, pady=15)
        self.aoorRecoveryTimeValue.grid(row=4, column=8, padx=15, pady=15)
        #AOOR END-------------------------------------------------------------------------------------------------------------------------------

        #VOOR BEGIN----------------------------------------------------------------------------------------------------------------------------- 
        #Setup labels for inputs
        self.voorLowerRateLimitLabel = tk.Label(self.voor, text = "Lower Rate Limit")
        self.voorUpperRateLimitLabel = tk.Label(self.voor, text = "Upper Rate Limit")
        self.voorVentricularAmplitudeLabel = tk.Label(self.voor, text = "Ventricular Amplitude")
        self.voorVentricularPulseWidthLabel = tk.Label(self.voor, text = "Ventricular Pulse Width")
        self.voorMaximumSensorRateLabel = tk.Label(self.voor, text = "Maximum Sensor Rate")
        self.voorActivityThresholdLabel = tk.Label(self.voor, text = "Activity Threshold")
        self.voorReactionTimeLabel = tk.Label(self.voor, text = "Reaction Time")
        self.voorResponseFactorLabel = tk.Label(self.voor, text = "Response Factor")
        self.voorRecoveryTimeLabel = tk.Label(self.voor, text = "Recovery Time")

        #Spinbox for setup
        self.voorLowerRateLimitEntry = tk.Spinbox(self.voor,from_=30,to=175,increment=5)
        self.voorUpperRateLimitEntry = tk.Spinbox(self.voor,from_=50,to=175,increment=5)
        self.voorVentricularAmplitudeEntry = tk.Spinbox(self.voor,from_=0.5,to=7.0,format="%.1f",increment=0.1)
        self.voorVentricularPulseWidthEntry = tk.Spinbox(self.voor,from_=0.05,to=1.9,format="%.2f",increment=0.1)
        self.voorMaximumSensorRateEntry = tk.Spinbox(self.voor,from_=50,to=175,increment=5)
        self.voorActivityThresholdEntry = ttk.Combobox(self.voor)
        self.voorActivityThresholdEntry['values']= ("V-Low", "Low", "Med-Low", "Med", "Med-High", "High","V-High")
        self.voorActivityThresholdEntry.current(3)
        self.voorReactionTimeEntry = tk.Spinbox(self.voor,from_=10,to=50,increment=10)
        self.voorResponseFactorEntry = tk.Spinbox(self.voor,from_=1,to=16,increment=1)
        self.voorRecoveryTimeEntry = tk.Spinbox(self.voor,from_=2,to=16,increment=1)

        #Setup buttons
        self.voorLowerRateLimitButton = tk.Button(self.voor, text = "Set", command= lambda: self.setValue("voorLowerRateLimit"))
        self.voorUpperRateLimitButton = tk.Button(self.voor, text = "Set", command= lambda: self.setValue("voorUpperRateLimit"))
        self.voorVentricularAmplitudeButton = tk.Button(self.voor, text = "Set", command= lambda: self.setValue("voorVentricularAmplitude"))
        self.voorVentricularPulseWidthButton = tk.Button(self.voor, text = "Set", command= lambda: self.setValue("voorVentricularPulseWidth"))
        self.voorMaximumSensorRateButton = tk.Button(self.voor, text = "Set", command= lambda: self.setValue("voorMaximumSensorRate"))
        self.voorActivityThresholdButton = tk.Button(self.voor, text = "Set", command= lambda: self.setValue("voorActivityThreshold"))
        self.voorReactionTimeButton = tk.Button(self.voor, text = "Set", command= lambda: self.setValue("voorReactionTime"))
        self.voorResponseFactorButton = tk.Button(self.voor, text = "Set", command= lambda: self.setValue("voorResponseFactor"))
        self.voorRecoveryTimeButton = tk.Button(self.voor, text = "Set", command= lambda: self.setValue("voorRecoveryTime"))

        #Setup  labels to display values
        self.voorLowerRateLimitValue = tk.Label(self.voor, text = "Current Value: " + voor_lowerRateLimitEntry)
        self.voorUpperRateLimitValue = tk.Label(self.voor, text = "Current Value: " + voor_upperRateLimitEntry)
        self.voorVentricularAmplitudeValue = tk.Label(self.voor, text = "Current Value: " + voor_ventricularAmplitudeEntry)
        self.voorVentricularPulseWidthValue = tk.Label(self.voor, text = "Current Value: " + voor_ventricularPulseWidthEntry)
        self.voorMaximumSensorRateValue = tk.Label(self.voor, text = "Current Value: " + voor_maximumSensorRateEntry)
        self.voorActivityThresholdValue = tk.Label(self.voor, text = "Current Value: " + voor_activityThresholdEntry)
        self.voorReactionTimeValue = tk.Label(self.voor, text = "Current Value: " + voor_reactionTimeEntry)
        self.voorResponseFactorValue = tk.Label(self.voor, text = "Current Value: " + voor_responseFactorEntry)
        self.voorRecoveryTimeValue = tk.Label(self.voor, text = "Current Value: " + voor_recoveryTimeEntry)

        #Adjust positioning
        self.voorLowerRateLimitLabel.grid(row=0, column=0, padx=15, pady=15)
        self.voorLowerRateLimitEntry.grid(row=0, column=1, padx=15, pady=15)
        self.voorLowerRateLimitButton.grid(row=0, column=2, padx=15, pady=15)
        self.voorLowerRateLimitValue.grid(row=0, column=3, padx=15, pady=15)

        self.voorUpperRateLimitLabel.grid(row=1, column=0, padx=15, pady=15)
        self.voorUpperRateLimitEntry.grid(row=1, column=1, padx=15, pady=15)
        self.voorUpperRateLimitButton.grid(row=1, column=2, padx=15, pady=15)
        self.voorUpperRateLimitValue.grid(row=1, column=3, padx=15, pady=15)

        self.voorVentricularAmplitudeLabel.grid(row=2, column=0, padx=15, pady=15)
        self.voorVentricularAmplitudeEntry.grid(row=2, column=1, padx=15, pady=15)
        self.voorVentricularAmplitudeButton.grid(row=2, column=2, padx=15, pady=15)
        self.voorVentricularAmplitudeValue.grid(row=2, column=3, padx=15, pady=15)

        self.voorVentricularPulseWidthLabel.grid(row=3, column=0, padx=15, pady=15)
        self.voorVentricularPulseWidthEntry.grid(row=3, column=1, padx=15, pady=15)
        self.voorVentricularPulseWidthButton.grid(row=3, column=2, padx=15, pady=15)
        self.voorVentricularPulseWidthValue.grid(row=3, column=3, padx=15, pady=15)
        
        self.voorMaximumSensorRateLabel.grid(row=0, column=5, padx=15, pady=15)
        self.voorMaximumSensorRateEntry.grid(row=0, column=6, padx=15, pady=15)
        self.voorMaximumSensorRateButton.grid(row=0, column=7, padx=15, pady=15)
        self.voorMaximumSensorRateValue.grid(row=0, column=8, padx=15, pady=15)

        self.voorActivityThresholdLabel.grid(row=1, column=5, padx=15, pady=15)
        self.voorActivityThresholdEntry.grid(row=1, column=6, padx=15, pady=15)
        self.voorActivityThresholdButton.grid(row=1, column=7, padx=15, pady=15)
        self.voorActivityThresholdValue.grid(row=1, column=8, padx=15, pady=15)

        self.voorReactionTimeLabel.grid(row=2, column=5, padx=15, pady=15)
        self.voorReactionTimeEntry.grid(row=2, column=6, padx=15, pady=15)
        self.voorReactionTimeButton.grid(row=2, column=7, padx=15, pady=15)
        self.voorReactionTimeValue.grid(row=2, column=8, padx=15, pady=15)

        self.voorResponseFactorLabel.grid(row=3, column=5, padx=15, pady=15)
        self.voorResponseFactorEntry.grid(row=3, column=6, padx=15, pady=15)
        self.voorResponseFactorButton.grid(row=3, column=7, padx=15, pady=15)
        self.voorResponseFactorValue.grid(row=3, column=8, padx=15, pady=15)

        self.voorRecoveryTimeLabel.grid(row=4, column=5, padx=15, pady=15)
        self.voorRecoveryTimeEntry.grid(row=4, column=6, padx=15, pady=15)
        self.voorRecoveryTimeButton.grid(row=4, column=7, padx=15, pady=15)
        self.voorRecoveryTimeValue.grid(row=4, column=8, padx=15, pady=15)
        #VOOR END------------------------------------------------------------------------------------------------------------------------------

        #AAIR BEGIN----------------------------------------------------------------------------------------------------------------------------
        #Setup labels for inputs
        self.aairLowerRateLimitLabel = tk.Label(self.aair, text = "Lower Rate Limit")
        self.aairUpperRateLimitLabel = tk.Label(self.aair, text = "Upper Rate Limit ")
        self.aairAtrialAmplitudeLabel = tk.Label(self.aair, text = "Atrial Amplitude")
        self.aairAtrialPulseWidthLabel = tk.Label(self.aair, text = "Atrial Pulse Width")
        self.aairAtrialSensitivityLabel = tk.Label(self.aair, text = "Atrial Sensitivity")
        self.aairARPLabel = tk.Label(self.aair, text = "ARP")
        self.aairPVARPLabel = tk.Label(self.aair, text = "APVARP")
        self.aairHysteresisLabel = tk.Label(self.aair, text = "Hysteresis")
        self.aairRateSmoothingLabel = tk.Label(self.aair, text = "Rate Smoothing")
        self.aairMaximumSensorRateLabel = tk.Label(self.aair, text = "Maximum Sensor Rate")
        self.aairActivityThresholdLabel = tk.Label(self.aair, text = "Activity Threshold")
        self.aairReactionTimeLabel = tk.Label(self.aair, text = "Reaction Time")
        self.aairResponseFactorLabel = tk.Label(self.aair, text = "Response Factor")
        self.aairRecoveryTimeLabel = tk.Label(self.aair, text = "Recovery Time")
        
        #Spinbox for setup
        self.aairLowerRateLimitEntry = tk.Spinbox(self.aair,from_=30,to=175,increment=5)
        self.aairUpperRateLimitEntry = tk.Spinbox(self.aair,from_=50,to=175,increment=5)
        self.aairAtrialAmplitudeEntry = tk.Spinbox(self.aair,from_=0.5,to=7.0,format="%.1f",increment=0.1)
        self.aairAtrialPulseWidthEntry = tk.Spinbox(self.aair,from_=0.05,to=1.9,format="%.2f",increment=0.1)
        self.aairAtrialSensitivityEntry = tk.Spinbox(self.aair,from_=0.25,to=10.0,format="%.2f",increment=0.25)
        self.aairARPEntry = tk.Spinbox(self.aair,from_=150,to=500,increment=10)
        self.aairPVARPEntry = tk.Spinbox(self.aair,from_=150,to=500,increment=10)
        self.aairHysteresisEntry = tk.Spinbox(self.aair,from_=0,to=25,increment=5)
        self.aairRateSmoothingEntry = tk.Spinbox(self.aair,from_=0,to=25,increment=3)
        self.aairMaximumSensorRateEntry = tk.Spinbox(self.aair,from_=50,to=175,increment=5)
        self.aairActivityThresholdEntry = ttk.Combobox(self.aair)
        self.aairActivityThresholdEntry['values']= ("V-Low", "Low", "Med-Low", "Med", "Med-High", "High","V-High")
        self.aairActivityThresholdEntry.current(3)
        self.aairReactionTimeEntry = tk.Spinbox(self.aair,from_=10,to=50,increment=10)
        self.aairResponseFactorEntry = tk.Spinbox(self.aair,from_=1,to=16,increment=1)
        self.aairRecoveryTimeEntry = tk.Spinbox(self.aair,from_=2,to=16,increment=1)

        #Setup buttons
        self.aairLowerRateLimitButton = tk.Button(self.aair, text = "Set", command= lambda: self.setValue("aairLowerRateLimit"))
        self.aairUpperRateLimitButton = tk.Button(self.aair, text = "Set", command= lambda: self.setValue("aairUpperRateLimit"))
        self.aairAtrialAmplitudeButton = tk.Button(self.aair, text = "Set", command= lambda: self.setValue("aairAtrialAmplitude"))
        self.aairAtrialPulseWidthButton = tk.Button(self.aair, text = "Set", command= lambda: self.setValue("aairAtrialPulseWidth"))
        self.aairAtrialSensitivityButton = tk.Button(self.aair, text = "Set", command= lambda: self.setValue("aairAtrialSensitivity"))
        self.aairARPButton = tk.Button(self.aair, text = "Set", command= lambda: self.setValue("aairARP"))
        self.aairPVARPButton = tk.Button(self.aair, text = "Set", command= lambda: self.setValue("aairPVARP"))
        self.aairHysteresisButton = tk.Button(self.aair, text = "Set", command= lambda: self.setValue("aairHysteresis"))
        self.aairRateSmoothingButton = tk.Button(self.aair, text = "Set", command= lambda: self.setValue("aairRateSmoothing"))
        self.aairMaximumSensorRateButton = tk.Button(self.aair, text = "Set", command= lambda: self.setValue("aairMaximumSensorRate"))
        self.aairActivityThresholdButton = tk.Button(self.aair, text = "Set", command= lambda: self.setValue("aairActivityThreshold"))
        self.aairReactionTimeButton = tk.Button(self.aair, text = "Set", command= lambda: self.setValue("aairReactionTime"))
        self.aairResponseFactorButton = tk.Button(self.aair, text = "Set", command= lambda: self.setValue("aairResponseFactor"))
        self.aairRecoveryTimeButton = tk.Button(self.aair, text = "Set", command= lambda: self.setValue("aairRecoveryTime"))

        #Setup  labels to display values
        self.aairLowerRateLimitValue = tk.Label(self.aair, text = "Current Value: "+ aair_lowerRateLimitEntry)
        self.aairUpperRateLimitValue = tk.Label(self.aair, text = "Current Value: "+ aair_upperRateLimitEntry)
        self.aairAtrialAmplitudeValue = tk.Label(self.aair, text = "Current Value: "+ aair_atrialAmplitudeEntry)
        self.aairAtrialPulseWidthValue = tk.Label(self.aair, text = "Current Value: "+ aair_atrialPulseWidthEntry)
        self.aairAtrialSensitivityValue = tk.Label(self.aair, text = "Current Value: "+ aair_atrialSensitivityEntry)
        self.aairARPValue = tk.Label(self.aair, text = "Current Value: "+ aair_ARPEntry)
        self.aairPVARPValue = tk.Label(self.aair, text = "Current Value: "+ aair_PVARPEntry)
        self.aairHysteresisValue = tk.Label(self.aair, text = "Current Value: "+ aair_hysteresisEntry)
        self.aairRateSmoothingValue = tk.Label(self.aair, text = "Current Value: "+ aair_rateSmoothingEntry)
        self.aairMaximumSensorRateValue = tk.Label(self.aair, text = "Current Value: " + aair_maximumSensorRateEntry)
        self.aairActivityThresholdValue = tk.Label(self.aair, text = "Current Value: " + aair_activityThresholdEntry)
        self.aairReactionTimeValue = tk.Label(self.aair, text = "Current Value: " + aair_reactionTimeEntry)
        self.aairResponseFactorValue = tk.Label(self.aair, text = "Current Value: " + aair_responseFactorEntry)
        self.aairRecoveryTimeValue = tk.Label(self.aair, text = "Current Value: " + aair_recoveryTimeEntry)

        #Adjust positioning
        self.aairLowerRateLimitLabel.grid(row=0, column=0, padx=15, pady=15)
        self.aairLowerRateLimitEntry.grid(row=0, column=1, padx=15, pady=15)
        self.aairLowerRateLimitButton.grid(row=0, column=2, padx=15, pady=15)
        self.aairLowerRateLimitValue.grid(row=0, column=3, padx=15, pady=15)
        
        self.aairUpperRateLimitLabel.grid(row=1, column=0, padx=15, pady=15)
        self.aairUpperRateLimitEntry.grid(row=1, column=1, padx=15, pady=15)
        self.aairUpperRateLimitButton.grid(row=1, column=2, padx=15, pady=15)
        self.aairUpperRateLimitValue.grid(row=1, column=3, padx=15, pady=15)       

        self.aairAtrialAmplitudeLabel.grid(row=2, column=0, padx=15, pady=15)
        self.aairAtrialAmplitudeEntry.grid(row=2, column=1, padx=15, pady=15)
        self.aairAtrialAmplitudeButton.grid(row=2, column=2, padx=15, pady=15)
        self.aairAtrialAmplitudeValue.grid(row=2, column=3, padx=15, pady=15)
        
        self.aairAtrialPulseWidthLabel.grid(row=3, column=0, padx=15, pady=15)
        self.aairAtrialPulseWidthEntry.grid(row=3, column=1, padx=15, pady=15)
        self.aairAtrialPulseWidthButton.grid(row=3, column=2, padx=15, pady=15)
        self.aairAtrialPulseWidthValue.grid(row=3, column=3, padx=15, pady=15)
        
        self.aairAtrialSensitivityLabel.grid(row=4, column=0, padx=15, pady=15)
        self.aairAtrialSensitivityEntry.grid(row=4, column=1, padx=15, pady=15)
        self.aairAtrialSensitivityButton.grid(row=4, column=2, padx=15, pady=15)
        self.aairAtrialSensitivityValue.grid(row=4, column=3, padx=15, pady=15)       

        self.aairARPLabel.grid(row=5, column=0, padx=15, pady=15)
        self.aairARPEntry.grid(row=5, column=1, padx=15, pady=15)
        self.aairARPButton.grid(row=5, column=2, padx=15, pady=15)
        self.aairARPValue.grid(row=5, column=3, padx=15, pady=15)
        
        self.aairPVARPLabel.grid(row=6, column=0, padx=15, pady=15)
        self.aairPVARPEntry.grid(row=6, column=1, padx=15, pady=15)
        self.aairPVARPButton.grid(row=6, column=2, padx=15, pady=15)
        self.aairPVARPValue.grid(row=6, column=3, padx=15, pady=15)
        
        self.aairHysteresisLabel.grid(row=7, column=0, padx=15, pady=15)
        self.aairHysteresisEntry.grid(row=7, column=1, padx=15, pady=15)
        self.aairHysteresisButton.grid(row=7, column=2, padx=15, pady=15)
        self.aairHysteresisValue.grid(row=7, column=3, padx=15, pady=15)
        
        self.aairRateSmoothingLabel.grid(row=8, column=0, padx=15, pady=15)
        self.aairRateSmoothingEntry.grid(row=8, column=1, padx=15, pady=15)
        self.aairRateSmoothingButton.grid(row=8, column=2, padx=15, pady=15)
        self.aairRateSmoothingValue.grid(row=8, column=3, padx=15, pady=15)

        self.aairMaximumSensorRateLabel.grid(row=0, column=5, padx=15, pady=15)
        self.aairMaximumSensorRateEntry.grid(row=0, column=6, padx=15, pady=15)
        self.aairMaximumSensorRateButton.grid(row=0, column=7, padx=15, pady=15)
        self.aairMaximumSensorRateValue.grid(row=0, column=8, padx=15, pady=15)

        self.aairActivityThresholdLabel.grid(row=1, column=5, padx=15, pady=15)
        self.aairActivityThresholdEntry.grid(row=1, column=6, padx=15, pady=15)
        self.aairActivityThresholdButton.grid(row=1, column=7, padx=15, pady=15)
        self.aairActivityThresholdValue.grid(row=1, column=8, padx=15, pady=15)

        self.aairReactionTimeLabel.grid(row=2, column=5, padx=15, pady=15)
        self.aairReactionTimeEntry.grid(row=2, column=6, padx=15, pady=15)
        self.aairReactionTimeButton.grid(row=2, column=7, padx=15, pady=15)
        self.aairReactionTimeValue.grid(row=2, column=8, padx=15, pady=15)

        self.aairResponseFactorLabel.grid(row=3, column=5, padx=15, pady=15)
        self.aairResponseFactorEntry.grid(row=3, column=6, padx=15, pady=15)
        self.aairResponseFactorButton.grid(row=3, column=7, padx=15, pady=15)
        self.aairResponseFactorValue.grid(row=3, column=8, padx=15, pady=15)

        self.aairRecoveryTimeLabel.grid(row=4, column=5, padx=15, pady=15)
        self.aairRecoveryTimeEntry.grid(row=4, column=6, padx=15, pady=15)
        self.aairRecoveryTimeButton.grid(row=4, column=7, padx=15, pady=15)
        self.aairRecoveryTimeValue.grid(row=4, column=8, padx=15, pady=15)
        #AAIR END------------------------------------------------------------------------------------------------------------------------------

        #VVIR BEGIN----------------------------------------------------------------------------------------------------------------------------
        #Setup labels for inputs
        self.vvirLowerRateLimitLabel = tk.Label(self.vvir, text = "Lower Rate Limit")
        self.vvirUpperRateLimitLabel = tk.Label(self.vvir, text = "Upper Rate Limit ")
        self.vvirVentricularAmplitudeLabel = tk.Label(self.vvir, text = "Ventricular Amplitude")
        self.vvirVentricularPulseWidthLabel = tk.Label(self.vvir, text = "Ventricular Pulse Width")
        self.vvirVentricularSensitivityLabel = tk.Label(self.vvir, text = "Ventricular Sensitivity")
        self.vvirVRPLabel = tk.Label(self.vvir, text = "VRP")
        self.vvirHysteresisLabel = tk.Label(self.vvir, text = "Hysteresis")
        self.vvirRateSmoothingLabel = tk.Label(self.vvir, text = "Rate Smoothing")
        self.vvirMaximumSensorRateLabel = tk.Label(self.vvir, text = "Maximum Sensor Rate")
        self.vvirActivityThresholdLabel = tk.Label(self.vvir, text = "Activity Threshold")
        self.vvirReactionTimeLabel = tk.Label(self.vvir, text = "Reaction Time")
        self.vvirResponseFactorLabel = tk.Label(self.vvir, text = "Response Factor")
        self.vvirRecoveryTimeLabel = tk.Label(self.vvir, text = "Recovery Time")

        #Spinbox for setup
        self.vvirLowerRateLimitEntry = tk.Spinbox(self.vvir,from_=30,to=175,increment=5)
        self.vvirUpperRateLimitEntry = tk.Spinbox(self.vvir,from_=50,to=175,increment=5)
        self.vvirVentricularAmplitudeEntry = tk.Spinbox(self.vvir,from_=0.5,to=7.0,format="%.1f",increment=0.1)
        self.vvirVentricularPulseWidthEntry = tk.Spinbox(self.vvir,from_=0.05,to=1.9,format="%.2f",increment=0.1)
        self.vvirVentricularSensitivityEntry = tk.Spinbox(self.vvir,from_=0.25,to=10.0,format="%.2f",increment=0.25)
        self.vvirVRPEntry = tk.Spinbox(self.vvir,from_=150,to=500,increment=10)
        self.vvirHysteresisEntry = tk.Spinbox(self.vvir,from_=0,to=25,increment=5)
        self.vvirRateSmoothingEntry = tk.Spinbox(self.vvir,from_=0,to=25,increment=3)
        self.vvirMaximumSensorRateEntry = tk.Spinbox(self.vvir,from_=50,to=175,increment=5)
        self.vvirActivityThresholdEntry = ttk.Combobox(self.vvir)
        self.vvirActivityThresholdEntry['values']= ("V-Low", "Low", "Med-Low", "Med", "Med-High", "High","V-High")
        self.vvirActivityThresholdEntry.current(3)
        self.vvirReactionTimeEntry = tk.Spinbox(self.vvir,from_=10,to=50,increment=10)
        self.vvirResponseFactorEntry = tk.Spinbox(self.vvir,from_=1,to=16,increment=1)
        self.vvirRecoveryTimeEntry = tk.Spinbox(self.vvir,from_=2,to=16,increment=1)
        
        #Setup buttons
        self.vvirLowerRateLimitButton = tk.Button(self.vvir, text = "Set", command= lambda: self.setValue("vvirLowerRateLimit"))
        self.vvirUpperRateLimitButton = tk.Button(self.vvir, text = "Set", command= lambda: self.setValue("vvirUpperRateLimit"))
        self.vvirVentricularAmplitudeButton = tk.Button(self.vvir, text = "Set", command= lambda: self.setValue("vvirVentricularAmplitude"))
        self.vvirVentricularPulseWidthButton = tk.Button(self.vvir, text = "Set", command= lambda: self.setValue("vvirVentricularPulseWidth"))
        self.vvirVentricularSensitivityButton = tk.Button(self.vvir, text = "Set", command= lambda: self.setValue("vvirVentricularSensitivity"))
        self.vvirVRPButton = tk.Button(self.vvir, text = "Set", command= lambda: self.setValue("vvirVRP"))
        self.vvirHysteresisButton = tk.Button(self.vvir, text = "Set", command= lambda: self.setValue("vvirHysteresis"))
        self.vvirRateSmoothingButton = tk.Button(self.vvir, text = "Set", command= lambda: self.setValue("vvirRateSmoothing"))
        self.vvirMaximumSensorRateButton = tk.Button(self.vvir, text = "Set", command= lambda: self.setValue("vvirMaximumSensorRate"))
        self.vvirActivityThresholdButton = tk.Button(self.vvir, text = "Set", command= lambda: self.setValue("vvirActivityThreshold"))
        self.vvirReactionTimeButton = tk.Button(self.vvir, text = "Set", command= lambda: self.setValue("vvirReactionTime"))
        self.vvirResponseFactorButton = tk.Button(self.vvir, text = "Set", command= lambda: self.setValue("vvirResponseFactor"))
        self.vvirRecoveryTimeButton = tk.Button(self.vvir, text = "Set", command= lambda: self.setValue("vvirRecoveryTime"))

        #Setup  labels to display values
        self.vvirLowerRateLimitValue = tk.Label(self.vvir, text = "Current Value: "+ vvir_lowerRateLimitEntry)
        self.vvirUpperRateLimitValue = tk.Label(self.vvir, text = "Current Value: "+ vvir_upperRateLimitEntry)
        self.vvirVentricularAmplitudeValue = tk.Label(self.vvir, text = "Current Value: "+ vvir_ventricularAmplitudeEntry)
        self.vvirVentricularPulseWidthValue = tk.Label(self.vvir, text = "Current Value: "+ vvir_ventricularPulseWidthEntry)
        self.vvirVentricularSensitivityValue = tk.Label(self.vvir, text = "Current Value: "+ vvir_ventricularSensitivityEntry)
        self.vvirVRPValue = tk.Label(self.vvir, text = "Current Value: "+ vvir_VRPEntry)
        self.vvirHysteresisValue = tk.Label(self.vvir, text = "Current Value: "+ vvir_hysteresisEntry)
        self.vvirRateSmoothingValue = tk.Label(self.vvir, text = "Current Value: "+ vvir_rateSmoothingEntry)
        self.vvirMaximumSensorRateValue = tk.Label(self.vvir, text = "Current Value: " + vvir_maximumSensorRateEntry)
        self.vvirActivityThresholdValue = tk.Label(self.vvir, text = "Current Value: " + vvir_activityThresholdEntry)
        self.vvirReactionTimeValue = tk.Label(self.vvir, text = "Current Value: " + vvir_reactionTimeEntry)
        self.vvirResponseFactorValue = tk.Label(self.vvir, text = "Current Value: " + vvir_responseFactorEntry)
        self.vvirRecoveryTimeValue = tk.Label(self.vvir, text = "Current Value: " + vvir_recoveryTimeEntry)

        #Adjust positioning
        self.vvirLowerRateLimitLabel.grid(row=0, column=0, padx=15, pady=15)
        self.vvirLowerRateLimitEntry.grid(row=0, column=1, padx=15, pady=15)
        self.vvirLowerRateLimitButton.grid(row=0, column=2, padx=15, pady=15)
        self.vvirLowerRateLimitValue.grid(row=0, column=3, padx=15, pady=15)
        
        self.vvirUpperRateLimitLabel.grid(row=1, column=0, padx=15, pady=15)
        self.vvirUpperRateLimitEntry.grid(row=1, column=1, padx=15, pady=15)
        self.vvirUpperRateLimitButton.grid(row=1, column=2, padx=15, pady=15)
        self.vvirUpperRateLimitValue.grid(row=1, column=3, padx=15, pady=15)
        
        self.vvirVentricularAmplitudeLabel.grid(row=2, column=0, padx=15, pady=15)
        self.vvirVentricularAmplitudeEntry.grid(row=2, column=1, padx=15, pady=15)
        self.vvirVentricularAmplitudeButton.grid(row=2, column=2, padx=15, pady=15)
        self.vvirVentricularAmplitudeValue.grid(row=2, column=3, padx=15, pady=15)
        
        self.vvirVentricularPulseWidthLabel.grid(row=3, column=0, padx=15, pady=15)
        self.vvirVentricularPulseWidthEntry.grid(row=3, column=1, padx=15, pady=15)
        self.vvirVentricularPulseWidthButton.grid(row=3, column=2, padx=15, pady=15)
        self.vvirVentricularPulseWidthValue.grid(row=3, column=3, padx=15, pady=15)
        
        self.vvirVentricularSensitivityLabel.grid(row=4, column=0, padx=15, pady=15)
        self.vvirVentricularSensitivityEntry.grid(row=4, column=1, padx=15, pady=15)
        self.vvirVentricularSensitivityButton.grid(row=4, column=2, padx=15, pady=15)
        self.vvirVentricularSensitivityValue.grid(row=4, column=3, padx=15, pady=15)
        
        self.vvirVRPLabel.grid(row=5, column=0, padx=15, pady=15)
        self.vvirVRPEntry.grid(row=5, column=1, padx=15, pady=15)
        self.vvirVRPButton.grid(row=5, column=2, padx=15, pady=15)
        self.vvirVRPValue.grid(row=5, column=3, padx=15, pady=15)
        
        self.vvirHysteresisLabel.grid(row=6, column=0, padx=15, pady=15)
        self.vvirHysteresisEntry.grid(row=6, column=1, padx=15, pady=15)
        self.vvirHysteresisButton.grid(row=6, column=2, padx=15, pady=15)
        self.vvirHysteresisValue.grid(row=6, column=3, padx=15, pady=15)
        
        self.vvirRateSmoothingLabel.grid(row=7, column=0, padx=15, pady=15)
        self.vvirRateSmoothingEntry.grid(row=7, column=1, padx=15, pady=15)
        self.vvirRateSmoothingButton.grid(row=7, column=2, padx=15, pady=15)
        self.vvirRateSmoothingValue.grid(row=7, column=3, padx=15, pady=15)

        self.vvirMaximumSensorRateLabel.grid(row=0, column=5, padx=15, pady=15)
        self.vvirMaximumSensorRateEntry.grid(row=0, column=6, padx=15, pady=15)
        self.vvirMaximumSensorRateButton.grid(row=0, column=7, padx=15, pady=15)
        self.vvirMaximumSensorRateValue.grid(row=0, column=8, padx=15, pady=15)

        self.vvirActivityThresholdLabel.grid(row=1, column=5, padx=15, pady=15)
        self.vvirActivityThresholdEntry.grid(row=1, column=6, padx=15, pady=15)
        self.vvirActivityThresholdButton.grid(row=1, column=7, padx=15, pady=15)
        self.vvirActivityThresholdValue.grid(row=1, column=8, padx=15, pady=15)

        self.vvirReactionTimeLabel.grid(row=2, column=5, padx=15, pady=15)
        self.vvirReactionTimeEntry.grid(row=2, column=6, padx=15, pady=15)
        self.vvirReactionTimeButton.grid(row=2, column=7, padx=15, pady=15)
        self.vvirReactionTimeValue.grid(row=2, column=8, padx=15, pady=15)

        self.vvirResponseFactorLabel.grid(row=3, column=5, padx=15, pady=15)
        self.vvirResponseFactorEntry.grid(row=3, column=6, padx=15, pady=15)
        self.vvirResponseFactorButton.grid(row=3, column=7, padx=15, pady=15)
        self.vvirResponseFactorValue.grid(row=3, column=8, padx=15, pady=15)

        self.vvirRecoveryTimeLabel.grid(row=4, column=5, padx=15, pady=15)
        self.vvirRecoveryTimeEntry.grid(row=4, column=6, padx=15, pady=15)
        self.vvirRecoveryTimeButton.grid(row=4, column=7, padx=15, pady=15)
        self.vvirRecoveryTimeValue.grid(row=4, column=8, padx=15, pady=15)
        #VVIR END------------------------------------------------------------------------------------------------------------------------------

        #DOOR BEGIN----------------------------------------------------------------------------------------------------------------------------
        #Setup labels for inputs
        self.doorLowerRateLimitLabel = tk.Label(self.door, text = "Lower Rate Limit")
        self.doorUpperRateLimitLabel = tk.Label(self.door, text = "Upper Rate Limit")
        self.doorAtrialAmplitudeLabel = tk.Label(self.door, text = "Atrial Amplitude")
        self.doorAtrialPulseWidthLabel = tk.Label(self.door, text = "Atrial Pulse Width")
        self.doorVentricularAmplitudeLabel = tk.Label(self.door, text = "Ventricular Amplitude")
        self.doorVentricularPulseWidthLabel = tk.Label(self.door, text = "Ventricular Pulse Width")
        self.doorFixedAVDelayLabel = tk.Label(self.door, text = "Fixed AV Delay")
        self.doorMaximumSensorRateLabel = tk.Label(self.door, text = "Maximum Sensor Rate")
        self.doorActivityThresholdLabel = tk.Label(self.door, text = "Activity Threshold")
        self.doorReactionTimeLabel = tk.Label(self.door, text = "Reaction Time")
        self.doorResponseFactorLabel = tk.Label(self.door, text = "Response Factor")
        self.doorRecoveryTimeLabel = tk.Label(self.door, text = "Recovery Time")

        #Spinbox for setup
        self.doorLowerRateLimitEntry = tk.Spinbox(self.door,from_=30,to=175,increment=5)
        self.doorUpperRateLimitEntry = tk.Spinbox(self.door,from_=50,to=175,increment=5)
        self.doorAtrialAmplitudeEntry = tk.Spinbox(self.door,from_=0.5,to=7.0,format="%.1f",increment=0.1)
        self.doorAtrialPulseWidthEntry = tk.Spinbox(self.door,from_=0.05,to=1.9,format="%.2f",increment=0.1)
        self.doorVentricularAmplitudeEntry = tk.Spinbox(self.door,from_=0.5,to=7.0,format="%.1f",increment=0.1)
        self.doorVentricularPulseWidthEntry = tk.Spinbox(self.door,from_=0.05,to=1.9,format="%.2f",increment=0.1)
        self.doorFixedAVDelayEntry = tk.Spinbox(self.door,from_=70,to=300,increment=10)
        self.doorMaximumSensorRateEntry = tk.Spinbox(self.door,from_=50,to=175,increment=5)
        self.doorActivityThresholdEntry = ttk.Combobox(self.door)
        self.doorActivityThresholdEntry['values']= ("V-Low", "Low", "Med-Low", "Med", "Med-High", "High","V-High")
        self.doorActivityThresholdEntry.current(3)
        self.doorReactionTimeEntry = tk.Spinbox(self.door,from_=10,to=50,increment=10)
        self.doorResponseFactorEntry = tk.Spinbox(self.door,from_=1,to=16,increment=1)
        self.doorRecoveryTimeEntry = tk.Spinbox(self.door,from_=2,to=16,increment=1)
        
        #Setup buttons
        self.doorLowerRateLimitButton = tk.Button(self.door, text = "Set", command= lambda: self.setValue("doorLowerRateLimit"))
        self.doorUpperRateLimitButton = tk.Button(self.door, text = "Set", command= lambda: self.setValue("doorUpperRateLimit"))
        self.doorAtrialAmplitudeButton = tk.Button(self.door, text = "Set", command= lambda: self.setValue("doorAtrialAmplitude"))
        self.doorAtrialPulseWidthButton = tk.Button(self.door, text = "Set", command= lambda: self.setValue("doorAtrialPulseWidth"))
        self.doorVentricularAmplitudeButton = tk.Button(self.door, text = "Set", command= lambda: self.setValue("doorVentricularAmplitude"))
        self.doorVentricularPulseWidthButton = tk.Button(self.door, text = "Set", command= lambda: self.setValue("doorVentricularPulseWidth"))
        self.doorFixedAVDelayButton = tk.Button(self.door, text = "Set", command= lambda: self.setValue("doorFixedAVDelay"))
        self.doorMaximumSensorRateButton = tk.Button(self.door, text = "Set", command= lambda: self.setValue("doorMaximumSensorRate"))
        self.doorActivityThresholdButton = tk.Button(self.door, text = "Set", command= lambda: self.setValue("doorActivityThreshold"))
        self.doorReactionTimeButton = tk.Button(self.door, text = "Set", command= lambda: self.setValue("doorReactionTime"))
        self.doorResponseFactorButton = tk.Button(self.door, text = "Set", command= lambda: self.setValue("doorResponseFactor"))
        self.doorRecoveryTimeButton = tk.Button(self.door, text = "Set", command= lambda: self.setValue("doorRecoveryTime"))
        
        #Setup labels to display values
        self.doorLowerRateLimitValue = tk.Label(self.door, text = "Current Value: " + door_lowerRateLimitEntry)
        self.doorUpperRateLimitValue = tk.Label(self.door, text = "Current Value: " + door_upperRateLimitEntry)
        self.doorAtrialAmplitudeValue = tk.Label(self.door, text = "Current Value: " + door_atrialAmplitudeEntry)
        self.doorAtrialPulseWidthValue = tk.Label(self.door, text = "Current Value: " + door_atrialPulseWidthEntry)
        self.doorVentricularAmplitudeValue = tk.Label(self.door, text = "Current Value: "+ door_ventricularAmplitudeEntry)
        self.doorVentricularPulseWidthValue = tk.Label(self.door, text = "Current Value: "+ door_ventricularPulseWidthEntry)
        self.doorFixedAVDelayValue = tk.Label(self.door, text = "Current Value: "+ door_fixedAVDelayEntry)
        self.doorMaximumSensorRateValue = tk.Label(self.door, text = "Current Value: " + door_maximumSensorRateEntry)
        self.doorActivityThresholdValue = tk.Label(self.door, text = "Current Value: " + door_activityThresholdEntry)
        self.doorReactionTimeValue = tk.Label(self.door, text = "Current Value: " + door_reactionTimeEntry)
        self.doorResponseFactorValue = tk.Label(self.door, text = "Current Value: " + door_responseFactorEntry)
        self.doorRecoveryTimeValue = tk.Label(self.door, text = "Current Value: " + door_recoveryTimeEntry)
        
        #Adjust positioning
        self.doorLowerRateLimitLabel.grid(row=0, column=0, padx=15, pady=15)
        self.doorLowerRateLimitEntry.grid(row=0, column=1, padx=15, pady=15)
        self.doorLowerRateLimitButton.grid(row=0, column=2, padx=15, pady=15)
        self.doorLowerRateLimitValue.grid(row=0, column=3, padx=15, pady=15)

        self.doorUpperRateLimitLabel.grid(row=1, column=0, padx=15, pady=15)
        self.doorUpperRateLimitEntry.grid(row=1, column=1, padx=15, pady=15)
        self.doorUpperRateLimitButton.grid(row=1, column=2, padx=15, pady=15)
        self.doorUpperRateLimitValue.grid(row=1, column=3, padx=15, pady=15)

        self.doorAtrialAmplitudeLabel.grid(row=2, column=0, padx=15, pady=15)
        self.doorAtrialAmplitudeEntry.grid(row=2, column=1, padx=15, pady=15)
        self.doorAtrialAmplitudeButton.grid(row=2, column=2, padx=15, pady=15)
        self.doorAtrialAmplitudeValue.grid(row=2, column=3, padx=15, pady=15)

        self.doorAtrialPulseWidthLabel.grid(row=3, column=0, padx=15, pady=15)
        self.doorAtrialPulseWidthEntry.grid(row=3, column=1, padx=15, pady=15)
        self.doorAtrialPulseWidthButton.grid(row=3, column=2, padx=15, pady=15)
        self.doorAtrialPulseWidthValue.grid(row=3, column=3, padx=15, pady=15)

        self.doorVentricularAmplitudeLabel.grid(row=4, column=0, padx=15, pady=15)
        self.doorVentricularAmplitudeEntry.grid(row=4, column=1, padx=15, pady=15)
        self.doorVentricularAmplitudeButton.grid(row=4, column=2, padx=15, pady=15)
        self.doorVentricularAmplitudeValue.grid(row=4, column=3, padx=15, pady=15)
        
        self.doorVentricularPulseWidthLabel.grid(row=5, column=0, padx=15, pady=15)
        self.doorVentricularPulseWidthEntry.grid(row=5, column=1, padx=15, pady=15)
        self.doorVentricularPulseWidthButton.grid(row=5, column=2, padx=15, pady=15)
        self.doorVentricularPulseWidthValue.grid(row=5, column=3, padx=15, pady=15)

        self.doorFixedAVDelayLabel.grid(row=6, column=0, padx=15, pady=15)
        self.doorFixedAVDelayEntry.grid(row=6, column=1, padx=15, pady=15)
        self.doorFixedAVDelayButton.grid(row=6, column=2, padx=15, pady=15)
        self.doorFixedAVDelayValue.grid(row=6, column=3, padx=15, pady=15)

        self.doorMaximumSensorRateLabel.grid(row=0, column=5, padx=15, pady=15)
        self.doorMaximumSensorRateEntry.grid(row=0, column=6, padx=15, pady=15)
        self.doorMaximumSensorRateButton.grid(row=0, column=7, padx=15, pady=15)
        self.doorMaximumSensorRateValue.grid(row=0, column=8, padx=15, pady=15)

        self.doorActivityThresholdLabel.grid(row=1, column=5, padx=15, pady=15)
        self.doorActivityThresholdEntry.grid(row=1, column=6, padx=15, pady=15)
        self.doorActivityThresholdButton.grid(row=1, column=7, padx=15, pady=15)
        self.doorActivityThresholdValue.grid(row=1, column=8, padx=15, pady=15)

        self.doorReactionTimeLabel.grid(row=2, column=5, padx=15, pady=15)
        self.doorReactionTimeEntry.grid(row=2, column=6, padx=15, pady=15)
        self.doorReactionTimeButton.grid(row=2, column=7, padx=15, pady=15)
        self.doorReactionTimeValue.grid(row=2, column=8, padx=15, pady=15)

        self.doorResponseFactorLabel.grid(row=3, column=5, padx=15, pady=15)
        self.doorResponseFactorEntry.grid(row=3, column=6, padx=15, pady=15)
        self.doorResponseFactorButton.grid(row=3, column=7, padx=15, pady=15)
        self.doorResponseFactorValue.grid(row=3, column=8, padx=15, pady=15)

        self.doorRecoveryTimeLabel.grid(row=4, column=5, padx=15, pady=15)
        self.doorRecoveryTimeEntry.grid(row=4, column=6, padx=15, pady=15)
        self.doorRecoveryTimeButton.grid(row=4, column=7, padx=15, pady=15)
        self.doorRecoveryTimeValue.grid(row=4, column=8, padx=15, pady=15)
        #DOOR END------------------------------------------------------------------------------------------------------------------------------

        #Track the process
        self.aooLogTitle = tk.Label(self.aoo, text = "Current Mode")
        self.aooLog = tk.Label(self.aoo, text = userlog)
        self.vooLogTitle = tk.Label(self.voo, text = "Current Mode")
        self.vooLog = tk.Label(self.voo, text = userlog)
        self.aaiLogTitle = tk.Label(self.aai, text = "Current Mode")
        self.aaiLog = tk.Label(self.aai, text = userlog)
        self.vviLogTitle = tk.Label(self.vvi, text = "Current Mode")
        self.vviLog = tk.Label(self.vvi, text = userlog)
        self.dooLogTitle = tk.Label(self.doo, text = "Current Mode")
        self.dooLog = tk.Label(self.doo, text = userlog)
        self.aoorLogTitle = tk.Label(self.aoor, text = "Current Mode")
        self.aoorLog = tk.Label(self.aoor, text = userlog)
        self.voorLogTitle = tk.Label(self.voor, text = "Current Mode")
        self.voorLog = tk.Label(self.voor, text = userlog)
        self.aairLogTitle = tk.Label(self.aair, text = "Current Mode")
        self.aairLog = tk.Label(self.aair, text = userlog)
        self.vvirLogTitle = tk.Label(self.vvir, text = "Current Mode")
        self.vvirLog = tk.Label(self.vvir, text = userlog)
        self.doorLogTitle = tk.Label(self.door, text = "Current Mode")
        self.doorLog = tk.Label(self.door, text = userlog)

        #Setup confirm buttons
        self.aooConfirmButton = tk.Button(self.aoo, text = 'Confirm', width = 20, command = lambda: self.confirmChanges("aooConfirm"))
        self.vooConfirmButton = tk.Button(self.voo, text = 'Confirm', width = 20, command = lambda: self.confirmChanges("vooConfirm"))
        self.aaiConfirmButton = tk.Button(self.aai, text = 'Confirm', width = 20, command = lambda: self.confirmChanges("aaiConfirm"))
        self.vviConfirmButton = tk.Button(self.vvi, text = 'Confirm', width = 20, command = lambda: self.confirmChanges("vviConfirm"))
        self.dooConfirmButton = tk.Button(self.doo, text = 'Confirm', width = 20, command = lambda: self.confirmChanges("dooConfirm"))
        self.aoorConfirmButton = tk.Button(self.aoor, text = 'Confirm', width = 20, command = lambda: self.confirmChanges("aoorConfirm"))
        self.voorConfirmButton = tk.Button(self.voor, text = 'Confirm', width = 20, command = lambda: self.confirmChanges("voorConfirm"))
        self.aairConfirmButton = tk.Button(self.aair, text = 'Confirm', width = 20, command = lambda: self.confirmChanges("aairConfirm"))
        self.vvirConfirmButton = tk.Button(self.vvir, text = 'Confirm', width = 20, command = lambda: self.confirmChanges("vvirConfirm"))
        self.doorConfirmButton = tk.Button(self.door, text = 'Confirm', width = 20, command = lambda: self.confirmChanges("doorConfirm"))
        
        #Setup logoff button
        self.aooLogoffButton = tk.Button(self.aoo, text = 'LogOff', width = 12, command = self.logOff)
        self.vooLogoffButton = tk.Button(self.voo, text = 'LogOff', width = 12, command = self.logOff)
        self.aaiLogoffButton = tk.Button(self.aai, text = 'LogOff', width = 12, command = self.logOff)
        self.vviLogoffButton = tk.Button(self.vvi, text = 'LogOff', width = 12, command = self.logOff)
        self.dooLogoffButton = tk.Button(self.doo, text = 'LogOff', width = 12, command = self.logOff)
        self.aoorLogoffButton = tk.Button(self.aoor, text = 'LogOff', width = 12, command = self.logOff)
        self.voorLogoffButton = tk.Button(self.voor, text = 'LogOff', width = 12, command = self.logOff)
        self.aairLogoffButton = tk.Button(self.aair, text = 'LogOff', width = 12, command = self.logOff)
        self.vvirLogoffButton = tk.Button(self.vvir, text = 'LogOff', width = 12, command = self.logOff)
        self.doorLogoffButton = tk.Button(self.door, text = 'LogOff', width = 12, command = self.logOff)
        
        #Adjust positioning
        self.aooLogTitle.grid(row=8, column=4, padx=15, pady=15)
        self.vooLogTitle.grid(row=8, column=4, padx=15, pady=15)
        self.aaiLogTitle.grid(row=8, column=4, padx=15, pady=15)
        self.vviLogTitle.grid(row=8, column=4, padx=15, pady=15)
        self.dooLogTitle.grid(row=8, column=4, padx=15, pady=15)
        self.aoorLogTitle.grid(row=8, column=4, padx=15, pady=15)
        self.voorLogTitle.grid(row=8, column=4, padx=15, pady=15)
        self.aairLogTitle.grid(row=8, column=4, padx=15, pady=15)
        self.vvirLogTitle.grid(row=8, column=4, padx=15, pady=15)
        self.doorLogTitle.grid(row=8, column=4, padx=15, pady=15)
        self.aooLog.grid(row=9, column=4, padx=15, pady=15)
        self.vooLog.grid(row=9, column=4, padx=15, pady=15)
        self.aaiLog.grid(row=9, column=4, padx=15, pady=15)
        self.vviLog.grid(row=9, column=4, padx=15, pady=15)
        self.dooLog.grid(row=9, column=4, padx=15, pady=15)
        self.aoorLog.grid(row=9, column=4, padx=15, pady=15)
        self.voorLog.grid(row=9, column=4, padx=15, pady=15)
        self.aairLog.grid(row=9, column=4, padx=15, pady=15)       
        self.vvirLog.grid(row=9, column=4, padx=15, pady=15)
        self.doorLog.grid(row=9, column=4, padx=15, pady=15)

        self.aooConfirmButton.grid(row=10, column=4)
        self.vooConfirmButton.grid(row=10, column=4)
        self.aaiConfirmButton.grid(row=10, column=4)
        self.vviConfirmButton.grid(row=10, column=4)
        self.dooConfirmButton.grid(row=10, column=4)
        self.aoorConfirmButton.grid(row=10, column=4)
        self.voorConfirmButton.grid(row=10, column=4)
        self.aairConfirmButton.grid(row=10, column=4)
        self.vvirConfirmButton.grid(row=10, column=4)
        self.doorConfirmButton.grid(row=10, column=4)

        self.aooLogoffButton.grid(row=11,column=4,pady=5)
        self.vooLogoffButton.grid(row=11,column=4,pady=5)
        self.aaiLogoffButton.grid(row=11,column=4,pady=5)
        self.vviLogoffButton.grid(row=11,column=4,pady=5)
        self.dooLogoffButton.grid(row=11,column=4,pady=5)
        self.aoorLogoffButton.grid(row=11,column=4,pady=5)
        self.voorLogoffButton.grid(row=11,column=4,pady=5)
        self.aairLogoffButton.grid(row=11,column=4,pady=5)
        self.vvirLogoffButton.grid(row=11,column=4,pady=5)
        self.doorLogoffButton.grid(row=11,column=4,pady=5)


        self.aooGraph = tk.Button(self.aoo, text = "Graph", command=lambda: self.DCMgraph("aoo"))
        self.vooGraph = tk.Button(self.voo, text = "Graph", command=lambda: self.DCMgraph("voo"))
        self.aaiGraph = tk.Button(self.aai, text = "Graph", command=lambda: self.DCMgraph("aai"))
        self.vviGraph = tk.Button(self.vvi, text = "Graph", command=lambda: self.DCMgraph("vvi"))
        self.dooGraph = tk.Button(self.doo, text = "Graph", command=lambda: self.DCMgraph("doo"))
        self.aoorGraph = tk.Button(self.aoor, text = "Graph", command=lambda: self.DCMgraph("aoor"))
        self.voorGraph = tk.Button(self.voor, text = "Graph", command=lambda: self.DCMgraph("voor"))
        self.aairGraph = tk.Button(self.aair, text = "Graph", command=lambda: self.DCMgraph("aair"))
        self.vvirGraph = tk.Button(self.vvir, text = "Graph", command=lambda: self.DCMgraph("vvir"))
        self.doorGraph = tk.Button(self.door, text = "Graph", command=lambda: self.DCMgraph("door"))
        
        self.aooGraph.grid(row=11,column=6,pady=5)
        self.vooGraph.grid(row=11,column=6,pady=5)
        self.aaiGraph.grid(row=11,column=6,pady=5)
        self.vviGraph.grid(row=11,column=6,pady=5)
        self.dooGraph.grid(row=11,column=6,pady=5)
        self.aoorGraph.grid(row=11,column=6,pady=5)
        self.voorGraph.grid(row=11,column=6,pady=5)
        self.aairGraph.grid(row=11,column=6,pady=5)
        self.vvirGraph.grid(row=11,column=6,pady=5)
        self.doorGraph.grid(row=11,column=6,pady=5)
    
    #Confirm changes method
    def confirmChanges(self,value):
        global currentuser
        if (value == "aooConfirm"):
            if messagebox.askyesno("CONFIRMATION", "Upload these changes?"):
                messagebox.showinfo("DONE", "Success")
                userlog = "AOO Was Uploaded"
                self.aooLog.config(text= userlog)
                self.vooLog.config(text= userlog)
                self.aaiLog.config(text= userlog)
                self.vviLog.config(text= userlog)
                self.dooLog.config(text= userlog)
                self.aoorLog.config(text= userlog)
                self.voorLog.config(text= userlog)
                self.aairLog.config(text= userlog)
                self.vvirLog.config(text= userlog)
                self.doorLog.config(text= userlog)
                db.execute("UPDATE "+currentuser+" SET userlog = ?", (userlog, ))
                db.commit()
        elif (value == "vooConfirm"):
            if messagebox.askyesno("CONFIRMATION", "Upload these changes?"):
                messagebox.showinfo("DONE", "Success")
                userlog = "VOO Was Uploaded"
                self.aooLog.config(text= userlog)
                self.vooLog.config(text= userlog)
                self.aaiLog.config(text= userlog)
                self.vviLog.config(text= userlog)
                self.dooLog.config(text= userlog)
                self.aoorLog.config(text= userlog)
                self.voorLog.config(text= userlog)
                self.aairLog.config(text= userlog)
                self.vvirLog.config(text= userlog)
                self.doorLog.config(text= userlog)
                db.execute("UPDATE "+currentuser+" SET userlog = ?", (userlog, ))
                db.commit()
        elif (value == "aaiConfirm"):
            if messagebox.askyesno("CONFIRMATION", "Upload these changes?"):
                messagebox.showinfo("DONE", "Success")
                userlog = "AAI Was Uploaded"
                self.aooLog.config(text= userlog)
                self.vooLog.config(text= userlog)
                self.aaiLog.config(text= userlog)
                self.vviLog.config(text= userlog)
                self.dooLog.config(text= userlog)
                self.aoorLog.config(text= userlog)
                self.voorLog.config(text= userlog)
                self.aairLog.config(text= userlog)
                self.vvirLog.config(text= userlog)
                self.doorLog.config(text= userlog)
                db.execute("UPDATE "+currentuser+" SET userlog = ?", (userlog, ))
                db.commit()
        elif (value == "vviConfirm"):
            if messagebox.askyesno("CONFIRMATION", "Upload these changes?"):
                messagebox.showinfo("DONE", "Success")
                userlog = "VVI Was Uploaded"
                self.aooLog.config(text= userlog)
                self.vooLog.config(text= userlog)
                self.aaiLog.config(text= userlog)
                self.vviLog.config(text= userlog)
                self.dooLog.config(text= userlog)
                self.aoorLog.config(text= userlog)
                self.voorLog.config(text= userlog)
                self.aairLog.config(text= userlog)
                self.vvirLog.config(text= userlog)
                self.doorLog.config(text= userlog)
                db.execute("UPDATE "+currentuser+" SET userlog = ?", (userlog, ))
                db.commit()
        elif (value == "dooConfirm"):
            if messagebox.askyesno("CONFIRMATION", "Upload these changes?"):
                messagebox.showinfo("DONE", "Success")
                userlog = "DOO Was Uploaded"
                self.aooLog.config(text= userlog)
                self.vooLog.config(text= userlog)
                self.aaiLog.config(text= userlog)
                self.vviLog.config(text= userlog)
                self.dooLog.config(text= userlog)
                self.aoorLog.config(text= userlog)
                self.voorLog.config(text= userlog)
                self.aairLog.config(text= userlog)
                self.vvirLog.config(text= userlog)
                self.doorLog.config(text= userlog)
                db.execute("UPDATE "+currentuser+" SET userlog = ?", (userlog, ))
                db.commit()
        elif (value == "aoorConfirm"):
            if messagebox.askyesno("CONFIRMATION", "Upload these changes?"):
                messagebox.showinfo("DONE", "Success")
                userlog = "AOOR Was Uploaded"
                self.aooLog.config(text= userlog)
                self.vooLog.config(text= userlog)
                self.aaiLog.config(text= userlog)
                self.vviLog.config(text= userlog)
                self.dooLog.config(text= userlog)
                self.aoorLog.config(text= userlog)
                self.voorLog.config(text= userlog)
                self.aairLog.config(text= userlog)
                self.vvirLog.config(text= userlog)
                self.doorLog.config(text= userlog)
                db.execute("UPDATE "+currentuser+" SET userlog = ?", (userlog, ))
                db.commit()
        elif (value == "voorConfirm"):
            if messagebox.askyesno("CONFIRMATION", "Upload these changes?"):
                messagebox.showinfo("DONE", "Success")
                userlog = "VOOR Was Uploaded"
                self.aooLog.config(text= userlog)
                self.vooLog.config(text= userlog)
                self.aaiLog.config(text= userlog)
                self.vviLog.config(text= userlog)
                self.dooLog.config(text= userlog)
                self.aoorLog.config(text= userlog)
                self.voorLog.config(text= userlog)
                self.aairLog.config(text= userlog)
                self.vvirLog.config(text= userlog)
                self.doorLog.config(text= userlog)
                db.execute("UPDATE "+currentuser+" SET userlog = ?", (userlog, ))
                db.commit()
        elif (value == "aairConfirm"):
            if messagebox.askyesno("CONFIRMATION", "Upload these changes?"):
                messagebox.showinfo("DONE", "Success")
                userlog = "AAIR Was Uploaded"
                self.aooLog.config(text= userlog)
                self.vooLog.config(text= userlog)
                self.aaiLog.config(text= userlog)
                self.vviLog.config(text= userlog)
                self.dooLog.config(text= userlog)
                self.aoorLog.config(text= userlog)
                self.voorLog.config(text= userlog)
                self.aairLog.config(text= userlog)
                self.vvirLog.config(text= userlog)
                self.doorLog.config(text= userlog)
                db.execute("UPDATE "+currentuser+" SET userlog = ?", (userlog, ))
                db.commit()
        elif (value == "vvirConfirm"):
            if messagebox.askyesno("CONFIRMATION", "Upload these changes?"):
                messagebox.showinfo("DONE", "Success")
                userlog = "VVIR Was Uploaded"
                self.aooLog.config(text= userlog)
                self.vooLog.config(text= userlog)
                self.aaiLog.config(text= userlog)
                self.vviLog.config(text= userlog)
                self.dooLog.config(text= userlog)
                self.aoorLog.config(text= userlog)
                self.voorLog.config(text= userlog)
                self.aairLog.config(text= userlog)
                self.vvirLog.config(text= userlog)
                self.doorLog.config(text= userlog)
                db.execute("UPDATE "+currentuser+" SET userlog = ?", (userlog, ))
                db.commit()
        elif (value == "doorConfirm"):
            if messagebox.askyesno("CONFIRMATION", "Upload these changes?"):
                messagebox.showinfo("DONE", "Success")
                userlog = "DOOR Was Uploaded"
                self.aooLog.config(text= userlog)
                self.vooLog.config(text= userlog)
                self.aaiLog.config(text= userlog)
                self.vviLog.config(text= userlog)
                self.dooLog.config(text= userlog)
                self.aoorLog.config(text= userlog)
                self.voorLog.config(text= userlog)
                self.aairLog.config(text= userlog)
                self.vvirLog.config(text= userlog)
                self.doorLog.config(text= userlog)
                db.execute("UPDATE "+currentuser+" SET userlog = ?", (userlog, ))
                db.commit()
        
    #Method to set value
    def setValue(self,value):
        #Global Variables
        #AOO
        global aoo_lowerRateLimitEntry,aoo_upperRateLimitEntry,aoo_atrialAmplitudeEntry,aoo_atrialPulseWidthEntry 
        #VOO
        global voo_lowerRateLimitEntry,voo_upperRateLimitEntry,voo_ventricularAmplitudeEntry,voo_ventricularPulseWidthEntry
        #AAI
        global aai_lowerRateLimitEntry,aai_upperRateLimitEntry,aai_atrialAmplitudeEntry,aai_atrialPulseWidthEntry,aai_atrialSensitivityEntry,aai_ARPEntry,aai_PVARPEntry,aai_hysteresisEntry,aai_rateSmoothingEntry
        #VVI
        global vvi_lowerRateLimitEntry,vvi_upperRateLimitEntry,vvi_ventricularAmplitudeEntry,vvi_ventricularPulseWidthEntry,vvi_ventricularSensitivityEntry,vvi_VRPEntry,vvi_hysteresisEntry,vvi_rateSmoothingEntry
        #DOO
        global doo_lowerRateLimitEntry,doo_upperRateLimitEntry,doo_atrialAmplitudeEntry,doo_atrialPulseWidthEntry,doo_ventricularAmplitudeEntry,doo_ventricularPulseWidthEntry,doo_fixedAVDelayEntry

        #AOOR
        global aoor_lowerRateLimitEntry, aoor_upperRateLimitEntry, aoor_atrialAmplitudeEntry, aoor_atrialPulseWidthEntry, aoor_maximumSensorRateEntry, aoor_activityThresholdEntry, aoor_reactionTimeEntry, aoor_responseFactorEntry, aoor_recoveryTimeEntry
        #VOOR
        global voor_lowerRateLimitEntry, voor_upperRateLimitEntry, voor_ventricularAmplitudeEntry, voor_ventricularPulseWidthEntry, voor_maximumSensorRateEntry, voor_activityThresholdEntry, voor_reactionTimeEntry, voor_responseFactorEntry, voor_recoveryTimeEntry
        #AAIR
        global aair_lowerRateLimitEntry, aair_upperRateLimitEntry, aair_atrialAmplitudeEntry, aair_atrialPulseWidthEntry, aair_atrialSensitivityEntry, aair_ARPEntry, aair_PVARPEntry, aair_hysteresisEntry, aair_rateSmoothingEntry, aair_maximumSensorRateEntry, aair_activityThresholdEntry, aair_reactionTimeEntry, aair_responseFactorEntry, aair_recoveryTimeEntry
        #VVIR
        global vvir_lowerRateLimitEntry, vvir_upperRateLimitEntry, vvir_ventricularAmplitudeEntry, vvir_ventricularPulseWidthEntry, vvir_ventricularSensitivityEntry, vvir_VRPEntry, vvir_hysteresisEntry, vvir_rateSmoothingEntry, vvir_maximumSensorRateEntry, vvir_activityThresholdEntry, vvir_reactionTimeEntry, vvir_responseFactorEntry, vvir_recoveryTimeEntry
        #DOOR
        global door_lowerRateLimitEntry, door_upperRateLimitEntry, door_atrialAmplitudeEntry, door_atrialPulseWidthEntry, door_ventricularAmplitudeEntry, door_ventricularPulseWidthEntry, door_maximumSensorRateEntry, door_fixedAVDelayEntry, door_activityThresholdEntry, door_reactionTimeEntry, door_responseFactorEntry, door_recoveryTimeEntry

        #Currentuser
        global currentuser

        #AOO BEGIN-----------------------------------------------------------------------------------------------------------------------------
        #aooLowerRateLimit
        if(value == "aooLowerRateLimit"):
            temp = self.aooLowerRateLimitEntry.get()
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                int(temp)
                if (temp == '' or int(temp)<0):
                    messagebox.showinfo("ERROR","Please enter a valid value")
                    pass

                #Ensure upper limit is larger than lower limit
                elif(int(self.aooLowerRateLimitEntry.get()) >= int(aoo_upperRateLimitEntry) and int(aoo_upperRateLimitEntry) != 0 ):
                    messagebox.showinfo("ERROR","Please ensure your lower rate limit is lower than your upper rate limit")
                    pass

                #Ensure value is in limited range
                elif(int(temp) < 30 or int(temp) > 175):
                    messagebox.showinfo("ERROR","The range is between 30 and 175")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("CONFIRMATION", "Replace current value?"):
                        messagebox.showinfo("DONE", "Success")
                        aoo_lowerRateLimitEntry = temp
                        self.aooLowerRateLimitValue.config(text="Current Value: " + aoo_lowerRateLimitEntry)
                        db.execute("UPDATE "+currentuser+" SET aoo_lowerRateLimitEntry = ?", (aoo_lowerRateLimitEntry,))
                        db.commit()

            except Exception as e:
                print(e)
                messagebox.showinfo("ERROR","Please enter a valid value")
                pass

        #aooUpperRateLimit
        if(value == "aooUpperRateLimit"):
            temp = self.aooUpperRateLimitEntry.get()
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                int(temp)
                if (temp == '' or int(temp)<0):
                    messagebox.showinfo("ERROR","Please enter a valid value")
                    pass

                #Ensure upper limit is larger than lower limit
                elif(int(aoo_lowerRateLimitEntry) >= int(self.aooUpperRateLimitEntry.get()) and int(aoo_lowerRateLimitEntry) != 0 ):
                    messagebox.showinfo("ERROR","Please ensure your upper rate limit is higher than your lower rate limit")
                    pass

                #Ensure value is in limited range
                elif(int(temp) < 50 or int(temp) > 175):
                    messagebox.showinfo("ERROR","The range is between 50 and 175")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("CONFIRMATION", "Replace current value?"):
                        messagebox.showinfo("DONE", "Success")
                        aoo_upperRateLimitEntry = temp
                        self.aooUpperRateLimitValue.config(text="Current Value: " + aoo_upperRateLimitEntry)
                        db.execute("UPDATE "+currentuser+" SET aoo_upperRateLimitEntry = ?", (aoo_upperRateLimitEntry,))
                        db.commit()

            except:
                messagebox.showinfo("ERROR","Please enter a valid value")
                pass

        #aooAtrialAmplitude
        if(value == "aooAtrialAmplitude"):
            temp = self.aooAtrialAmplitudeEntry.get()
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                float(temp)
                if (temp == '' or float(temp)<0):
                    messagebox.showinfo("ERROR","Please enter a valid value")
                    pass
                #Ensure value is in limited range
                elif(float(temp) < 0 or float(temp) > 7.0):
                    messagebox.showinfo("ERROR","The range is between 0(off) and 7.0")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("CONFIRMATION", "Replace current value?"):
                        messagebox.showinfo("DONE", "Success")
                        aoo_atrialAmplitudeEntry = temp
                        self.aooAtrialAmplitudeValue.config(text="Current Value: " + aoo_atrialAmplitudeEntry)
                        db.execute("UPDATE "+currentuser+" SET aoo_atrialAmplitudeEntry = ?", (aoo_atrialAmplitudeEntry,))
                        db.commit()

            except:
                messagebox.showinfo("ERROR","Please enter a valid value")
                pass

        #aooAtrialPulseWidth
        if(value == "aooAtrialPulseWidth"):
            temp = self.aooAtrialPulseWidthEntry.get()
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                float(temp)
                if (temp == '' or float(temp)<0):
                    messagebox.showinfo("ERROR","Please enter a valid value")
                    pass

                #Ensure value is in limited range
                elif(float(temp) < 0.05 or float(temp) > 1.9):
                    messagebox.showinfo("ERROR","The range is between 0.05 and 1.9")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("CONFIRMATION", "Replace current value?"):
                        messagebox.showinfo("DONE", "Success")
                        aoo_atrialPulseWidthEntry = temp
                        self.aooAtrialPulseWidthValue.config(text="Current Value: " + aoo_atrialPulseWidthEntry)
                        db.execute("UPDATE "+currentuser+" SET aoo_atrialPulseWidthEntry = ?", (aoo_atrialPulseWidthEntry,))
                        db.commit()

            except:
                messagebox.showinfo("ERROR","Please enter a valid value")
                pass
        #AOO END-------------------------------------------------------------------------------------------------------------------------------

        #VOO BEGIN-----------------------------------------------------------------------------------------------------------------------------
        #vooLowerRateLimit
        if(value == "vooLowerRateLimit"):
            temp = self.vooLowerRateLimitEntry.get()
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                int(temp)
                if (temp == '' or int(temp)<0):
                    messagebox.showinfo("ERROR","Please enter a valid value")
                    pass

                #Ensure upper limit is larger than lower limit
                elif(int(self.vooLowerRateLimitEntry.get()) >= int(voo_upperRateLimitEntry) and int(voo_upperRateLimitEntry) != 0 ):
                    messagebox.showinfo("ERROR","Please ensure your lower rate limit is lower than your upper rate limit")
                    pass

                #Ensure value is in limited range
                elif(int(temp) < 30 or int(temp) > 175):
                    messagebox.showinfo("ERROR","The range is between 30 and 175")
                    pass
                
                #If everything is good update current value
                else:
                    if messagebox.askyesno("CONFIRMATION", "Replace current value?"):
                        messagebox.showinfo("DONE", "Success")
                        voo_lowerRateLimitEntry = temp
                        self.vooLowerRateLimitValue.config(text="Current Value: " + voo_lowerRateLimitEntry)
                        db.execute("UPDATE "+currentuser+" SET voo_lowerRateLimitEntry = ?", (voo_lowerRateLimitEntry,))
                        db.commit()
                        
            except:
                messagebox.showinfo("ERROR","Please enter a valid value")
                pass
        
        #vooUpperRateLimit
        if(value == "vooUpperRateLimit"):
            temp = self.vooUpperRateLimitEntry.get()
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                int(temp)
                if (temp == '' or int(temp)<0):
                    messagebox.showinfo("ERROR","Please enter a valid value")
                    pass

                #Ensure upper limit is larger than lower limit
                elif(int(voo_lowerRateLimitEntry) >= int(self.vooUpperRateLimitEntry.get()) and int(voo_lowerRateLimitEntry) != 0 ):
                    messagebox.showinfo("ERROR","Please ensure your upper rate limit is higher than your lower rate limit")
                    pass

                #Ensure value is in limited range
                elif(int(temp) < 50 or int(temp) > 175):
                    messagebox.showinfo("ERROR","The range is between 50 and 175")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("CONFIRMATION", "Replace current value?"):
                        messagebox.showinfo("DONE", "Success")
                        voo_upperRateLimitEntry = temp
                        self.vooUpperRateLimitValue.config(text="Current Value: " + voo_upperRateLimitEntry)
                        db.execute("UPDATE "+currentuser+" SET voo_upperRateLimitEntry = ?", (voo_upperRateLimitEntry,))
                        db.commit()

            except:
                messagebox.showinfo("ERROR","Please enter a valid value")
                pass

        #vooVentricularAmplitude
        if(value == "vooVentricularAmplitude"):
            temp = self.vooVentricularAmplitudeEntry.get()
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                float(temp)
                if (temp == '' or float(temp)<0):
                    messagebox.showinfo("ERROR","Please enter a valid value")
                    pass

                #Ensure value is in limited range
                elif(float(temp) < 0 or float(temp) > 7.0):
                    messagebox.showinfo("ERROR","The range is between 0(off) and 7.0")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("CONFIRMATION", "Replace current value?"):
                        messagebox.showinfo("DONE", "Success")
                        voo_ventricularAmplitudeEntry = temp
                        self.vooVentricularAmplitudeValue.config(text="Current Value: " + voo_ventricularAmplitudeEntry)
                        db.execute("UPDATE "+currentuser+" SET voo_ventricularAmplitudeEntry = ?", (voo_ventricularAmplitudeEntry,))
                        db.commit()

            except:
                messagebox.showinfo("ERROR","Please enter a valid value")
                pass

        #vooVentricularPulseWidth
        if(value == "vooVentricularPulseWidth"):
            temp = self.vooVentricularPulseWidthEntry.get()
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                float(temp)
                if (temp == '' or float(temp)<0):
                    messagebox.showinfo("ERROR","Please enter a valid value")
                    pass

                #Ensure value is in limited range
                elif(float(temp) < 0.05 or float(temp) > 1.9):
                    messagebox.showinfo("ERROR","The range is between 0.05 and 1.9")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("CONFIRMATION", "Replace current value?"):
                        messagebox.showinfo("DONE", "Success")
                        voo_ventricularPulseWidthEntry = temp
                        self.vooVentricularPulseWidthValue.config(text="Current Value: " + voo_ventricularPulseWidthEntry)
                        db.execute("UPDATE "+currentuser+" SET voo_ventricularPulseWidthEntry = ?", (voo_ventricularPulseWidthEntry,))
                        db.commit()

            except:
                messagebox.showinfo("ERROR","Please enter a valid value")
                pass
        #VOO END-------------------------------------------------------------------------------------------------------------------------------

        #AAI BEGIN-----------------------------------------------------------------------------------------------------------------------------
        #aaiLowerRateLimit
        if(value == "aaiLowerRateLimit"):
            temp = self.aaiLowerRateLimitEntry.get()
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                int(temp)
                if (temp == '' or int(temp)<0):
                    messagebox.showinfo("ERROR","Please enter a valid value")
                    pass
                #Ensure upper limit is larger than lower limit
                elif(int(self.aaiLowerRateLimitEntry.get()) >= int(aai_upperRateLimitEntry) and int(aai_upperRateLimitEntry) != 0 ):
                    messagebox.showinfo("ERROR","Please ensure your lower rate limit is lower than your upper rate limit")
                    pass

                #Ensure value is in limited range
                elif(int(temp) < 30 or int(temp) > 175):
                    messagebox.showinfo("ERROR","The range is between 30 and 175")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("CONFIRMATION", "Replace current value?"):
                        messagebox.showinfo("DONE", "Success")
                        aai_lowerRateLimitEntry = temp
                        self.aaiLowerRateLimitValue.config(text="Current Value: " + aai_lowerRateLimitEntry)
                        db.execute("UPDATE "+currentuser+" SET aai_lowerRateLimitEntry = ?", (aai_lowerRateLimitEntry,))
                        db.commit()

            except:
                messagebox.showinfo("ERROR","Please enter a valid value")
                pass

        #aaiUpperRateLimit
        if(value == "aaiUpperRateLimit"):
            temp = self.aaiUpperRateLimitEntry.get()
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                int(temp)
                if (temp == '' or int(temp)<0):
                    messagebox.showinfo("ERROR","Please enter a valid value")
                    pass
                #Ensure upper limit is larger than lower limit
                elif(int(aai_lowerRateLimitEntry) >= int(self.aaiUpperRateLimitEntry.get()) and int(aai_lowerRateLimitEntry) != 0 ):
                    messagebox.showinfo("ERROR","Please ensure your upper rate limit is higher than your lower rate limit")
                    pass

                #Ensure value is in limited range
                elif(int(temp) < 50 or int(temp) > 175):
                    messagebox.showinfo("ERROR","The range is between 50 and 175")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("CONFIRMATION", "Replace current value?"):
                        messagebox.showinfo("DONE", "Success")
                        aai_upperRateLimitEntry = temp
                        self.aaiUpperRateLimitValue.config(text="Current Value: " + aai_upperRateLimitEntry)
                        db.execute("UPDATE "+currentuser+" SET aai_upperRateLimitEntry = ?", (aai_upperRateLimitEntry,))
                        db.commit()

            except:
                messagebox.showinfo("ERROR","Please enter a valid value")
                pass

        #aaiAtrialAmplitude
        if(value == "aaiAtrialAmplitude"):
            temp = self.aaiAtrialAmplitudeEntry .get()
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                float(temp)
                if (temp == '' or float(temp)<0):
                    messagebox.showinfo("ERROR","Please enter a valid value")
                    pass

                #Ensure value is in limited range
                elif(float(temp) < 0 or float(temp) > 7.0):
                    messagebox.showinfo("ERROR","The range is between 0(off) and 7.0")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("CONFIRMATION", "Replace current value?"):
                        messagebox.showinfo("DONE", "Success")
                        aai_atrialAmplitudeEntry  = temp
                        self.aaiAtrialAmplitudeValue.config(text="Current Value: " + aai_atrialAmplitudeEntry)
                        db.execute("UPDATE "+currentuser+" SET aai_atrialAmplitudeEntry = ?", (aai_atrialAmplitudeEntry,))
                        db.commit()

            except:
                messagebox.showinfo("ERROR","Please enter a valid value")
                pass

        #aaiAtrialPulseWidth
        if(value == "aaiAtrialPulseWidth"):
            temp = self.aaiAtrialPulseWidthEntry.get()
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                float(temp)
                if (temp == '' or float(temp)<0):
                    messagebox.showinfo("ERROR","Please enter a valid value")
                    pass

                #Ensure value is in limited range
                elif(float(temp) < 0.05 or float(temp) > 1.9):
                    messagebox.showinfo("ERROR","The range is between 0.05 and 1.9")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("CONFIRMATION", "Replace current value?"):
                        messagebox.showinfo("DONE", "Success")
                        aai_atrialPulseWidthEntry = temp
                        self.aaiAtrialPulseWidthValue.config(text="Current Value: " + aai_atrialPulseWidthEntry)
                        db.execute("UPDATE "+currentuser+" SET aai_atrialPulseWidthEntry = ?", (aai_atrialPulseWidthEntry,))
                        db.commit()

            except:
                messagebox.showinfo("ERROR","Please enter a valid value")
                pass

        #aaiAtrialSensitivity
        if(value == "aaiAtrialSensitivity"):
            temp = self.aaiAtrialSensitivityEntry.get()
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                float(temp)
                if (temp == '' or float(temp)<0):
                    messagebox.showinfo("ERROR","Please enter a valid value")
                    pass

                #Ensure value is in limited range
                elif(float(temp) < 0.25 or float(temp) > 10.0):
                    messagebox.showinfo("ERROR","The range is between 0.25 and 10.0")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("CONFIRMATION", "Replace current value?"):
                        messagebox.showinfo("DONE", "Success")
                        aai_atrialSensitivityEntry = temp
                        self.aaiAtrialSensitivityValue.config(text="Current Value: " + aai_atrialSensitivityEntry)
                        db.execute("UPDATE "+currentuser+" SET aai_atrialSensitivityEntry = ?", (aai_atrialSensitivityEntry,))
                        db.commit()

            except:
                messagebox.showinfo("ERROR","Please enter a valid value")
                pass

        #aaiARP
        if(value == "aaiARP"):
            temp = self.aaiARPEntry.get()
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                int(temp)
                if (temp == '' or int(temp)<0):
                    messagebox.showinfo("ERROR","Please enter a valid value")
                    pass

                #Ensure value is in limited range
                elif(int(temp) < 150 or int(temp) > 500):
                    messagebox.showinfo("ERROR","The range is between 150 and 500")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("CONFIRMATION", "Replace current value?"):
                        messagebox.showinfo("DONE", "Success")
                        aai_ARPEntry = temp
                        self.aaiARPValue.config(text="Current Value: " + aai_ARPEntry)
                        db.execute("UPDATE "+currentuser+" SET aai_ARPEntry = ?", (aai_ARPEntry,))
                        db.commit()

            except:
                messagebox.showinfo("ERROR","Please enter a valid value")
                pass

        #aaiPVARP
        if(value == "aaiPVARP"):
            temp = self.aaiPVARPEntry.get()
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                int(temp)
                if (temp == '' or int(temp)<0):
                    messagebox.showinfo("ERROR","Please enter a valid value")
                    pass

                #Ensure value is in limited range
                elif(int(temp) < 150 or int(temp) > 500):
                    messagebox.showinfo("ERROR","The range is between 150 and 500")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("CONFIRMATION", "Replace current value?"):
                        messagebox.showinfo("DONE", "Success")
                        aai_PVARPEntry = temp
                        self.aaiPVARPValue.config(text="Current Value: " + aai_PVARPEntry)
                        db.execute("UPDATE "+currentuser+" SET aai_PVARPEntry = ?", (aai_PVARPEntry,))
                        db.commit()

            except:
                messagebox.showinfo("ERROR","Please enter a valid value")
                pass

        #aaiHysteresis
        if(value == "aaiHysteresis"):
            temp = self.aaiHysteresisEntry.get()
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                int(temp)
                if (temp == '' or int(temp)<0):
                    messagebox.showinfo("ERROR","Please enter a valid value")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("CONFIRMATION", "Replace current value?"):
                        messagebox.showinfo("DONE", "Success")
                        aai_hysteresisEntry = temp
                        self.aaiHysteresisValue.config(text="Current Value: " + aai_hysteresisEntry)
                        db.execute("UPDATE "+currentuser+" SET aai_hysteresisEntry = ?", (aai_hysteresisEntry,))
                        db.commit()

            except:
                messagebox.showinfo("ERROR","Please enter a valid value")
                pass

        #aaiRateSmoothing
        if(value == "aaiRateSmoothing"):
            temp = self.aaiRateSmoothingEntry.get()
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                int(temp)
                if (temp == '' or int(temp)<0):
                    messagebox.showinfo("ERROR","Please enter a valid value")
                    pass

                #Ensure value is in limited range
                elif(int(temp) < 0 or int(temp) > 25):
                    messagebox.showinfo("ERROR","The range is between 0(off) and 25")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("CONFIRMATION", "Replace current value?"):
                        messagebox.showinfo("DONE", "Success")
                        aai_rateSmoothingEntry = temp
                        self.aaiRateSmoothingValue.config(text="Current Value: " + aai_rateSmoothingEntry)
                        db.execute("UPDATE "+currentuser+" SET aai_rateSmoothingEntry = ?", (aai_rateSmoothingEntry,))
                        db.commit()

            except:
                messagebox.showinfo("ERROR","Please enter a valid value")
                pass
        #AAI END-------------------------------------------------------------------------------------------------------------------------------
        
        #VVI BEGIN-----------------------------------------------------------------------------------------------------------------------------
        #vviLowerRateLimit
        if(value == "vviLowerRateLimit"):
            temp = self.vviLowerRateLimitEntry.get()
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                int(temp)
                if (temp == '' or int(temp)<0):
                    messagebox.showinfo("ERROR","Please enter a valid value")
                    pass

                #Ensure upper limit is larger than lower limit
                elif(int(self.vviLowerRateLimitEntry.get()) >= int(vvi_upperRateLimitEntry) and int(vvi_upperRateLimitEntry) != 0 ):
                    messagebox.showinfo("ERROR","Please ensure your lower rate limit is lower than your upper rate limit")
                    pass

                #Ensure value is in limited range
                elif(int(temp) < 30 or int(temp) > 175):
                    messagebox.showinfo("ERROR","The range is between 30 and 175")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("CONFIRMATION", "Replace current value?"):
                        messagebox.showinfo("DONE", "Success")
                        vvi_lowerRateLimitEntry = temp
                        self.vviLowerRateLimitValue.config(text="Current Value: " + vvi_lowerRateLimitEntry)
                        db.execute("UPDATE "+currentuser+" SET vvi_lowerRateLimitEntry = ?", (vvi_lowerRateLimitEntry,))
                        db.commit()

            except:
                messagebox.showinfo("ERROR","Please enter a valid value")
                pass

        #vviUpperRateLimit
        if(value == "vviUpperRateLimit"):
            temp = self.vviUpperRateLimitEntry.get() 
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                int(temp)
                if (temp == '' or int(temp)<0):
                    messagebox.showinfo("ERROR","Please enter a valid value")
                    pass

                #Ensure upper limit is larger than lower limit
                elif(int(vvi_lowerRateLimitEntry) >= int(self.vviUpperRateLimitEntry.get()) and int(vvi_lowerRateLimitEntry) != 0 ):
                    messagebox.showinfo("ERROR","Please ensure your upper rate limit is higher than your lower rate limit")
                    pass

                #Ensure value is in limited range
                elif(int(temp) < 50 or int(temp) > 175):
                    messagebox.showinfo("ERROR","The range is between 50 and 175")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("CONFIRMATION", "Replace current value?"):
                        messagebox.showinfo("DONE", "Success")
                        vvi_upperRateLimitEntry = temp
                        self.vviUpperRateLimitValue.config(text="Current Value: " + vvi_upperRateLimitEntry)
                        db.execute("UPDATE "+currentuser+" SET vvi_upperRateLimitEntry = ?", (vvi_upperRateLimitEntry,))
                        db.commit()

            except:
                messagebox.showinfo("ERROR","Please enter a valid value")
                pass

        #vviVentricularAmplitude
        if(value == "vviVentricularAmplitude"):
            temp = self.vviVentricularAmplitudeEntry.get() 
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                float(temp)
                if (temp == '' or float(temp)<0):
                    messagebox.showinfo("ERROR","Please enter a valid value")
                    pass

                #Ensure value is in limited range
                elif(float(temp) < 0 or float(temp) > 7.0):
                    messagebox.showinfo("ERROR","The range is between 0(off) and 7.0")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("CONFIRMATION", "Replace current value?"):
                        messagebox.showinfo("DONE", "Success")
                        vvi_ventricularAmplitudeEntry = temp
                        self.vviVentricularAmplitudeValue.config(text="Current Value: " + vvi_ventricularAmplitudeEntry)
                        db.execute("UPDATE "+currentuser+" SET vvi_ventricularAmplitudeEntry = ?", (vvi_ventricularAmplitudeEntry,))
                        db.commit()

            except:
                messagebox.showinfo("ERROR","Please enter a valid value")
                pass

        #vviVentricularPulseWidth
        if(value == "vviVentricularPulseWidth"):
            temp = self.vviVentricularPulseWidthEntry.get() 
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                float(temp)
                if (temp == '' or float(temp)<0):
                    messagebox.showinfo("ERROR","Please enter a valid value")
                    pass

                #Ensure value is in limited range
                elif(float(temp) < 0.05 or float(temp) > 1.9):
                    messagebox.showinfo("ERROR","The range is between 0.05 and 1.9")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("CONFIRMATION", "Replace current value?"):
                        messagebox.showinfo("DONE", "Success")
                        vvi_ventricularPulseWidthEntry = temp
                        self.vviVentricularPulseWidthValue.config(text="Current Value: " + vvi_ventricularPulseWidthEntry)
                        db.execute("UPDATE "+currentuser+" SET vvi_ventricularPulseWidthEntry = ?", (vvi_ventricularPulseWidthEntry,))
                        db.commit()

            except:
                messagebox.showinfo("ERROR","Please enter a valid value")
                pass

        #vviVentricularSensitivity
        if(value == "vviVentricularSensitivity"):
            temp = self.vviVentricularSensitivityEntry.get()
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                float(temp)
                if (temp == '' or float(temp)<0):
                    messagebox.showinfo("ERROR","Please enter a valid value")
                    pass

                #Ensure value is in limited range
                elif(float(temp) < 0.25 or float(temp) > 10.0):
                    messagebox.showinfo("ERROR","The range is between 0.25 and 10.0")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("CONFIRMATION", "Replace current value?"):
                        messagebox.showinfo("DONE", "Success")
                        vvi_ventricularSensitivityEntry = temp
                        self.vviVentricularSensitivityValue.config(text="Current Value: " + vvi_ventricularSensitivityEntry)
                        db.execute("UPDATE "+currentuser+" SET vvi_ventricularSensitivityEntry = ?", (vvi_ventricularSensitivityEntry,))
                        db.commit()

            except:
                messagebox.showinfo("ERROR","Please enter a valid value")
                pass

        #vviVRP
        if(value == "vviVRP"):
            temp = self.vviVRPEntry.get() 
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                int(temp)
                if (temp == '' or int(temp)<0):
                    messagebox.showinfo("ERROR","Please enter a valid value")
                    pass

                #Ensure value is in limited range
                elif(int(temp) < 150 or int(temp) > 500):
                    messagebox.showinfo("ERROR","The range is between 150 and 500")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("CONFIRMATION", "Replace current value?"):
                        messagebox.showinfo("DONE", "Success")
                        vvi_VRPEntry = temp
                        self.vviVRPValue.config(text="Current Value: " + vvi_VRPEntry)
                        db.execute("UPDATE "+currentuser+" SET vvi_VRPEntry = ?", (vvi_VRPEntry,))
                        db.commit()

            except:
                messagebox.showinfo("ERROR","Please enter a valid value")
                pass

        #vviHysteresis
        if(value == "vviHysteresis"):
            temp = self.vviHysteresisEntry.get() 
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                int(temp)
                if (temp == '' or int(temp)<0):
                    messagebox.showinfo("ERROR","Please enter a valid value")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("CONFIRMATION", "Replace current value?"):
                        messagebox.showinfo("DONE", "Success")
                        vvi_hysteresisEntry = temp
                        self.vviHysteresisValue.config(text="Current Value: " + vvi_hysteresisEntry)
                        db.execute("UPDATE "+currentuser+" SET vvi_hysteresisEntry = ?", (vvi_hysteresisEntry,))
                        db.commit()

            except:
                messagebox.showinfo("ERROR","Please enter a valid value")
                pass

        #vviRateSmoothing
        if(value == "vviRateSmoothing"):
            temp = self.vviRateSmoothingEntry.get()
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                int(temp)
                if (temp == '' or int(temp)<0):
                    messagebox.showinfo("ERROR","Please enter a valid value")
                    pass

                #Ensure value is in limited range
                elif(int(temp) < 0 or int(temp) > 25):
                    messagebox.showinfo("ERROR","The range is between 0(off) and 25")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("CONFIRMATION", "Replace current value?"):
                        messagebox.showinfo("DONE", "Success")
                        vvi_rateSmoothingEntry = temp
                        self.vviRateSmoothingValue.config(text="Current Value: " + vvi_rateSmoothingEntry)
                        db.execute("UPDATE "+currentuser+" SET vvi_rateSmoothingEntry = ?", (vvi_rateSmoothingEntry,))
                        db.commit()

            except:
                messagebox.showinfo("ERROR","Please enter a valid value")
                pass
        #VVI END-------------------------------------------------------------------------------------------------------------------------------

        #DOO BEGIN-----------------------------------------------------------------------------------------------------------------------------
        #dooLowerRateLimit
        if(value == "dooLowerRateLimit"):
            temp = self.dooLowerRateLimitEntry.get()
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                int(temp)
                if (temp == '' or int(temp)<0):
                    messagebox.showinfo("ERROR","Please enter a valid value")
                    pass

                #Ensure upper limit is larger than lower limit
                elif(int(self.dooLowerRateLimitEntry.get()) >= int(doo_upperRateLimitEntry) and int(doo_upperRateLimitEntry) != 0 ):
                    messagebox.showinfo("ERROR","Please ensure your lower rate limit is lower than your upper rate limit")
                    pass

                #Ensure value is in limited range
                elif(int(temp) < 30 or int(temp) > 175):
                    messagebox.showinfo("ERROR","The range is between 30 and 175")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("CONFIRMATION", "Replace current value?"):
                        messagebox.showinfo("DONE", "Success")
                        doo_lowerRateLimitEntry = temp
                        self.dooLowerRateLimitValue.config(text="Current Value: " + doo_lowerRateLimitEntry)
                        db.execute("UPDATE "+currentuser+" SET doo_lowerRateLimitEntry = ?", (doo_lowerRateLimitEntry,))
                        db.commit()

            except:
                messagebox.showinfo("ERROR","Please enter a valid value")
                pass

        #dooUpperRateLimit
        if(value == "dooUpperRateLimit"):
            temp = self.dooUpperRateLimitEntry.get()
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                int(temp)
                if (temp == '' or int(temp)<0):
                    messagebox.showinfo("ERROR","Please enter a valid value")
                    pass

                #Ensure upper limit is larger than lower limit
                elif(int(doo_lowerRateLimitEntry) >= int(self.dooUpperRateLimitEntry.get()) and int(doo_lowerRateLimitEntry) != 0 ):
                    messagebox.showinfo("ERROR","Please ensure your upper rate limit is higher than your lower rate limit")
                    pass

                #Ensure value is in limited range
                elif(int(temp) < 50 or int(temp) > 175):
                    messagebox.showinfo("ERROR","The range is between 50 and 175")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("CONFIRMATION", "Replace current value?"):
                        messagebox.showinfo("DONE", "Success")
                        doo_upperRateLimitEntry = temp
                        self.dooUpperRateLimitValue.config(text="Current Value: " + doo_upperRateLimitEntry)
                        db.execute("UPDATE "+currentuser+" SET doo_upperRateLimitEntry = ?", (doo_upperRateLimitEntry,))
                        db.commit()

            except:
                messagebox.showinfo("ERROR","Please enter a valid value")
                pass

        #dooAtrialAmplitude
        if(value == "dooAtrialAmplitude"):
            temp = self.dooAtrialAmplitudeEntry.get()
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                float(temp)
                if (temp == '' or float(temp)<0):
                    messagebox.showinfo("ERROR","Please enter a valid value")
                    pass
                #Ensure value is in limited range
                elif(float(temp) < 0 or float(temp) > 7.0):
                    messagebox.showinfo("ERROR","The range is between 0(off) and 7.0")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("CONFIRMATION", "Replace current value?"):
                        messagebox.showinfo("DONE", "Success")
                        doo_atrialAmplitudeEntry = temp
                        self.dooAtrialAmplitudeValue.config(text="Current Value: " + doo_atrialAmplitudeEntry)
                        db.execute("UPDATE "+currentuser+" SET doo_atrialAmplitudeEntry = ?", (doo_atrialAmplitudeEntry,))
                        db.commit()

            except:
                messagebox.showinfo("ERROR","Please enter a valid value")
                pass

        #dooAtrialPulseWidth
        if(value == "dooAtrialPulseWidth"):
            temp = self.dooAtrialPulseWidthEntry.get()
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                float(temp)
                if (temp == '' or float(temp)<0):
                    messagebox.showinfo("ERROR","Please enter a valid value")
                    pass

                #Ensure value is in limited range
                elif(float(temp) < 0.05 or float(temp) > 1.9):
                    messagebox.showinfo("ERROR","The range is between 0.05 and 1.9")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("CONFIRMATION", "Replace current value?"):
                        messagebox.showinfo("DONE", "Success")
                        doo_atrialPulseWidthEntry = temp
                        self.dooAtrialPulseWidthValue.config(text="Current Value: " + doo_atrialPulseWidthEntry)
                        db.execute("UPDATE "+currentuser+" SET doo_atrialPulseWidthEntry = ?", (doo_atrialPulseWidthEntry,))
                        db.commit()

            except:
                messagebox.showinfo("ERROR","Please enter a valid value")
                pass
        
        #dooVentricularAmplitude
        if(value == "dooVentricularAmplitude"):
            temp = self.dooVentricularAmplitudeEntry.get()
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                float(temp)
                if (temp == '' or float(temp)<0):
                    messagebox.showinfo("ERROR","Please enter a valid value")
                    pass

                #Ensure value is in limited range
                elif(float(temp) < 0 or float(temp) > 7.0):
                    messagebox.showinfo("ERROR","The range is between 0(off) and 7.0")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("CONFIRMATION", "Replace current value?"):
                        messagebox.showinfo("DONE", "Success")
                        doo_ventricularAmplitudeEntry = temp
                        self.dooVentricularAmplitudeValue.config(text="Current Value: " + doo_ventricularAmplitudeEntry)
                        db.execute("UPDATE "+currentuser+" SET doo_ventricularAmplitudeEntry = ?", (doo_ventricularAmplitudeEntry,))
                        db.commit()

            except:
                messagebox.showinfo("ERROR","Please enter a valid value")
                pass

        #dooVentricularPulseWidth
        if(value == "dooVentricularPulseWidth"):
            temp = self.dooVentricularPulseWidthEntry.get()
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                float(temp)
                if (temp == '' or float(temp)<0):
                    messagebox.showinfo("ERROR","Please enter a valid value")
                    pass

                #Ensure value is in limited range
                elif(float(temp) < 0.05 or float(temp) > 1.9):
                    messagebox.showinfo("ERROR","The range is between 0.05 and 1.9")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("CONFIRMATION", "Replace current value?"):
                        messagebox.showinfo("DONE", "Success")
                        doo_ventricularPulseWidthEntry = temp
                        self.dooVentricularPulseWidthValue.config(text="Current Value: " + doo_ventricularPulseWidthEntry)
                        db.execute("UPDATE "+currentuser+" SET doo_ventricularPulseWidthEntry = ?", (doo_ventricularPulseWidthEntry,))
                        db.commit()

            except:
                messagebox.showinfo("ERROR","Please enter a valid value")
                pass
        
        #dooFixedAVDelay
        if(value == "dooFixedAVDelay"):
            temp = self.dooFixedAVDelayEntry.get()
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                int(temp)
                if (temp == '' or int(temp)<0):
                    messagebox.showinfo("ERROR","Please enter a valid value")
                    pass

                #Ensure value is in limited range
                elif(int(temp) < 70 or int(temp) > 300):
                    messagebox.showinfo("ERROR","The range is between 70 and 300")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("CONFIRMATION", "Replace current value?"):
                        messagebox.showinfo("DONE", "Success")
                        doo_fixedAVDelayEntry = temp
                        self.dooFixedAVDelayValue.config(text="Current Value: " + doo_fixedAVDelayEntry)
                        db.execute("UPDATE "+currentuser+" SET doo_fixedAVDelayEntry = ?", (doo_fixedAVDelayEntry,))
                        db.commit()

            except:
                messagebox.showinfo("ERROR","Please enter a valid value")
                pass
        #DOO END-------------------------------------------------------------------------------------------------------------------------------

        #AOOR BEGIN----------------------------------------------------------------------------------------------------------------------------
        #aoorLowerRateLimit
        if(value == "aoorLowerRateLimit"):
            temp = self.aoorLowerRateLimitEntry.get()
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                int(temp)
                if (temp == '' or int(temp)<0):
                    messagebox.showinfo("ERROR","Please enter a valid value")
                    pass

                #Ensure upper limit is larger than lower limit
                elif(int(self.aoorLowerRateLimitEntry.get()) >= int(aoor_upperRateLimitEntry) and int(aoor_upperRateLimitEntry) != 0 ):
                    messagebox.showinfo("ERROR","Please ensure your lower rate limit is lower than your upper rate limit")
                    pass

                #Ensure value is in limited range
                elif(int(temp) < 30 or int(temp) > 175):
                    messagebox.showinfo("ERROR","The range is between 30 and 175")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("CONFIRMATION", "Replace current value?"):
                        messagebox.showinfo("DONE", "Success")
                        aoor_lowerRateLimitEntry = temp
                        self.aoorLowerRateLimitValue.config(text="Current Value: " + aoor_lowerRateLimitEntry)
                        db.execute("UPDATE "+currentuser+" SET aoor_lowerRateLimitEntry = ?", (aoor_lowerRateLimitEntry,))
                        db.commit()

            except:
                messagebox.showinfo("ERROR","Please enter a valid value")
                pass

        #aoorUpperRateLimit
        if(value == "aoorUpperRateLimit"):
            temp = self.aoorUpperRateLimitEntry.get()
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                int(temp)
                if (temp == '' or int(temp)<0):
                    messagebox.showinfo("ERROR","Please enter a valid value")
                    pass

                #Ensure upper limit is larger than lower limit
                elif(int(aoor_lowerRateLimitEntry) >= int(self.aoorUpperRateLimitEntry.get()) and int(aoor_lowerRateLimitEntry) != 0 ):
                    messagebox.showinfo("ERROR","Please ensure your upper rate limit is higher than your lower rate limit")
                    pass

                #Ensure value is in limited range
                elif(int(temp) < 50 or int(temp) > 175):
                    messagebox.showinfo("ERROR","The range is between 50 and 175")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("CONFIRMATION", "Replace current value?"):
                        messagebox.showinfo("DONE", "Success")
                        aoor_upperRateLimitEntry = temp
                        self.aoorUpperRateLimitValue.config(text="Current Value: " + aoor_upperRateLimitEntry)
                        db.execute("UPDATE "+currentuser+" SET aoor_upperRateLimitEntry = ?", (aoor_upperRateLimitEntry,))
                        db.commit()

            except:
                messagebox.showinfo("ERROR","Please enter a valid value")
                pass

        #aoorAtrialAmplitude
        if(value == "aoorAtrialAmplitude"):
            temp = self.aoorAtrialAmplitudeEntry.get()
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                float(temp)
                if (temp == '' or float(temp)<0):
                    messagebox.showinfo("ERROR","Please enter a valid value")
                    pass
                #Ensure value is in limited range
                elif(float(temp) < 0 or float(temp) > 7.0):
                    messagebox.showinfo("ERROR","The range is between 0(off) and 7.0")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("CONFIRMATION", "Replace current value?"):
                        messagebox.showinfo("DONE", "Success")
                        aoor_atrialAmplitudeEntry = temp
                        self.aoorAtrialAmplitudeValue.config(text="Current Value: " + aoor_atrialAmplitudeEntry)
                        db.execute("UPDATE "+currentuser+" SET aoor_atrialAmplitudeEntry = ?", (aoor_atrialAmplitudeEntry,))
                        db.commit()

            except:
                messagebox.showinfo("ERROR","Please enter a valid value")
                pass

        #aoorAtrialPulseWidth
        if(value == "aoorAtrialPulseWidth"):
            temp = self.aoorAtrialPulseWidthEntry.get()
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                float(temp)
                if (temp == '' or float(temp)<0):
                    messagebox.showinfo("ERROR","Please enter a valid value")
                    pass

                #Ensure value is in limited range
                elif(float(temp) < 0.05 or float(temp) > 1.9):
                    messagebox.showinfo("ERROR","The range is between 0.05 and 1.9")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("CONFIRMATION", "Replace current value?"):
                        messagebox.showinfo("DONE", "Success")
                        aoor_atrialPulseWidthEntry = temp
                        self.aoorAtrialPulseWidthValue.config(text="Current Value: " + aoor_atrialPulseWidthEntry)
                        db.execute("UPDATE "+currentuser+" SET aoor_atrialPulseWidthEntry = ?", (aoor_atrialPulseWidthEntry,))
                        db.commit()

            except:
                messagebox.showinfo("ERROR","Please enter a valid value")
                pass

        #aoorMaximumSensorRate
        if(value == "aoorMaximumSensorRate"):
            temp = self.aoorMaximumSensorRateEntry.get()
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                int(temp)
                if (temp == '' or int(temp)<0):
                    messagebox.showinfo("ERROR","Please enter a valid value")
                    pass

                #Ensure value is in limited range
                elif(int(temp) < 50 or int(temp) > 175):
                    messagebox.showinfo("ERROR","The range is between 50 and 175")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("CONFIRMATION", "Replace current value?"):
                        messagebox.showinfo("DONE", "Success")
                        aoor_maximumSensorRateEntry = temp
                        self.aoorMaximumSensorRateValue.config(text="Current Value: " + aoor_maximumSensorRateEntry)
                        db.execute("UPDATE "+currentuser+" SET aoor_maximumSensorRateEntry = ?", (aoor_maximumSensorRateEntry,))
                        db.commit()

            except:
                messagebox.showinfo("ERROR","Please enter a valid value")
                pass

        #aoorActivityThreshold
        if(value == "aoorActivityThreshold"):
            temp = self.aoorActivityThresholdEntry.get()
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                str(temp)
                if(str(temp) != "V-Low" and str(temp) != "Low" and str(temp) != "Med-Low" and str(temp) != "Med" and str(temp) != "Med-High" and str(temp) != "High" and str(temp) != "V-High"):
                    messagebox.showinfo("ERROR","The range is between V-Low and V-High")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("CONFIRMATION", "Replace current value?"):
                        messagebox.showinfo("DONE", "Success")
                        aoor_activityThresholdEntry = temp
                        self.aoorActivityThresholdValue.config(text="Current Value: " + aoor_activityThresholdEntry)
                        db.execute("UPDATE "+currentuser+" SET aoor_activityThresholdEntry = ?", (aoor_activityThresholdEntry,))
                        db.commit()

            except:
                messagebox.showinfo("ERROR","Please enter a valid value")
                pass

        #aoorReactionTime
        if(value == "aoorReactionTime"):
            temp = self.aoorReactionTimeEntry.get()
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                int(temp)
                if (temp == '' or int(temp)<0):
                    messagebox.showinfo("ERROR","Please enter a valid value")
                    pass

                #Ensure value is in limited range
                elif(int(temp) < 10 or int(temp) > 50):
                    messagebox.showinfo("ERROR","The range is between 10 and 50")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("CONFIRMATION", "Replace current value?"):
                        messagebox.showinfo("DONE", "Success")
                        aoor_reactionTimeEntry = temp
                        self.aoorReactionTimeValue.config(text="Current Value: " + aoor_reactionTimeEntry)
                        db.execute("UPDATE "+currentuser+" SET aoor_reactionTimeEntry = ?", (aoor_reactionTimeEntry,))
                        db.commit()

            except:
                messagebox.showinfo("ERROR","Please enter a valid value")
                pass

        #aoorResponseFactor
        if(value == "aoorResponseFactor"):
            temp = self.aoorResponseFactorEntry.get()
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                int(temp)
                if (temp == '' or int(temp)<0):
                    messagebox.showinfo("ERROR","Please enter a valid value")
                    pass

                #Ensure value is in limited range
                elif(int(temp) < 1 or int(temp) > 16):
                    messagebox.showinfo("ERROR","The range is between 1 and 16")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("CONFIRMATION", "Replace current value?"):
                        messagebox.showinfo("DONE", "Success")
                        aoor_responseFactorEntry = temp
                        self.aoorResponseFactorValue.config(text="Current Value: " + aoor_responseFactorEntry)
                        db.execute("UPDATE "+currentuser+" SET aoor_responseFactorEntry = ?", (aoor_responseFactorEntry,))
                        db.commit()

            except:
                messagebox.showinfo("ERROR","Please enter a valid value")
                pass

        #aoorRecoveryTime
        if(value == "aoorRecoveryTime"):
            temp = self.aoorRecoveryTimeEntry.get()
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                int(temp)
                if (temp == '' or int(temp)<0):
                    messagebox.showinfo("ERROR","Please enter a valid value")
                    pass

                #Ensure value is in limited range
                elif(int(temp) < 2 or int(temp) > 16):
                    messagebox.showinfo("ERROR","The range is between 2 and 16")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("CONFIRMATION", "Replace current value?"):
                        messagebox.showinfo("DONE", "Success")
                        aoor_recoveryTimeEntry = temp
                        self.aoorRecoveryTimeValue.config(text="Current Value: " + aoor_recoveryTimeEntry)
                        db.execute("UPDATE "+currentuser+" SET aoor_recoveryTimeEntry = ?", (aoor_recoveryTimeEntry,))
                        db.commit()

            except:
                messagebox.showinfo("ERROR","Please enter a valid value")
                pass
        #AOOR END------------------------------------------------------------------------------------------------------------------------------

        #VOOR BEGIN----------------------------------------------------------------------------------------------------------------------------
        #voorLowerRateLimit
        if(value == "voorLowerRateLimit"):
            temp = self.voorLowerRateLimitEntry.get()
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                int(temp)
                if (temp == '' or int(temp)<0):
                    messagebox.showinfo("ERROR","Please enter a valid value")
                    pass

                #Ensure upper limit is larger than lower limit
                elif(int(self.voorLowerRateLimitEntry.get()) >= int(voor_upperRateLimitEntry) and int(voor_upperRateLimitEntry) != 0 ):
                    messagebox.showinfo("ERROR","Please ensure your lower rate limit is lower than your upper rate limit")
                    pass

                #Ensure value is in limited range
                elif(int(temp) < 30 or int(temp) > 175):
                    messagebox.showinfo("ERROR","The range is between 30 and 175")
                    pass
                
                #If everything is good update current value
                else:
                    if messagebox.askyesno("CONFIRMATION", "Replace current value?"):
                        messagebox.showinfo("DONE", "Success")
                        voor_lowerRateLimitEntry = temp
                        self.voorLowerRateLimitValue.config(text="Current Value: " + voor_lowerRateLimitEntry)
                        db.execute("UPDATE "+currentuser+" SET voor_lowerRateLimitEntry = ?", (voor_lowerRateLimitEntry,))
                        db.commit()
                        
            except:
                messagebox.showinfo("ERROR","Please enter a valid value")
                pass
        
        #voorUpperRateLimit
        if(value == "voorUpperRateLimit"):
            temp = self.voorUpperRateLimitEntry.get()
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                int(temp)
                if (temp == '' or int(temp)<0):
                    messagebox.showinfo("ERROR","Please enter a valid value")
                    pass

                #Ensure upper limit is larger than lower limit
                elif(int(voor_lowerRateLimitEntry) >= int(self.voorUpperRateLimitEntry.get()) and int(voor_lowerRateLimitEntry) != 0 ):
                    messagebox.showinfo("ERROR","Please ensure your upper rate limit is higher than your lower rate limit")
                    pass

                #Ensure value is in limited range
                elif(int(temp) < 50 or int(temp) > 175):
                    messagebox.showinfo("ERROR","The range is between 50 and 175")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("CONFIRMATION", "Replace current value?"):
                        messagebox.showinfo("DONE", "Success")
                        voor_upperRateLimitEntry = temp
                        self.voorUpperRateLimitValue.config(text="Current Value: " + voor_upperRateLimitEntry)
                        db.execute("UPDATE "+currentuser+" SET voor_upperRateLimitEntry = ?", (voor_upperRateLimitEntry,))
                        db.commit()

            except:
                messagebox.showinfo("ERROR","Please enter a valid value")
                pass

        #voorVentricularAmplitude
        if(value == "voorVentricularAmplitude"):
            temp = self.voorVentricularAmplitudeEntry.get()
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                float(temp)
                if (temp == '' or float(temp)<0):
                    messagebox.showinfo("ERROR","Please enter a valid value")
                    pass

                #Ensure value is in limited range
                elif(float(temp) < 0 or float(temp) > 7.0):
                    messagebox.showinfo("ERROR","The range is between 0(off) and 7.0")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("CONFIRMATION", "Replace current value?"):
                        messagebox.showinfo("DONE", "Success")
                        voor_ventricularAmplitudeEntry = temp
                        self.voorVentricularAmplitudeValue.config(text="Current Value: " + voor_ventricularAmplitudeEntry)
                        db.execute("UPDATE "+currentuser+" SET voor_ventricularAmplitudeEntry = ?", (voor_ventricularAmplitudeEntry,))
                        db.commit()

            except:
                messagebox.showinfo("ERROR","Please enter a valid value")
                pass

        #voorVentricularPulseWidth
        if(value == "voorVentricularPulseWidth"):
            temp = self.voorVentricularPulseWidthEntry.get()
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                float(temp)
                if (temp == '' or float(temp)<0):
                    messagebox.showinfo("ERROR","Please enter a valid value")
                    pass

                #Ensure value is in limited range
                elif(float(temp) < 0.05 or float(temp) > 1.9):
                    messagebox.showinfo("ERROR","The range is between 0.05 and 1.9")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("CONFIRMATION", "Replace current value?"):
                        messagebox.showinfo("DONE", "Success")
                        voor_ventricularPulseWidthEntry = temp
                        self.voorVentricularPulseWidthValue.config(text="Current Value: " + voor_ventricularPulseWidthEntry)
                        db.execute("UPDATE "+currentuser+" SET voor_ventricularPulseWidthEntry = ?", (voor_ventricularPulseWidthEntry,))
                        db.commit()

            except:
                messagebox.showinfo("ERROR","Please enter a valid value")
                pass

        #voorMaximumSensorRate
        if(value == "voorMaximumSensorRate"):
            temp = self.voorMaximumSensorRateEntry.get()
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                int(temp)
                if (temp == '' or int(temp)<0):
                    messagebox.showinfo("ERROR","Please enter a valid value")
                    pass

                #Ensure value is in limited range
                elif(int(temp) < 50 or int(temp) > 175):
                    messagebox.showinfo("ERROR","The range is between 50 and 175")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("CONFIRMATION", "Replace current value?"):
                        messagebox.showinfo("DONE", "Success")
                        voor_maximumSensorRateEntry = temp
                        self.voorMaximumSensorRateValue.config(text="Current Value: " + voor_maximumSensorRateEntry)
                        db.execute("UPDATE "+currentuser+" SET voor_maximumSensorRateEntry = ?", (voor_maximumSensorRateEntry,))
                        db.commit()

            except:
                messagebox.showinfo("ERROR","Please enter a valid value")
                pass

        #voorActivityThreshold
        if(value == "voorActivityThreshold"):
            temp = self.voorActivityThresholdEntry.get()
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                str(temp)
                if(str(temp) != "V-Low" and str(temp) != "Low" and str(temp) != "Med-Low" and str(temp) != "Med" and str(temp) != "Med-High" and str(temp) != "High" and str(temp) != "V-High"):
                    messagebox.showinfo("ERROR","The range is between V-Low and V-High")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("CONFIRMATION", "Replace current value?"):
                        messagebox.showinfo("DONE", "Success")
                        voor_activityThresholdEntry = temp
                        self.voorActivityThresholdValue.config(text="Current Value: " + voor_activityThresholdEntry)
                        db.execute("UPDATE "+currentuser+" SET voor_activityThresholdEntry = ?", (voor_activityThresholdEntry,))
                        db.commit()

            except:
                messagebox.showinfo("ERROR","Please enter a valid value")
                pass

        #voorReactionTime
        if(value == "voorReactionTime"):
            temp = self.voorReactionTimeEntry.get()
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                int(temp)
                if (temp == '' or int(temp)<0):
                    messagebox.showinfo("ERROR","Please enter a valid value")
                    pass

                #Ensure value is in limited range
                elif(int(temp) < 10 or int(temp) > 50):
                    messagebox.showinfo("ERROR","The range is between 10 and 50")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("CONFIRMATION", "Replace current value?"):
                        messagebox.showinfo("DONE", "Success")
                        voor_reactionTimeEntry = temp
                        self.voorReactionTimeValue.config(text="Current Value: " + voor_reactionTimeEntry)
                        db.execute("UPDATE "+currentuser+" SET voor_reactionTimeEntry = ?", (voor_reactionTimeEntry,))
                        db.commit()

            except:
                messagebox.showinfo("ERROR","Please enter a valid value")
                pass

        #voorResponseFactor
        if(value == "voorResponseFactor"):
            temp = self.voorResponseFactorEntry.get()
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                int(temp)
                if (temp == '' or int(temp)<0):
                    messagebox.showinfo("ERROR","Please enter a valid value")
                    pass

                #Ensure value is in limited range
                elif(int(temp) < 1 or int(temp) > 16):
                    messagebox.showinfo("ERROR","The range is between 1 and 16")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("CONFIRMATION", "Replace current value?"):
                        messagebox.showinfo("DONE", "Success")
                        voor_responseFactorEntry = temp
                        self.voorResponseFactorValue.config(text="Current Value: " + voor_responseFactorEntry)
                        db.execute("UPDATE "+currentuser+" SET voor_responseFactorEntry = ?", (voor_responseFactorEntry,))
                        db.commit()

            except:
                messagebox.showinfo("ERROR","Please enter a valid value")
                pass

        #voorRecoveryTime
        if(value == "voorRecoveryTime"):
            temp = self.voorRecoveryTimeEntry.get()
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                int(temp)
                if (temp == '' or int(temp)<0):
                    messagebox.showinfo("ERROR","Please enter a valid value")
                    pass

                #Ensure value is in limited range
                elif(int(temp) < 2 or int(temp) > 16):
                    messagebox.showinfo("ERROR","The range is between 2 and 16")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("CONFIRMATION", "Replace current value?"):
                        messagebox.showinfo("DONE", "Success")
                        voor_recoveryTimeEntry = temp
                        self.voorRecoveryTimeValue.config(text="Current Value: " + voor_recoveryTimeEntry)
                        db.execute("UPDATE "+currentuser+" SET voor_recoveryTimeEntry = ?", (voor_recoveryTimeEntry,))
                        db.commit()

            except:
                messagebox.showinfo("ERROR","Please enter a valid value")
                pass
        #VOOR END------------------------------------------------------------------------------------------------------------------------------

        #AAIR BEGIN----------------------------------------------------------------------------------------------------------------------------
        #aairLowerRateLimit
        if(value == "aairLowerRateLimit"):
            temp = self.aairLowerRateLimitEntry.get()
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                int(temp)
                if (temp == '' or int(temp)<0):
                    messagebox.showinfo("ERROR","Please enter a valid value")
                    pass
                #Ensure upper limit is larger than lower limit
                elif(int(self.aairLowerRateLimitEntry.get()) >= int(aair_upperRateLimitEntry) and int(aair_upperRateLimitEntry) != 0 ):
                    messagebox.showinfo("ERROR","Please ensure your lower rate limit is lower than your upper rate limit")
                    pass

                #Ensure value is in limited range
                elif(int(temp) < 30 or int(temp) > 175):
                    messagebox.showinfo("ERROR","The range is between 30 and 175")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("CONFIRMATION", "Replace current value?"):
                        messagebox.showinfo("DONE", "Success")
                        aair_lowerRateLimitEntry = temp
                        self.aairLowerRateLimitValue.config(text="Current Value: " + aair_lowerRateLimitEntry)
                        db.execute("UPDATE "+currentuser+" SET aair_lowerRateLimitEntry = ?", (aair_lowerRateLimitEntry,))
                        db.commit()

            except:
                messagebox.showinfo("ERROR","Please enter a valid value")
                pass

        #aairUpperRateLimit
        if(value == "aairUpperRateLimit"):
            temp = self.aairUpperRateLimitEntry.get()
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                int(temp)
                if (temp == '' or int(temp)<0):
                    messagebox.showinfo("ERROR","Please enter a valid value")
                    pass
                #Ensure upper limit is larger than lower limit
                elif(int(aair_lowerRateLimitEntry) >= int(self.aairUpperRateLimitEntry.get()) and int(aair_lowerRateLimitEntry) != 0 ):
                    messagebox.showinfo("ERROR","Please ensure your upper rate limit is higher than your lower rate limit")
                    pass

                #Ensure value is in limited range
                elif(int(temp) < 50 or int(temp) > 175):
                    messagebox.showinfo("ERROR","The range is between 50 and 175")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("CONFIRMATION", "Replace current value?"):
                        messagebox.showinfo("DONE", "Success")
                        aair_upperRateLimitEntry = temp
                        self.aairUpperRateLimitValue.config(text="Current Value: " + aair_upperRateLimitEntry)
                        db.execute("UPDATE "+currentuser+" SET aair_upperRateLimitEntry = ?", (aair_upperRateLimitEntry,))
                        db.commit()

            except:
                messagebox.showinfo("ERROR","Please enter a valid value")
                pass

        #aairAtrialAmplitude
        if(value == "aairAtrialAmplitude"):
            temp = self.aairAtrialAmplitudeEntry .get()
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                float(temp)
                if (temp == '' or float(temp)<0):
                    messagebox.showinfo("ERROR","Please enter a valid value")
                    pass

                #Ensure value is in limited range
                elif(float(temp) < 0 or float(temp) > 7.0):
                    messagebox.showinfo("ERROR","The range is between 0(off) and 7.0")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("CONFIRMATION", "Replace current value?"):
                        messagebox.showinfo("DONE", "Success")
                        aair_atrialAmplitudeEntry  = temp
                        self.aairAtrialAmplitudeValue.config(text="Current Value: " + aair_atrialAmplitudeEntry)
                        db.execute("UPDATE "+currentuser+" SET aair_atrialAmplitudeEntry = ?", (aair_atrialAmplitudeEntry,))
                        db.commit()

            except:
                messagebox.showinfo("ERROR","Please enter a valid value")
                pass

        #aairAtrialPulseWidth
        if(value == "aairAtrialPulseWidth"):
            temp = self.aairAtrialPulseWidthEntry.get()
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                float(temp)
                if (temp == '' or float(temp)<0):
                    messagebox.showinfo("ERROR","Please enter a valid value")
                    pass

                #Ensure value is in limited range
                elif(float(temp) < 0.05 or float(temp) > 1.9):
                    messagebox.showinfo("ERROR","The range is between 0.05 and 1.9")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("CONFIRMATION", "Replace current value?"):
                        messagebox.showinfo("DONE", "Success")
                        aair_atrialPulseWidthEntry = temp
                        self.aairAtrialPulseWidthValue.config(text="Current Value: " + aair_atrialPulseWidthEntry)
                        db.execute("UPDATE "+currentuser+" SET aair_atrialPulseWidthEntry = ?", (aair_atrialPulseWidthEntry,))
                        db.commit()

            except:
                messagebox.showinfo("ERROR","Please enter a valid value")
                pass

        #aairAtrialSensitivity
        if(value == "aairAtrialSensitivity"):
            temp = self.aairAtrialSensitivityEntry.get()
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                float(temp)
                if (temp == '' or float(temp)<0):
                    messagebox.showinfo("ERROR","Please enter a valid value")
                    pass

                #Ensure value is in limited range
                elif(float(temp) < 0.25 or float(temp) > 10.0):
                    messagebox.showinfo("ERROR","The range is between 0.25 and 10.0")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("CONFIRMATION", "Replace current value?"):
                        messagebox.showinfo("DONE", "Success")
                        aair_atrialSensitivityEntry = temp
                        self.aairAtrialSensitivityValue.config(text="Current Value: " + aair_atrialSensitivityEntry)
                        db.execute("UPDATE "+currentuser+" SET aair_atrialSensitivityEntry = ?", (aair_atrialSensitivityEntry,))
                        db.commit()

            except:
                messagebox.showinfo("ERROR","Please enter a valid value")
                pass

        #aairARP
        if(value == "aairARP"):
            temp = self.aairARPEntry.get()
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                int(temp)
                if (temp == '' or int(temp)<0):
                    messagebox.showinfo("ERROR","Please enter a valid value")
                    pass

                #Ensure value is in limited range
                elif(int(temp) < 150 or int(temp) > 500):
                    messagebox.showinfo("ERROR","The range is between 150 and 500")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("CONFIRMATION", "Replace current value?"):
                        messagebox.showinfo("DONE", "Success")
                        aair_ARPEntry = temp
                        self.aairARPValue.config(text="Current Value: " + aair_ARPEntry)
                        db.execute("UPDATE "+currentuser+" SET aair_ARPEntry = ?", (aair_ARPEntry,))
                        db.commit()

            except:
                messagebox.showinfo("ERROR","Please enter a valid value")
                pass

        #aairPVARP
        if(value == "aairPVARP"):
            temp = self.aairPVARPEntry.get()
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                int(temp)
                if (temp == '' or int(temp)<0):
                    messagebox.showinfo("ERROR","Please enter a valid value")
                    pass

                #Ensure value is in limited range
                elif(int(temp) < 150 or int(temp) > 500):
                    messagebox.showinfo("ERROR","The range is between 150 and 500")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("CONFIRMATION", "Replace current value?"):
                        messagebox.showinfo("DONE", "Success")
                        aair_PVARPEntry = temp
                        self.aairPVARPValue.config(text="Current Value: " + aair_PVARPEntry)
                        db.execute("UPDATE "+currentuser+" SET aair_PVARPEntry = ?", (aair_PVARPEntry,))
                        db.commit()

            except:
                messagebox.showinfo("ERROR","Please enter a valid value")
                pass

        #aairHysteresis
        if(value == "aairHysteresis"):
            temp = self.aairHysteresisEntry.get()
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                int(temp)
                if (temp == '' or int(temp)<0):
                    messagebox.showinfo("ERROR","Please enter a valid value")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("CONFIRMATION", "Replace current value?"):
                        messagebox.showinfo("DONE", "Success")
                        aair_hysteresisEntry = temp
                        self.aairHysteresisValue.config(text="Current Value: " + aair_hysteresisEntry)
                        db.execute("UPDATE "+currentuser+" SET aair_hysteresisEntry = ?", (aair_hysteresisEntry,))
                        db.commit()

            except:
                messagebox.showinfo("ERROR","Please enter a valid value")
                pass

        #aairRateSmoothing
        if(value == "aairRateSmoothing"):
            temp = self.aairRateSmoothingEntry.get()
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                int(temp)
                if (temp == '' or int(temp)<0):
                    messagebox.showinfo("ERROR","Please enter a valid value")
                    pass

                #Ensure value is in limited range
                elif(int(temp) < 0 or int(temp) > 25):
                    messagebox.showinfo("ERROR","The range is between 0(off) and 25")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("CONFIRMATION", "Replace current value?"):
                        messagebox.showinfo("DONE", "Success")
                        aair_rateSmoothingEntry = temp
                        self.aairRateSmoothingValue.config(text="Current Value: " + aair_rateSmoothingEntry)
                        db.execute("UPDATE "+currentuser+" SET aair_rateSmoothingEntry = ?", (aair_rateSmoothingEntry,))
                        db.commit()

            except:
                messagebox.showinfo("ERROR","Please enter a valid value")
                pass
        
        #aairMaximumSensorRate
        if(value == "aairMaximumSensorRate"):
            temp = self.aairMaximumSensorRateEntry.get()
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                int(temp)
                if (temp == '' or int(temp)<0):
                    messagebox.showinfo("ERROR","Please enter a valid value")
                    pass

                #Ensure value is in limited range
                elif(int(temp) < 50 or int(temp) > 175):
                    messagebox.showinfo("ERROR","The range is between 50 and 175")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("CONFIRMATION", "Replace current value?"):
                        messagebox.showinfo("DONE", "Success")
                        aair_maximumSensorRateEntry = temp
                        self.aairMaximumSensorRateValue.config(text="Current Value: " + aair_maximumSensorRateEntry)
                        db.execute("UPDATE "+currentuser+" SET aair_maximumSensorRateEntry = ?", (aair_maximumSensorRateEntry,))
                        db.commit()

            except:
                messagebox.showinfo("ERROR","Please enter a valid value")
                pass

        #aairActivityThreshold
        if(value == "aairActivityThreshold"):
            temp = self.aairActivityThresholdEntry.get()
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                str(temp)
                if(str(temp) != "V-Low" and str(temp) != "Low" and str(temp) != "Med-Low" and str(temp) != "Med" and str(temp) != "Med-High" and str(temp) != "High" and str(temp) != "V-High"):
                    messagebox.showinfo("ERROR","The range is between V-Low and V-High")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("CONFIRMATION", "Replace current value?"):
                        messagebox.showinfo("DONE", "Success")
                        aair_activityThresholdEntry = temp
                        self.aairActivityThresholdValue.config(text="Current Value: " + aair_activityThresholdEntry)
                        db.execute("UPDATE "+currentuser+" SET aair_activityThresholdEntry = ?", (aair_activityThresholdEntry,))
                        db.commit()

            except:
                messagebox.showinfo("ERROR","Please enter a valid value")
                pass

        #aairReactionTime
        if(value == "aairReactionTime"):
            temp = self.aairReactionTimeEntry.get()
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                int(temp)
                if (temp == '' or int(temp)<0):
                    messagebox.showinfo("ERROR","Please enter a valid value")
                    pass

                #Ensure value is in limited range
                elif(int(temp) < 10 or int(temp) > 50):
                    messagebox.showinfo("ERROR","The range is between 10 and 50")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("CONFIRMATION", "Replace current value?"):
                        messagebox.showinfo("DONE", "Success")
                        aair_reactionTimeEntry = temp
                        self.aairReactionTimeValue.config(text="Current Value: " + aair_reactionTimeEntry)
                        db.execute("UPDATE "+currentuser+" SET aair_reactionTimeEntry = ?", (aair_reactionTimeEntry,))
                        db.commit()

            except:
                messagebox.showinfo("ERROR","Please enter a valid value")
                pass

        #aairResponseFactor
        if(value == "aairResponseFactor"):
            temp = self.aairResponseFactorEntry.get()
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                int(temp)
                if (temp == '' or int(temp)<0):
                    messagebox.showinfo("ERROR","Please enter a valid value")
                    pass

                #Ensure value is in limited range
                elif(int(temp) < 1 or int(temp) > 16):
                    messagebox.showinfo("ERROR","The range is between 1 and 16")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("CONFIRMATION", "Replace current value?"):
                        messagebox.showinfo("DONE", "Success")
                        aair_responseFactorEntry = temp
                        self.aairResponseFactorValue.config(text="Current Value: " + aair_responseFactorEntry)
                        db.execute("UPDATE "+currentuser+" SET aair_responseFactorEntry = ?", (aair_responseFactorEntry,))
                        db.commit()

            except:
                messagebox.showinfo("ERROR","Please enter a valid value")
                pass

        #aairRecoveryTime
        if(value == "aairRecoveryTime"):
            temp = self.aairRecoveryTimeEntry.get()
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                int(temp)
                if (temp == '' or int(temp)<0):
                    messagebox.showinfo("ERROR","Please enter a valid value")
                    pass

                #Ensure value is in limited range
                elif(int(temp) < 2 or int(temp) > 16):
                    messagebox.showinfo("ERROR","The range is between 2 and 16")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("CONFIRMATION", "Replace current value?"):
                        messagebox.showinfo("DONE", "Success")
                        aair_recoveryTimeEntry = temp
                        self.aairRecoveryTimeValue.config(text="Current Value: " + aair_recoveryTimeEntry)
                        db.execute("UPDATE "+currentuser+" SET aair_recoveryTimeEntry = ?", (aair_recoveryTimeEntry,))
                        db.commit()

            except:
                messagebox.showinfo("ERROR","Please enter a valid value")
                pass
        #AAIR END------------------------------------------------------------------------------------------------------------------------------

        #VVIR BEGIN----------------------------------------------------------------------------------------------------------------------------
        #vvirLowerRateLimit
        if(value == "vvirLowerRateLimit"):
            temp = self.vvirLowerRateLimitEntry.get()
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                int(temp)
                if (temp == '' or int(temp)<0):
                    messagebox.showinfo("ERROR","Please enter a valid value")
                    pass

                #Ensure upper limit is larger than lower limit
                elif(int(self.vvirLowerRateLimitEntry.get()) >= int(vvir_upperRateLimitEntry) and int(vvir_upperRateLimitEntry) != 0 ):
                    messagebox.showinfo("ERROR","Please ensure your lower rate limit is lower than your upper rate limit")
                    pass

                #Ensure value is in limited range
                elif(int(temp) < 30 or int(temp) > 175):
                    messagebox.showinfo("ERROR","The range is between 30 and 175")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("CONFIRMATION", "Replace current value?"):
                        messagebox.showinfo("DONE", "Success")
                        vvir_lowerRateLimitEntry = temp
                        self.vvirLowerRateLimitValue.config(text="Current Value: " + vvir_lowerRateLimitEntry)
                        db.execute("UPDATE "+currentuser+" SET vvir_lowerRateLimitEntry = ?", (vvir_lowerRateLimitEntry,))
                        db.commit()

            except:
                messagebox.showinfo("ERROR","Please enter a valid value")
                pass

        #vvirUpperRateLimit
        if(value == "vvirUpperRateLimit"):
            temp = self.vvirUpperRateLimitEntry.get() 
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                int(temp)
                if (temp == '' or int(temp)<0):
                    messagebox.showinfo("ERROR","Please enter a valid value")
                    pass

                #Ensure upper limit is larger than lower limit
                elif(int(vvir_lowerRateLimitEntry) >= int(self.vvirUpperRateLimitEntry.get()) and int(vvir_lowerRateLimitEntry) != 0 ):
                    messagebox.showinfo("ERROR","Please ensure your upper rate limit is higher than your lower rate limit")
                    pass

                #Ensure value is in limited range
                elif(int(temp) < 50 or int(temp) > 175):
                    messagebox.showinfo("ERROR","The range is between 50 and 175")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("CONFIRMATION", "Replace current value?"):
                        messagebox.showinfo("DONE", "Success")
                        vvir_upperRateLimitEntry = temp
                        self.vvirUpperRateLimitValue.config(text="Current Value: " + vvir_upperRateLimitEntry)
                        db.execute("UPDATE "+currentuser+" SET vvir_upperRateLimitEntry = ?", (vvir_upperRateLimitEntry,))
                        db.commit()

            except:
                messagebox.showinfo("ERROR","Please enter a valid value")
                pass

        #vvirVentricularAmplitude
        if(value == "vvirVentricularAmplitude"):
            temp = self.vvirVentricularAmplitudeEntry.get() 
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                float(temp)
                if (temp == '' or float(temp)<0):
                    messagebox.showinfo("ERROR","Please enter a valid value")
                    pass

                #Ensure value is in limited range
                elif(float(temp) < 0 or float(temp) > 7.0):
                    messagebox.showinfo("ERROR","The range is between 0(off) and 7.0")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("CONFIRMATION", "Replace current value?"):
                        messagebox.showinfo("DONE", "Success")
                        vvir_ventricularAmplitudeEntry = temp
                        self.vvirVentricularAmplitudeValue.config(text="Current Value: " + vvir_ventricularAmplitudeEntry)
                        db.execute("UPDATE "+currentuser+" SET vvir_ventricularAmplitudeEntry = ?", (vvir_ventricularAmplitudeEntry,))
                        db.commit()

            except:
                messagebox.showinfo("ERROR","Please enter a valid value")
                pass

        #vvirVentricularPulseWidth
        if(value == "vvirVentricularPulseWidth"):
            temp = self.vvirVentricularPulseWidthEntry.get() 
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                float(temp)
                if (temp == '' or float(temp)<0):
                    messagebox.showinfo("ERROR","Please enter a valid value")
                    pass

                #Ensure value is in limited range
                elif(float(temp) < 0.05 or float(temp) > 1.9):
                    messagebox.showinfo("ERROR","The range is between 0.05 and 1.9")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("CONFIRMATION", "Replace current value?"):
                        messagebox.showinfo("DONE", "Success")
                        vvir_ventricularPulseWidthEntry = temp
                        self.vvirVentricularPulseWidthValue.config(text="Current Value: " + vvir_ventricularPulseWidthEntry)
                        db.execute("UPDATE "+currentuser+" SET vvir_ventricularPulseWidthEntry = ?", (vvir_ventricularPulseWidthEntry,))
                        db.commit()

            except:
                messagebox.showinfo("ERROR","Please enter a valid value")
                pass

        #vvirVentricularSensitivity
        if(value == "vvirVentricularSensitivity"):
            temp = self.vvirVentricularSensitivityEntry.get()
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                float(temp)
                if (temp == '' or float(temp)<0):
                    messagebox.showinfo("ERROR","Please enter a valid value")
                    pass

                #Ensure value is in limited range
                elif(float(temp) < 0.25 or float(temp) > 10.0):
                    messagebox.showinfo("ERROR","The range is between 0.25 and 10.0")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("CONFIRMATION", "Replace current value?"):
                        messagebox.showinfo("DONE", "Success")
                        vvir_ventricularSensitivityEntry = temp
                        self.vvirVentricularSensitivityValue.config(text="Current Value: " + vvir_ventricularSensitivityEntry)
                        db.execute("UPDATE "+currentuser+" SET vvir_ventricularSensitivityEntry = ?", (vvir_ventricularSensitivityEntry,))
                        db.commit()

            except:
                messagebox.showinfo("ERROR","Please enter a valid value")
                pass

        #vvirVRP
        if(value == "vvirVRP"):
            temp = self.vvirVRPEntry.get() 
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                int(temp)
                if (temp == '' or int(temp)<0):
                    messagebox.showinfo("ERROR","Please enter a valid value")
                    pass

                #Ensure value is in limited range
                elif(int(temp) < 150 or int(temp) > 500):
                    messagebox.showinfo("ERROR","The range is between 150 and 500")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("CONFIRMATION", "Replace current value?"):
                        messagebox.showinfo("DONE", "Success")
                        vvir_VRPEntry = temp
                        self.vvirVRPValue.config(text="Current Value: " + vvir_VRPEntry)
                        db.execute("UPDATE "+currentuser+" SET vvir_VRPEntry = ?", (vvir_VRPEntry,))
                        db.commit()

            except:
                messagebox.showinfo("ERROR","Please enter a valid value")
                pass

        #vvirHysteresis
        if(value == "vvirHysteresis"):
            temp = self.vvirHysteresisEntry.get() 
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                int(temp)
                if (temp == '' or int(temp)<0):
                    messagebox.showinfo("ERROR","Please enter a valid value")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("CONFIRMATION", "Replace current value?"):
                        messagebox.showinfo("DONE", "Success")
                        vvir_hysteresisEntry = temp
                        self.vvirHysteresisValue.config(text="Current Value: " + vvir_hysteresisEntry)
                        db.execute("UPDATE "+currentuser+" SET vvir_hysteresisEntry = ?", (vvir_hysteresisEntry,))
                        db.commit()

            except:
                messagebox.showinfo("ERROR","Please enter a valid value")
                pass

        #vvirRateSmoothing
        if(value == "vvirRateSmoothing"):
            temp = self.vvirRateSmoothingEntry.get()
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                int(temp)
                if (temp == '' or int(temp)<0):
                    messagebox.showinfo("ERROR","Please enter a valid value")
                    pass

                #Ensure value is in limited range
                elif(int(temp) < 0 or int(temp) > 25):
                    messagebox.showinfo("ERROR","The range is between 0(off) and 25")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("CONFIRMATION", "Replace current value?"):
                        messagebox.showinfo("DONE", "Success")
                        vvir_rateSmoothingEntry = temp
                        self.vvirRateSmoothingValue.config(text="Current Value: " + vvir_rateSmoothingEntry)
                        db.execute("UPDATE "+currentuser+" SET vvir_rateSmoothingEntry = ?", (vvir_rateSmoothingEntry,))
                        db.commit()

            except:
                messagebox.showinfo("ERROR","Please enter a valid value")
                pass
        
        #vvirMaximumSensorRate
        if(value == "vvirMaximumSensorRate"):
            temp = self.vvirMaximumSensorRateEntry.get()
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                int(temp)
                if (temp == '' or int(temp)<0):
                    messagebox.showinfo("ERROR","Please enter a valid value")
                    pass

                #Ensure value is in limited range
                elif(int(temp) < 50 or int(temp) > 175):
                    messagebox.showinfo("ERROR","The range is between 50 and 175")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("CONFIRMATION", "Replace current value?"):
                        messagebox.showinfo("DONE", "Success")
                        vvir_maximumSensorRateEntry = temp
                        self.vvirMaximumSensorRateValue.config(text="Current Value: " + vvir_maximumSensorRateEntry)
                        db.execute("UPDATE "+currentuser+" SET vvir_maximumSensorRateEntry = ?", (vvir_maximumSensorRateEntry,))
                        db.commit()

            except:
                messagebox.showinfo("ERROR","Please enter a valid value")
                pass

        #vvirActivityThreshold
        if(value == "vvirActivityThreshold"):
            temp = self.vvirActivityThresholdEntry.get()
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                str(temp)
                if(str(temp) != "V-Low" and str(temp) != "Low" and str(temp) != "Med-Low" and str(temp) != "Med" and str(temp) != "Med-High" and str(temp) != "High" and str(temp) != "V-High"):
                    messagebox.showinfo("ERROR","The range is between V-Low and V-High")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("CONFIRMATION", "Replace current value?"):
                        messagebox.showinfo("DONE", "Success")
                        vvir_activityThresholdEntry = temp
                        self.vvirActivityThresholdValue.config(text="Current Value: " + vvir_activityThresholdEntry)
                        db.execute("UPDATE "+currentuser+" SET vvir_activityThresholdEntry = ?", (vvir_activityThresholdEntry,))
                        db.commit()

            except:
                messagebox.showinfo("ERROR","Please enter a valid value")
                pass

        #vvirReactionTime
        if(value == "vvirReactionTime"):
            temp = self.vvirReactionTimeEntry.get()
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                int(temp)
                if (temp == '' or int(temp)<0):
                    messagebox.showinfo("ERROR","Please enter a valid value")
                    pass

                #Ensure value is in limited range
                elif(int(temp) < 10 or int(temp) > 50):
                    messagebox.showinfo("ERROR","The range is between 10 and 50")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("CONFIRMATION", "Replace current value?"):
                        messagebox.showinfo("DONE", "Success")
                        vvir_reactionTimeEntry = temp
                        self.vvirReactionTimeValue.config(text="Current Value: " + vvir_reactionTimeEntry)
                        db.execute("UPDATE "+currentuser+" SET vvir_reactionTimeEntry = ?", (vvir_reactionTimeEntry,))
                        db.commit()

            except:
                messagebox.showinfo("ERROR","Please enter a valid value")
                pass

        #vvirResponseFactor
        if(value == "vvirResponseFactor"):
            temp = self.vvirResponseFactorEntry.get()
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                int(temp)
                if (temp == '' or int(temp)<0):
                    messagebox.showinfo("ERROR","Please enter a valid value")
                    pass

                #Ensure value is in limited range
                elif(int(temp) < 1 or int(temp) > 16):
                    messagebox.showinfo("ERROR","The range is between 1 and 16")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("CONFIRMATION", "Replace current value?"):
                        messagebox.showinfo("DONE", "Success")
                        vvir_responseFactorEntry = temp
                        self.vvirResponseFactorValue.config(text="Current Value: " + vvir_responseFactorEntry)
                        db.execute("UPDATE "+currentuser+" SET vvir_responseFactorEntry = ?", (vvir_responseFactorEntry,))
                        db.commit()

            except:
                messagebox.showinfo("ERROR","Please enter a valid value")
                pass

        #vvirRecoveryTime
        if(value == "vvirRecoveryTime"):
            temp = self.vvirRecoveryTimeEntry.get()
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                int(temp)
                if (temp == '' or int(temp)<0):
                    messagebox.showinfo("ERROR","Please enter a valid value")
                    pass

                #Ensure value is in limited range
                elif(int(temp) < 2 or int(temp) > 16):
                    messagebox.showinfo("ERROR","The range is between 2 and 16")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("CONFIRMATION", "Replace current value?"):
                        messagebox.showinfo("DONE", "Success")
                        vvir_recoveryTimeEntry = temp
                        self.vvirRecoveryTimeValue.config(text="Current Value: " + vvir_recoveryTimeEntry)
                        db.execute("UPDATE "+currentuser+" SET vvir_recoveryTimeEntry = ?", (vvir_recoveryTimeEntry,))
                        db.commit()

            except:
                messagebox.showinfo("ERROR","Please enter a valid value")
                pass
        #VVIR END------------------------------------------------------------------------------------------------------------------------------

        #DOOR BEGIN----------------------------------------------------------------------------------------------------------------------------
        #doorLowerRateLimit
        if(value == "doorLowerRateLimit"):
            temp = self.doorLowerRateLimitEntry.get()
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                int(temp)
                if (temp == '' or int(temp)<0):
                    messagebox.showinfo("ERROR","Please enter a valid value")
                    pass

                #Ensure upper limit is larger than lower limit
                elif(int(self.doorLowerRateLimitEntry.get()) >= int(door_upperRateLimitEntry) and int(door_upperRateLimitEntry) != 0 ):
                    messagebox.showinfo("ERROR","Please ensure your lower rate limit is lower than your upper rate limit")
                    pass

                #Ensure value is in limited range
                elif(int(temp) < 30 or int(temp) > 175):
                    messagebox.showinfo("ERROR","The range is between 30 and 175")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("CONFIRMATION", "Replace current value?"):
                        messagebox.showinfo("DONE", "Success")
                        door_lowerRateLimitEntry = temp
                        self.doorLowerRateLimitValue.config(text="Current Value: " + door_lowerRateLimitEntry)
                        db.execute("UPDATE "+currentuser+" SET door_lowerRateLimitEntry = ?", (door_lowerRateLimitEntry,))
                        db.commit()

            except:
                messagebox.showinfo("ERROR","Please enter a valid value")
                pass

        #doorUpperRateLimit
        if(value == "doorUpperRateLimit"):
            temp = self.doorUpperRateLimitEntry.get()
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                int(temp)
                if (temp == '' or int(temp)<0):
                    messagebox.showinfo("ERROR","Please enter a valid value")
                    pass

                #Ensure upper limit is larger than lower limit
                elif(int(door_lowerRateLimitEntry) >= int(self.doorUpperRateLimitEntry.get()) and int(door_lowerRateLimitEntry) != 0 ):
                    messagebox.showinfo("ERROR","Please ensure your upper rate limit is higher than your lower rate limit")
                    pass

                #Ensure value is in limited range
                elif(int(temp) < 50 or int(temp) > 175):
                    messagebox.showinfo("ERROR","The range is between 50 and 175")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("CONFIRMATION", "Replace current value?"):
                        messagebox.showinfo("DONE", "Success")
                        door_upperRateLimitEntry = temp
                        self.doorUpperRateLimitValue.config(text="Current Value: " + door_upperRateLimitEntry)
                        db.execute("UPDATE "+currentuser+" SET door_upperRateLimitEntry = ?", (door_upperRateLimitEntry,))
                        db.commit()

            except:
                messagebox.showinfo("ERROR","Please enter a valid value")
                pass

        #doorAtrialAmplitude
        if(value == "doorAtrialAmplitude"):
            temp = self.doorAtrialAmplitudeEntry.get()
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                float(temp)
                if (temp == '' or float(temp)<0):
                    messagebox.showinfo("ERROR","Please enter a valid value")
                    pass
                #Ensure value is in limited range
                elif(float(temp) < 0 or float(temp) > 7.0):
                    messagebox.showinfo("ERROR","The range is between 0(off) and 7.0")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("CONFIRMATION", "Replace current value?"):
                        messagebox.showinfo("DONE", "Success")
                        door_atrialAmplitudeEntry = temp
                        self.doorAtrialAmplitudeValue.config(text="Current Value: " + door_atrialAmplitudeEntry)
                        db.execute("UPDATE "+currentuser+" SET door_atrialAmplitudeEntry = ?", (door_atrialAmplitudeEntry,))
                        db.commit()

            except:
                messagebox.showinfo("ERROR","Please enter a valid value")
                pass

        #doorAtrialPulseWidth
        if(value == "doorAtrialPulseWidth"):
            temp = self.doorAtrialPulseWidthEntry.get()
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                float(temp)
                if (temp == '' or float(temp)<0):
                    messagebox.showinfo("ERROR","Please enter a valid value")
                    pass

                #Ensure value is in limited range
                elif(float(temp) < 0.05 or float(temp) > 1.9):
                    messagebox.showinfo("ERROR","The range is between 0.05 and 1.9")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("CONFIRMATION", "Replace current value?"):
                        messagebox.showinfo("DONE", "Success")
                        door_atrialPulseWidthEntry = temp
                        self.doorAtrialPulseWidthValue.config(text="Current Value: " + door_atrialPulseWidthEntry)
                        db.execute("UPDATE "+currentuser+" SET door_atrialPulseWidthEntry = ?", (door_atrialPulseWidthEntry,))
                        db.commit()

            except:
                messagebox.showinfo("ERROR","Please enter a valid value")
                pass
        
        #doorVentricularAmplitude
        if(value == "doorVentricularAmplitude"):
            temp = self.doorVentricularAmplitudeEntry.get()
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                float(temp)
                if (temp == '' or float(temp)<0):
                    messagebox.showinfo("ERROR","Please enter a valid value")
                    pass

                #Ensure value is in limited range
                elif(float(temp) < 0 or float(temp) > 7.0):
                    messagebox.showinfo("ERROR","The range is between 0(off) and 7.0")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("CONFIRMATION", "Replace current value?"):
                        messagebox.showinfo("DONE", "Success")
                        door_ventricularAmplitudeEntry = temp
                        self.doorVentricularAmplitudeValue.config(text="Current Value: " + door_ventricularAmplitudeEntry)
                        db.execute("UPDATE "+currentuser+" SET door_ventricularAmplitudeEntry = ?", (door_ventricularAmplitudeEntry,))
                        db.commit()

            except:
                messagebox.showinfo("ERROR","Please enter a valid value")
                pass

        #doorVentricularPulseWidth
        if(value == "doorVentricularPulseWidth"):
            temp = self.doorVentricularPulseWidthEntry.get()
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                float(temp)
                if (temp == '' or float(temp)<0):
                    messagebox.showinfo("ERROR","Please enter a valid value")
                    pass

                #Ensure value is in limited range
                elif(float(temp) < 0.05 or float(temp) > 1.9):
                    messagebox.showinfo("ERROR","The range is between 0.05 and 1.9")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("CONFIRMATION", "Replace current value?"):
                        messagebox.showinfo("DONE", "Success")
                        door_ventricularPulseWidthEntry = temp
                        self.doorVentricularPulseWidthValue.config(text="Current Value: " + door_ventricularPulseWidthEntry)
                        db.execute("UPDATE "+currentuser+" SET door_ventricularPulseWidthEntry = ?", (door_ventricularPulseWidthEntry,))
                        db.commit()

            except:
                messagebox.showinfo("ERROR","Please enter a valid value")
                pass
        
        #doorFixedAVDelay
        if(value == "doorFixedAVDelay"):
            temp = self.doorFixedAVDelayEntry.get()
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                int(temp)
                if (temp == '' or int(temp)<0):
                    messagebox.showinfo("ERROR","Please enter a valid value")
                    pass

                #Ensure value is in limited range
                elif(int(temp) < 70 or int(temp) > 300):
                    messagebox.showinfo("ERROR","The range is between 70 and 300")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("CONFIRMATION", "Replace current value?"):
                        messagebox.showinfo("DONE", "Success")
                        door_fixedAVDelayEntry = temp
                        self.doorFixedAVDelayValue.config(text="Current Value: " + door_fixedAVDelayEntry)
                        db.execute("UPDATE "+currentuser+" SET door_fixedAVDelayEntry = ?", (door_fixedAVDelayEntry,))
                        db.commit()

            except:
                messagebox.showinfo("ERROR","Please enter a valid value")
                pass
        
        #doorMaximumSensorRate
        if(value == "doorMaximumSensorRate"):
            temp = self.doorMaximumSensorRateEntry.get()
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                int(temp)
                if (temp == '' or int(temp)<0):
                    messagebox.showinfo("ERROR","Please enter a valid value")
                    pass

                #Ensure value is in limited range
                elif(int(temp) < 50 or int(temp) > 175):
                    messagebox.showinfo("ERROR","The range is between 50 and 175")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("CONFIRMATION", "Replace current value?"):
                        messagebox.showinfo("DONE", "Success")
                        door_maximumSensorRateEntry = temp
                        self.doorMaximumSensorRateValue.config(text="Current Value: " + door_maximumSensorRateEntry)
                        db.execute("UPDATE "+currentuser+" SET door_maximumSensorRateEntry = ?", (door_maximumSensorRateEntry,))
                        db.commit()

            except:
                messagebox.showinfo("ERROR","Please enter a valid value")
                pass

        #doorActivityThreshold
        if(value == "doorActivityThreshold"):
            temp = self.doorActivityThresholdEntry.get()
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                str(temp)
                if(str(temp) != "V-Low" and str(temp) != "Low" and str(temp) != "Med-Low" and str(temp) != "Med" and str(temp) != "Med-High" and str(temp) != "High" and str(temp) != "V-High"):
                    messagebox.showinfo("ERROR","The range is between V-Low and V-High")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("CONFIRMATION", "Replace current value?"):
                        messagebox.showinfo("DONE", "Success")
                        door_activityThresholdEntry = temp
                        self.doorActivityThresholdValue.config(text="Current Value: " + door_activityThresholdEntry)
                        db.execute("UPDATE "+currentuser+" SET door_activityThresholdEntry = ?", (door_activityThresholdEntry,))
                        db.commit()

            except:
                messagebox.showinfo("ERROR","Please enter a valid value")
                pass

        #doorReactionTime
        if(value == "doorReactionTime"):
            temp = self.doorReactionTimeEntry.get()
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                int(temp)
                if (temp == '' or int(temp)<0):
                    messagebox.showinfo("ERROR","Please enter a valid value")
                    pass

                #Ensure value is in limited range
                elif(int(temp) < 10 or int(temp) > 50):
                    messagebox.showinfo("ERROR","The range is between 10 and 50")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("CONFIRMATION", "Replace current value?"):
                        messagebox.showinfo("DONE", "Success")
                        door_reactionTimeEntry = temp
                        self.doorReactionTimeValue.config(text="Current Value: " + door_reactionTimeEntry)
                        db.execute("UPDATE "+currentuser+" SET door_reactionTimeEntry = ?", (door_reactionTimeEntry,))
                        db.commit()

            except:
                messagebox.showinfo("ERROR","Please enter a valid value")
                pass

        #doorResponseFactor
        if(value == "doorResponseFactor"):
            temp = self.doorResponseFactorEntry.get()
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                int(temp)
                if (temp == '' or int(temp)<0):
                    messagebox.showinfo("ERROR","Please enter a valid value")
                    pass

                #Ensure value is in limited range
                elif(int(temp) < 1 or int(temp) > 16):
                    messagebox.showinfo("ERROR","The range is between 1 and 16")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("CONFIRMATION", "Replace current value?"):
                        messagebox.showinfo("DONE", "Success")
                        door_responseFactorEntry = temp
                        self.doorResponseFactorValue.config(text="Current Value: " + door_responseFactorEntry)
                        db.execute("UPDATE "+currentuser+" SET door_responseFactorEntry = ?", (door_responseFactorEntry,))
                        db.commit()

            except:
                messagebox.showinfo("ERROR","Please enter a valid value")
                pass

        #doorRecoveryTime
        if(value == "doorRecoveryTime"):
            temp = self.doorRecoveryTimeEntry.get()
            #Try/access to sanitize user input and ask for confirmation if there are no errors
            try:
                int(temp)
                if (temp == '' or int(temp)<0):
                    messagebox.showinfo("ERROR","Please enter a valid value")
                    pass

                #Ensure value is in limited range
                elif(int(temp) < 2 or int(temp) > 16):
                    messagebox.showinfo("ERROR","The range is between 2 and 16")
                    pass

                #If everything is good update current value
                else:
                    if messagebox.askyesno("CONFIRMATION", "Replace current value?"):
                        messagebox.showinfo("DONE", "Success")
                        door_recoveryTimeEntry = temp
                        self.doorRecoveryTimeValue.config(text="Current Value: " + door_recoveryTimeEntry)
                        db.execute("UPDATE "+currentuser+" SET door_recoveryTimeEntry = ?", (door_recoveryTimeEntry,))
                        db.commit()

            except:
                messagebox.showinfo("ERROR","Please enter a valid value")
                pass
        #DOOR END------------------------------------------------------------------------------------------------------------------------------

    #Method used to log off user
    def logOff(self):
        if messagebox.askyesno("LOGOFF", "Do you want to log off?"):
            self.master.destroy()
            main()
            #exit()

    #Method to exit application
    def on_exit(self):
        if messagebox.askyesno("EXIT", "Do you want to quit the application?"):
            exit()

    #New window method
    def new_window(self,window):
        self.newWindow = tk.Toplevel(self.master)
        self.app = window(self.newWindow)
    
    #Method for closing windows
    def close_windows(self):
        self.master.destroy()
        exit()


    """def _graph_btn_clicked(self):
    self.new_window(Graph)"""

    def DCMgraph(self,value):
        #Global Variables
        #AOO
        global aoo_lowerRateLimitEntry,aoo_upperRateLimitEntry,aoo_atrialAmplitudeEntry,aoo_atrialPulseWidthEntry 
        #VOO
        global voo_lowerRateLimitEntry,voo_upperRateLimitEntry,voo_ventricularAmplitudeEntry,voo_ventricularPulseWidthEntry
        #AAI
        global aai_lowerRateLimitEntry,aai_upperRateLimitEntry,aai_atrialAmplitudeEntry,aai_atrialPulseWidthEntry,aai_atrialSensitivityEntry,aai_ARPEntry,aai_PVARPEntry,aai_hysteresisEntry,aai_rateSmoothingEntry
        #VVI
        global vvi_lowerRateLimitEntry,vvi_upperRateLimitEntry,vvi_ventricularAmplitudeEntry,vvi_ventricularPulseWidthEntry,vvi_ventricularSensitivityEntry,vvi_VRPEntry,vvi_hysteresisEntry,vvi_rateSmoothingEntry
        #DOO
        global doo_lowerRateLimitEntry,doo_upperRateLimitEntry,doo_atrialAmplitudeEntry,doo_atrialPulseWidthEntry,doo_ventricularAmplitudeEntry,doo_ventricularPulseWidthEntry,doo_fixedAVDelayEntry

        #AOOR
        global aoor_lowerRateLimitEntry, aoor_upperRateLimitEntry, aoor_atrialAmplitudeEntry, aoor_atrialPulseWidthEntry, aoor_maximumSensorRateEntry, aoor_activityThresholdEntry, aoor_reactionTimeEntry, aoor_responseFactorEntry, aoor_recoveryTimeEntry
        #VOOR
        global voor_lowerRateLimitEntry, voor_upperRateLimitEntry, voor_ventricularAmplitudeEntry, voor_ventricularPulseWidthEntry, voor_maximumSensorRateEntry, voor_activityThresholdEntry, voor_reactionTimeEntry, voor_responseFactorEntry, voor_recoveryTimeEntry
        #AAIR
        global aair_lowerRateLimitEntry, aair_upperRateLimitEntry, aair_atrialAmplitudeEntry, aair_atrialPulseWidthEntry, aair_atrialSensitivityEntry, aair_ARPEntry, aair_PVARPEntry, aair_hysteresisEntry, aair_rateSmoothingEntry, aair_maximumSensorRateEntry, aair_activityThresholdEntry, aair_reactionTimeEntry, aair_responseFactorEntry, aair_recoveryTimeEntry
        #VVIR
        global vvir_lowerRateLimitEntry, vvir_upperRateLimitEntry, vvir_ventricularAmplitudeEntry, vvir_ventricularPulseWidthEntry, vvir_ventricularSensitivityEntry, vvir_VRPEntry, vvir_hysteresisEntry, vvir_rateSmoothingEntry, vvir_maximumSensorRateEntry, vvir_activityThresholdEntry, vvir_reactionTimeEntry, vvir_responseFactorEntry, vvir_recoveryTimeEntry
        #DOOR
        global door_lowerRateLimitEntry, door_upperRateLimitEntry, door_atrialAmplitudeEntry, door_atrialPulseWidthEntry, door_ventricularAmplitudeEntry, door_ventricularPulseWidthEntry, door_maximumSensorRateEntry, door_fixedAVDelayEntry, door_activityThresholdEntry, door_reactionTimeEntry, door_responseFactorEntry, door_recoveryTimeEntry
        
        fig = plt.figure()
        AtrialAX = fig.add_subplot(1,2,1)
        VentricularAX = fig.add_subplot(1,2,2)
        fig.show()

        i = 0
        timeList = []
        AtrialAMP, VentricularAMP = [], []

        if (value == "aoo"):
            PulseWidth = float(aoo_atrialPulseWidthEntry)
            AtrialPulseAMP = float(aoo_atrialAmplitudeEntry)
            VentricularPulseAMP = 0

            while i!=10:
                timeList.append(i)
                if (i%PulseWidth==0):
                    AtrialAMP.append(AtrialPulseAMP)
                    VentricularAMP.append(VentricularPulseAMP)
                else:
                    AtrialAMP.append(0)
                    VentricularAMP.append(0)


                AtrialAX.plot(timeList, AtrialAMP, color='r')

                VentricularAX.plot(timeList, VentricularAMP, color='b')

                fig.canvas.draw()

                AtrialAX.set_xlim(left=max(0, i-10), right=i+10)
                VentricularAX.set_xlim(left=max(0, i-10), right=i+10)

                time.sleep(0.5)

                i += 1

        if (value == "voo"):
            PulseWidth = float(voo_ventricularPulseWidthEntry)
            AtrialPulseAMP = 0
            VentricularPulseAMP = float(voo_ventricularAmplitudeEntry)

            while i!=10:
                timeList.append(i)
                if (i%PulseWidth==0):
                    AtrialAMP.append(AtrialPulseAMP)
                    VentricularAMP.append( VentricularPulseAMP)
                else:
                    AtrialAMP.append(0)
                    VentricularAMP.append(0)


                AtrialAX.plot(timeList, AtrialAMP, color='r')

                VentricularAX.plot(timeList, VentricularAMP, color='b')

                fig.canvas.draw()

                AtrialAX.set_xlim(left=max(0, i-10), right=i+10)
                VentricularAX.set_xlim(left=max(0, i-10), right=i+10)

                time.sleep(0.5)

                i += 1
        
        if (value == "aai"):
            PulseWidth = float(aai_atrialPulseWidthEntry)
            AtrialPulseAMP = float(aai_atrialAmplitudeEntry)
            VentricularPulseAMP = 0

            while i!=10:
                timeList.append(i)
                if (i%PulseWidth==0):
                    AtrialAMP.append(AtrialPulseAMP)
                    VentricularAMP.append(VentricularPulseAMP)
                else:
                    AtrialAMP.append(0)
                    VentricularAMP.append(0)


                AtrialAX.plot(timeList, AtrialAMP, color='r')

                VentricularAX.plot(timeList, VentricularAMP, color='b')

                fig.canvas.draw()

                AtrialAX.set_xlim(left=max(0, i-10), right=i+10)
                VentricularAX.set_xlim(left=max(0, i-10), right=i+10)

                time.sleep(0.5)

                i += 1
        
        if (value == "vvi"):
            PulseWidth = float(vvi_ventricularPulseWidthEntry)
            AtrialPulseAMP = 0
            VentricularPulseAMP = float(vvi_ventricularAmplitudeEntry)

            while i!=10:
                timeList.append(i)
                if (i%PulseWidth==0):
                    AtrialAMP.append(AtrialPulseAMP)
                    VentricularAMP.append( VentricularPulseAMP)
                else:
                    AtrialAMP.append(0)
                    VentricularAMP.append(0)


                AtrialAX.plot(timeList, AtrialAMP, color='r')

                VentricularAX.plot(timeList, VentricularAMP, color='b')

                fig.canvas.draw()

                AtrialAX.set_xlim(left=max(0, i-10), right=i+10)
                VentricularAX.set_xlim(left=max(0, i-10), right=i+10)

                time.sleep(0.5)

                i += 1
        
        if (value == "doo"):
            AtrialPulseAMP = float(doo_atrialAmplitudeEntry)
            AtrialPulsePulseWidth = float(doo_atrialPulseWidthEntry)
            
            VentricularPulseAMP = float(doo_ventricularAmplitudeEntry)
            VentricularPulseWidth = float(doo_ventricularPulseWidthEntry)

            while i!=10:
                timeList.append(i)
                if (i%AtrialPulsePulseWidth==0):
                    AtrialAMP.append(AtrialPulseAMP)
                else:
                    AtrialAMP.append(0)
                    
                if (i%VentricularPulseWidth==0):
                    VentricularAMP.append(VentricularPulseAMP)
                else:
                    VentricularAMP.append(0)
                   

                AtrialAX.plot(timeList, AtrialAMP, color='r')

                VentricularAX.plot(timeList, VentricularAMP, color='b')

                fig.canvas.draw()

                AtrialAX.set_xlim(left=max(0, i-10), right=i+10)
                VentricularAX.set_xlim(left=max(0, i-10), right=i+10)

                time.sleep(0.5)

                i += 1
        
        if (value == "aoor"):
            PulseWidth = float(aoor_atrialPulseWidthEntry)
            AtrialPulseAMP = float(aoor_atrialAmplitudeEntry)
            VentricularPulseAMP = 0

            while i!=10:
                timeList.append(i)
                if (i%PulseWidth==0):
                    AtrialAMP.append(AtrialPulseAMP)
                    VentricularAMP.append(VentricularPulseAMP)
                else:
                    AtrialAMP.append(0)
                    VentricularAMP.append(0)


                AtrialAX.plot(timeList, AtrialAMP, color='r')

                VentricularAX.plot(timeList, VentricularAMP, color='b')

                fig.canvas.draw()

                AtrialAX.set_xlim(left=max(0, i-10), right=i+10)
                VentricularAX.set_xlim(left=max(0, i-10), right=i+10)

                time.sleep(0.5)

                i += 1

        if (value == "voor"):
            PulseWidth = float(voor_ventricularPulseWidthEntry)
            AtrialPulseAMP = 0
            VentricularPulseAMP = float(voor_ventricularAmplitudeEntry)

            while i!=10:
                timeList.append(i)
                if (i%PulseWidth==0):
                    AtrialAMP.append(AtrialPulseAMP)
                    VentricularAMP.append( VentricularPulseAMP)
                else:
                    AtrialAMP.append(0)
                    VentricularAMP.append(0)


                AtrialAX.plot(timeList, AtrialAMP, color='r')

                VentricularAX.plot(timeList, VentricularAMP, color='b')

                fig.canvas.draw()

                AtrialAX.set_xlim(left=max(0, i-10), right=i+10)
                VentricularAX.set_xlim(left=max(0, i-10), right=i+10)

                time.sleep(0.5)

                i += 1
        
        if (value == "aair"):
            PulseWidth = float(aair_atrialPulseWidthEntry)
            AtrialPulseAMP = float(aair_atrialAmplitudeEntry)
            VentricularPulseAMP = 0

            while i!=10:
                timeList.append(i)
                if (i%PulseWidth==0):
                    AtrialAMP.append(AtrialPulseAMP)
                    VentricularAMP.append(VentricularPulseAMP)
                else:
                    AtrialAMP.append(0)
                    VentricularAMP.append(0)


                AtrialAX.plot(timeList, AtrialAMP, color='r')

                VentricularAX.plot(timeList, VentricularAMP, color='b')

                fig.canvas.draw()

                AtrialAX.set_xlim(left=max(0, i-10), right=i+10)
                VentricularAX.set_xlim(left=max(0, i-10), right=i+10)

                time.sleep(0.5)

                i += 1
        
        if (value == "vvir"):
            PulseWidth = float(vvir_ventricularPulseWidthEntry)
            AtrialPulseAMP = 0
            VentricularPulseAMP = float(vvir_ventricularAmplitudeEntry)

            while i!=10:
                timeList.append(i)
                if (i%PulseWidth==0):
                    AtrialAMP.append(AtrialPulseAMP)
                    VentricularAMP.append( VentricularPulseAMP)
                else:
                    AtrialAMP.append(0)
                    VentricularAMP.append(0)


                AtrialAX.plot(timeList, AtrialAMP, color='r')

                VentricularAX.plot(timeList, VentricularAMP, color='b')

                fig.canvas.draw()

                AtrialAX.set_xlim(left=max(0, i-10), right=i+10)
                VentricularAX.set_xlim(left=max(0, i-10), right=i+10)

                time.sleep(0.5)

                i += 1
        
        if (value == "door"):
            AtrialPulseAMP = float(door_atrialAmplitudeEntry)
            AtrialPulsePulseWidth = float(door_atrialPulseWidthEntry)
            
            VentricularPulseAMP = float(door_ventricularAmplitudeEntry)
            VentricularPulseWidth = float(door_ventricularPulseWidthEntry)

            while i!=10:
                timeList.append(i)
                if (i%AtrialPulsePulseWidth==0):
                    AtrialAMP.append(AtrialPulseAMP)
                else:
                    AtrialAMP.append(0)
                    
                if (i%VentricularPulseWidth==0):
                    VentricularAMP.append(VentricularPulseAMP)
                else:
                    VentricularAMP.append(0)
                   

                AtrialAX.plot(timeList, AtrialAMP, color='r')

                VentricularAX.plot(timeList, VentricularAMP, color='b')

                fig.canvas.draw()

                AtrialAX.set_xlim(left=max(0, i-10), right=i+10)
                VentricularAX.set_xlim(left=max(0, i-10), right=i+10)

                time.sleep(0.5)

                i += 1



        plt.show()

"""class Graph:
    def __init__(self, master):
        #General paramters
        self.master = master
        self.master.title("Graph")
        self.frame = tk.Frame(self.master)
        self.master.resizable(width=False, height=False)
        self.DCMgraph()
    
    def DCMgraph(self):
        
        fig = plt.figure()
        AtrialAX = fig.add_subplot(1,2,1)
        VentricularAX = fig.add_subplot(1,2,2)
        fig.show()

        i = 0
        timeList = []
        AtrialAMP, VentricularAMP = [], []


        PulseWidth = 5
        AtrialPulseAMP = 6
        VentricularPulseAMP = 0

        while i!=10:
            timeList.append(i)
            if (i%PulseWidth==0):
                AtrialAMP.append(AtrialPulseAMP)
                VentricularAMP.append( VentricularPulseAMP)
            else:
                AtrialAMP.append(0)
                VentricularAMP.append(0)


            AtrialAX.plot(timeList, AtrialAMP, color='r')

            VentricularAX.plot(timeList, VentricularAMP, color='b')

            fig.canvas.draw()

            AtrialAX.set_xlim(left=max(0, i-10), right=i+10)
            VentricularAX.set_xlim(left=max(0, i-10), right=i+10)

            time.sleep(0.5)

            i += 1

        plt.show()"""

#Main function that runs everything
def main():

    #Run Tkinter
    root = tk.Tk()
    app = WelcomeFrame(root)
    root.mainloop()

if __name__ == '__main__':
    main()